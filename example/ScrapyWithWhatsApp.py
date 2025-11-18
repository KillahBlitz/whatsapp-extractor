from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

import time
import re

# Ruta al chromedriver (ajusta si estás en Windows)
PROFILE_PATH = r"C:\Users\fach7\AppData\Local\Google\Chrome\User Data\Profile1"  # Corregir esto


# Configuración para guardar sesión (evita escanear QR cada vez)
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
options.add_argument(f"--user-data-dir={PROFILE_PATH}")
options.add_argument("--start-maximized")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
options.add_argument('--remote-debugging-port=9222')


# Iniciar navegador
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1. Ir a WhatsApp Web
driver.get("https://web.whatsapp.com")

print("🔄 Esperando que escanees el código QR (solo si es la primera vez).")
print("✅ Cuando termines de escanear y esté todo cargado, presiona ENTER para continuar.")
time.sleep(10)  # Espera inicial para cargar la página
input("Presiona ENTER para continuar...")


# 2. Intenta expandir "Archivados" si está minimizado
try:
    archivados = driver.find_element(By.XPATH, '//button[@aria-label="Archivados "]')
    archivados.click()
    print("📁 Se accedió a la sección de Archivados.")
    time.sleep(2)
    print("🔄 Esperando que se cargue la lista de chats archivados...")
    time.sleep(3)
except:
    print("⚠️ Ya estás dentro de 'Archivados' o no se encontró la opción.")



# 3. Buscar y hacer clic en el grupo
# Intenta localizarlo con scroll y verificación por title

# 3. Buscar y hacer clic en el grupo dentro de Archivados

# Espera a que aparezcan los elementos individuales de chat archivado
try:
    chat_items = WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.XPATH, '//div[@role="listitem"]'))
    )
    print(f"✅ Se detectaron {len(chat_items)} elementos en la sección de Archivados.")
except:
    print("❌ No se encontraron chats archivados.")
    driver.quit()
    exit()

# Nombre del grupo a buscar (ajústalo según tu grupo)
grupo_nombre = "Brazos de 35"
grupo_encontrado = False
intentos = 0
max_scrolls = 300

print("🔍 Buscando el grupo dentro de archivados...")

while not grupo_encontrado and intentos < max_scrolls:
    spans = driver.find_elements(By.XPATH, '//div[@role="listitem"]//span[@title]')
    print(f"🔎 Se detectaron {len(spans)} elementos con título.")

    for span in spans:
        try:
            titulo = span.get_attribute("title")
            print(f"🔍 Revisando: {titulo}")
            if grupo_nombre.lower() in titulo.lower():
                driver.execute_script("arguments[0].scrollIntoView();", span)
                time.sleep(1)
                span.click()
                grupo_encontrado = True
                print(f"✅ Se accedió al grupo: {titulo}")
                time.sleep(2)
                break
        except Exception as e:
            print(f"⚠️ Error al procesar elemento: {e}")
            continue

    if not grupo_encontrado:
        print("↪️ Scroll abajo para cargar más chats archivados...")
        driver.execute_script("arguments[0].scrollTop += 300", chat_items)
        time.sleep(2)
        intentos += 1

if not grupo_encontrado:
    print(f"❌ No se encontró el grupo '{grupo_nombre}' después de {max_scrolls} scrolls.")



# 4. Hacer clic en la imagen del encabezado del grupo para abrir la info
try:
    imagen_xpath = '//*[@id="main"]/header/div[1]/div/img'
    
    imagen = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, imagen_xpath))
    )

    # Scroll por si acaso está fuera de vista
    driver.execute_script("arguments[0].scrollIntoView(true);", imagen)
    time.sleep(1)

    # Hacer clic en la imagen
    imagen.click()
    print("🖼️ Se hizo clic en la imagen del encabezado. Info del grupo abierta.")
    time.sleep(2)

except Exception as e:
    print(f"❌ No se pudo hacer clic en la imagen: {e}")
    driver.quit()
    exit()


# 5b. Hacer clic en "Ver todos (X más)" para expandir todos los miembros
try:
    ver_todos_xpath = '//*[@id="app"]/div/div[3]/div/div[5]/span/div/span/div/div/div/section/div[10]/div[2]/div[2]/div'
    boton_ver_todos = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, ver_todos_xpath))
    )
    boton_ver_todos.click()
    print("🔽 Se expandió la lista completa de miembros con 'Ver todos'.")
    # — 5c) Scroll JS hasta que deje de cargar más filas —
    lista = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,
            "//div[contains(@aria-label, 'Lista de miembros')]"
        ))
    )

    prev = 0
    while True:
        # subimos hasta el final
        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight;", lista)
        time.sleep(0.5)
        rows = lista.find_elements(By.XPATH, ".//div[@role='listitem']")
        if len(rows) == prev:
            break
        prev = len(rows)
    print(f"🔽 Se cargaron {len(rows)} filas de miembros")
    time.sleep(2)
except Exception as e:
    print(f"❌ No se pudo hacer clic en 'Ver todos': {e}")
    driver.quit()
    exit()





#  — tras clicar el “Ver todos” y localizar: —
lista = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//div[contains(@aria-label,'Lista de miembros')]"))
)

phone_re = re.compile(r'^\+\d+')      # sólo cadenas que empiecen con ‘+’ y luego dígitos
numeros = set()
seen_scrolls = set()

while True:
    # 1) Extraigo todos los spans de número que haya ahora mismo en DOM:
    filas = lista.find_elements(By.XPATH, ".//div[@role='listitem']")
    for row in filas:
        try:
            elm = row.find_element(
                By.XPATH,
                ".//span[normalize-space(text()) and starts-with(normalize-space(.), '+')]"
            )
            txt = elm.text.strip()
            if phone_re.match(txt):
                numeros.add(txt)
        except:
            pass

    # 2) Compruebo dónde estoy:
    scrollTop = driver.execute_script("return arguments[0].scrollTop;", lista)
    scrollHeight = driver.execute_script("return arguments[0].scrollHeight;", lista)
    clientHeight = driver.execute_script("return arguments[0].clientHeight;", lista)

    # Si ya lo vimos o hemos llegado al final, rompemos:
    if scrollTop in seen_scrolls or scrollTop + clientHeight >= scrollHeight:
        break
    seen_scrolls.add(scrollTop)

    # 3) Scroll un pasito:
    driver.execute_script("arguments[0].scrollTop += arguments[0].clientHeight;", lista)
    time.sleep(0.3)

print(f"✅ Total números extraídos: {len(numeros)}")
for n in sorted(numeros):
    print(n)