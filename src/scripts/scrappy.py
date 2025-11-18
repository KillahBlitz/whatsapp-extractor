import re
import time
from typing import List, Tuple, Callable, Optional
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.remote.webelement import WebElement
from .save_data import save_to_csv, normalize_phone, clean_name
from .errors import log_info, log_success, log_warning, log_error, handle_exception, safe_quit
  
# configuracion
CHROME_USER_DATA_DIR = r'C:\Users\emanu\AppData\Local\Google\Chrome\User Data\Profile 1'

# funciones auxiliares

def extract_from_card(card: WebElement) -> Tuple[str, str]:
    name = ""
    number = ""
    try:
        # extrae nombre visible
        try:
            name = card.find_element(By.XPATH, './/span[@dir="auto"]').text.strip()
        except:
            name = ""
        # intenta obtener numero por xpath conocido
        try:
            number = card.find_element(By.XPATH, './/div/div/div[2]/div[2]/div[2]/span[1]/span').text.strip()
        except:
            # fallback: cualquier span con signo mas y digitos
            try:
                cand = card.find_elements(By.XPATH, './/span[contains(text(), "+")]')
                for c in cand:
                    t = c.text.strip()
                    if any(ch.isdigit() for ch in t):
                        number = t
                        break
            except:
                number = ""
        # algunas tarjetas muestran numero en atributo title
        if not name:
            try:
                tspan = card.find_element(By.XPATH, './/span[@title]')
                t = tspan.get_attribute('title') or ""
                if t.startswith('+') and any(ch.isdigit() for ch in t):
                    number = t.strip()
            except:
                pass
    except:
        pass
    return clean_name(name), normalize_phone(number)

# funciones principales del scraper
def setup_driver(user_data_dir: str):
    opts = Options()
    opts.add_argument(f'--user-data-dir={user_data_dir}')
    opts.add_argument('--profile-directory=Default')
    opts.add_argument('--disable-infobars')
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument('--no-sandbox')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=opts)
    driver.maximize_window()
    return driver

def search_and_open_group(driver, group_name: str) -> bool:
    try:
        search_box = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true" and @data-tab="3"]'))
        )
        search_box.click()
        time.sleep(0.15)
        search_box.send_keys(Keys.CONTROL, 'a')
        search_box.send_keys(Keys.DELETE)
        time.sleep(0.1)
        search_box.send_keys(group_name)
        time.sleep(0.5)
        group = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//span[@title="{group_name}"]'))
        )
        group.click()
        time.sleep(1.0)
        return True
    except Exception as e:
        log_error(f"Error al buscar/abrir grupo: {e}")
        return False

