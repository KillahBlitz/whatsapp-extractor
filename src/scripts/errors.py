import logging
import traceback
from datetime import datetime
import os

# configuracion de logging:
# consola: nivel info y superior
# archivo: nivel error y superior, se crea solo al primer error

_LOG_DIR = 'logs'
_LOG_FILE = None
_FILE_HANDLER_ATTACHED = False

_console_handler = logging.StreamHandler()
_console_handler.setLevel(logging.INFO)
_console_handler.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))

logging.basicConfig(level=logging.INFO, handlers=[_console_handler])

def _ensure_file_handler():
    global _FILE_HANDLER_ATTACHED, _LOG_FILE
    if _FILE_HANDLER_ATTACHED:
        return
    try:
        os.makedirs(_LOG_DIR, exist_ok=True)
        _LOG_FILE = os.path.join(_LOG_DIR, f'whatsapp_scraper_{datetime.now().strftime("%Y%m%d")}.log')
        fh = logging.FileHandler(_LOG_FILE, encoding='utf-8')
        fh.setLevel(logging.ERROR)
        fh.setFormatter(logging.Formatter('%(asctime)s [%(levelname)s] %(message)s'))
        logging.getLogger().addHandler(fh)
        _FILE_HANDLER_ATTACHED = True
    except Exception:
        # si no se puede crear el archivo, continua solo con consola
        pass

def log_info(message: str) -> None:
    logging.info(message)

def log_success(message: str) -> None:
    logging.info(f" {message}")

def log_warning(message: str) -> None:
    logging.warning(f" {message}")

def log_error(message: str) -> None:
    _ensure_file_handler()
    logging.error(f" {message}")

def handle_exception(exc: Exception, context: str = None) -> None:
    # registra excepcion completa con contexto
    ctx = f' en {context}' if context else ''
    _ensure_file_handler()
    logging.error(f"Excepción{ctx}: {str(exc)}")
    logging.debug(traceback.format_exc())

def safe_quit(driver) -> None:
    # cierra el webdriver de forma segura si existe
    try:
        if driver:
            driver.quit()
            log_info("WebDriver cerrado correctamente")
    except Exception as e:
        logging.error(f"Error cerrando WebDriver: {e}")