def get_group_info(driver, is_cancelled: Optional[Callable[[], bool]] = None) -> List[Tuple[str, str]]:
    participants_raw: List[Tuple[str, str]] = []
    actions = ActionChains(driver)

    try:
        # abrir panel de informacion
        actions.key_down(Keys.ALT).send_keys('i').key_up(Keys.ALT).perform()
        time.sleep(1.0)

        # busca y abre modal 
        modal_button = None

        #  busca botones con aria-label que contengan miembro
        try:
            btns = driver.find_elements(By.XPATH,
                '//div[@role="button" and contains(translate(@aria-label,"ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz"), "miembro")]')
            for b in btns:
                if b.is_displayed():
                    modal_button = b
                    break
        except:
            pass

        # si no se encuentra buscar span que muestre cantidad de miembros y subir a ancestro clickable
        if not modal_button:
            try:
                spans = driver.find_elements(By.XPATH, '//span[contains(text(), "miembro") or contains(text(), "miembros")]')
                for s in spans:
                    try:
                        anc = s.find_element(By.XPATH, './ancestor::div[@role="button" or @tabindex]')
                        if anc.is_displayed():
                            modal_button = anc
                            break
                    except:
                        if s.is_displayed():
                            modal_button = s
                            break
            except:
                pass

        #  fallback a xpaths conocidos
        if not modal_button:
            fallback_xpaths = [
                '//*[@id="app"]/div[1]/div/div[3]/div/div[6]/span/div/span/div/div/div/section/div[10]/div[1]/div/div[1]/span',
                '//*[@id="app"]/div[1]/div/div[3]/div/div[6]/span/div/span/div/div/div/section/div[10]',
                '//*[@id="app"]/div[1]/div/span[2]/div/span/div/div/div'
            ]
            for xp in fallback_xpaths:
                try:
                    b = driver.find_element(By.XPATH, xp)
                    if b.is_displayed():
                        modal_button = b
                        break
                except:
                    continue

        # si se encuentra boton abrir modal con mover y hacer clic
        if modal_button:
            try:
                ActionChains(driver).move_to_element(modal_button).pause(0.12).click().perform()
            except:
                try:
                    modal_button.click()
                except:
                    pass
            time.sleep(0.9)
        else:
            # no se encontro boton fallback a extraccion desde barra lateral para grupos pequenos
            log_info("boton modal no encontrado usando fallback de barra lateral para grupos menores a 10 miembros")
            try:
                container = WebDriverWait(driver, 6).until(
                    EC.presence_of_element_located((By.XPATH, '//div[@role="list"]'))
                )
            except:
                try:
                    container = driver.find_element(By.XPATH, '//*[@id="app"]//section//div[contains(@class,"copyable-area")]')
                except Exception as e:
                    log_error(f"No se pudo localizar contenedor lateral: {e}")
                    container = None

            if container:
                items = container.find_elements(By.XPATH, './/div[@role="listitem"]')
                for item in items:
                    if is_cancelled and is_cancelled():
                        log_info("cancelado por usuario durante extraccion desde barra lateral")
                        raise RuntimeError("cancelado por usuario")
                    try:
                        name = ""
                        number = ""
                        try:
                            name = item.find_element(By.XPATH, './/span[@dir="auto"]').text.strip()
                        except:
                            name = ""
                        try:
                            num_cands = item.find_elements(By.XPATH, './/span[contains(text(), "+")]')
                            for nc in num_cands:
                                t = nc.text.strip()
                                if any(ch.isdigit() for ch in t):
                                    number = t
                                    break
                        except:
                            number = ""
                        if not name and number:
                            number_norm = normalize_phone(number)
                            name = f'Sin nombre +{number_norm[-4:] if number_norm else number[-4:]}'
                        participants_raw.append((name, number))
                    except:
                        continue
                return participants_raw

        #  aqui el modal fue abierto continua con extraccion del modal
        modal = WebDriverWait(driver, 12).until(
            EC.presence_of_element_located((By.XPATH, '//div[@role="dialog" or @role="presentation"]'))
        )

        # localiza contenedor de scroll con fallbacks
        scroll_container = None
        try:
            scroll_container = WebDriverWait(modal, 8).until(
                EC.presence_of_element_located((By.XPATH, './/div[contains(@style,"overflow") or contains(@class,"copyable-area")]'))
            )
        except:
            try:
                scroll_container = modal.find_element(By.XPATH, './/div/div/div/div[2]/div/div/div')
            except Exception as e:
                log_error(f"No pude localizar contenedor scroll: {e}")
                ActionChains(driver).send_keys(Keys.ESCAPE).perform()
                time.sleep(0.3)
                return []

        # forzar foco con tabs 
        try:
            actions.send_keys(Keys.TAB, Keys.TAB, Keys.TAB).perform()
        except:
            pass

        # scroll  para grupos grandes
        seen_keys = set()
        raw_results: List[Tuple[str, str]] = []
        step_px = 800
        max_down_attempts = 2000
        attempts = 0
        last_len = 0
        stable = 0
        stable_at_end = 0
        at_end = False

        while attempts < max_down_attempts:
            if is_cancelled and is_cancelled():
                log_info("cancelado por usuario durante barrido hacia abajo")
                raise RuntimeError("cancelado por usuario")

            # hacer scroll un paso para avanzar mas rapido
            try:
                driver.execute_script("arguments[0].scrollTop = arguments[0].scrollTop + arguments[1];", scroll_container, step_px)
            except:
                try:
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_container)
                except:
                    pass
            time.sleep(0.08)

            # intenta obtener tarjetas renderizadas con multiples selectores
            cards = modal.find_elements(By.XPATH,
                './/div[contains(@class,"x10l6tqk") and @role="listitem"] | .//div[@data-testid="cell-frame-container"] | .//div/div/div/div[2]/div/div/div/div')
            if not cards:
                cards = modal.find_elements(By.XPATH, './/div/div/div/div[2]/div/div/div/div')

            # extrae de tarjetas encontradas
            for c in cards:
                nm, ph = extract_from_card(c)
                if not nm and ph:
                    nm = f"Sin nombre +{ph[-4:]}"
                key = (ph or nm).strip()
                if not key:
                    continue
                if key not in seen_keys:
                    seen_keys.add(key)
                    raw_results.append((nm, ph))

            # control de estabilidad
            if len(raw_results) == last_len:
                stable += 1
            else:
                stable = 0
                last_len = len(raw_results)
            attempts += 1

            # verifica si llega al final del scroll
            try:
                at_end = driver.execute_script("return arguments[0].scrollTop + arguments[0].clientHeight >= arguments[0].scrollHeight - 10", scroll_container)
                if at_end:
                    stable_at_end += 1
                    # solo rompe despues de 15 iteraciones estables en el final
                    if stable_at_end >= 15:
                        log_info(f"Scroll down completado: {len(raw_results)} participantes extraídos al llegar al final")
                        break
                else:
                    stable_at_end = 0
            except:
                pass
            
            # rompe solo si no hay progreso por mucho tiempo y no esta en el final
            if stable >= 80 and not at_end:
                log_warning(f"scroll hacia abajo detenido por estabilidad sin llegar al final extraidos: {len(raw_results)}")
                # intenta forzar scroll al final 
                try:
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", scroll_container)
                    time.sleep(0.3)
                except:
                    pass
                break

        # barrido hacia arriba solo si el barrido hacia abajo llego al final
        if at_end:
            log_info(f"iniciando barrido hacia arriba participantes antes: {len(raw_results)}")
            for _ in range(80):
                if is_cancelled and is_cancelled():
                    log_info("cancelado por usuario durante barrido hacia arriba")
                    raise RuntimeError("cancelado por usuario")
                try:
                    driver.execute_script("arguments[0].scrollTop = Math.max(0, arguments[0].scrollTop - arguments[1]);", scroll_container, step_px)
                except:
                    pass
                time.sleep(0.06)
                cards = modal.find_elements(By.XPATH,
                    './/div[contains(@class,"x10l6tqk") and @role="listitem"] | .//div[@data-testid="cell-frame-container"]')
                for c in cards:
                    nm, ph = extract_from_card(c)
                    if not nm and ph:
                        nm = f"Sin nombre +{ph[-4:]}"
                    key = (ph or nm).strip()
                    if not key:
                        continue
                    if key not in seen_keys:
                        seen_keys.add(key)
                        raw_results.append((nm, ph))
            log_info(f"barrido hacia arriba completado participantes despues: {len(raw_results)}")
        else:
            log_warning("barrido hacia arriba omitido porque barrido hacia abajo no llego al final")
        # fallback por indice si faltan miembros extendido
        if len(raw_results) < 300:
            for idx in range(1, 260):
                if is_cancelled and is_cancelled():
                    log_info("cancelado por usuario durante fallback de indice")
                    raise RuntimeError("cancelado por usuario")
                try:
                    xpath_card = f'.//div/div/div/div[2]/div/div/div/div[{idx}]'
                    elems = modal.find_elements(By.XPATH, xpath_card)
                    if not elems:
                        continue
                    for c in elems:
                        nm, ph = extract_from_card(c)
                        if not nm and ph:
                            nm = f"Sin nombre +{ph[-4:]}"
                        key = (ph or nm).strip()
                        if not key:
                            continue
                        if key not in seen_keys:
                            seen_keys.add(key)
                            raw_results.append((nm, ph))
                    try:
                        driver.execute_script("arguments[0].scrollIntoView(true);", elems[-1])
                        time.sleep(0.22)
                    except:
                        pass
                except:
                    continue
        participants_raw = raw_results
    except Exception as e:
        log_error(f"Error en get_group_info: {e}")
    finally:
        try:
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.2)
            ActionChains(driver).send_keys(Keys.ESCAPE).perform()
            time.sleep(0.2)
        except:
            pass
    by_phone = {}
    by_name = {}
    for nm, ph in participants_raw:
        nm = clean_name(nm)
        phn = normalize_phone(ph)
        if phn:
            if phn not in by_phone:
                by_phone[phn] = nm
        else:
            if nm and nm not in by_name and nm not in by_phone.values():
                by_name[nm] = ""

    final: List[Tuple[str, str]] = []
    for phn, nm in by_phone.items():
        final.append((nm, phn))
    for nm in by_name.keys():
        final.append((nm, ""))

    return final

# punto de entrada principal
def scrape_group(profile_path: str, group_name: str, is_cancelled: Optional[Callable[[], bool]] = None) -> List[Tuple[str, str]]:
    # punto de entrada para la app retorna lista de tuplas (nombre, telefono)
    # is_cancelled funcion opcional que retorna verdadero si la operacion debe abortarse
    driver = None
    try:
        driver = setup_driver(profile_path)
        driver.get('https://web.whatsapp.com')
        try:
            WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true" and @data-tab="3"]')))
        except Exception:
            pass

        if not search_and_open_group(driver, group_name):
            raise RuntimeError(f"No se pudo abrir el grupo: {group_name}")
        participants = get_group_info(driver, is_cancelled=is_cancelled)
        return participants

    finally:
        try:
            if driver:
                driver.quit()
        except Exception:
            pass