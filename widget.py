from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide6.QtCore import QThread, Signal
from UI.ui_ErrorScreen import Ui_ErrorForm
from UI.ui_form import Ui_Widget
from UI.ui_ProccesScreen import Ui_ProcessForm
import os
import sys
import subprocess

from src.scripts.worker import ScraperWorker
from src.scripts import errors


CHROME_USER_DATA_DIR = r'C:\Users\emanu\AppData\Local\Google\Chrome\User Data\Profile 1'
CSV_OUTPUT_DIR = os.path.join(os.getcwd(), "output")


class ErrorScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ErrorForm()
        self.ui.setupUi(self)


class ProccesScreen(QWidget):
    completed = Signal(list)  # emite lista de tuplas (nombre, telefono) cuando termina
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProcessForm()
        self.ui.setupUi(self)
        self.ui.btn_aceptar.clicked.connect(self.on_aceptar_clicked)

        self.thread = None
        self.worker = None
        self.profile_path = None
        self.group_name = None
        self.scraping_started = False

    def prepare_scrape(self, profile_path: str, group_name: str):
        # guardar parametros para iniciar cuando se presione aceptar
        self.profile_path = profile_path
        self.group_name = group_name
        self.set_status(f"grupo: {group_name}\npresiona aceptar para iniciar extraccion")

    def on_aceptar_clicked(self):
        # si ya termino el scraping cierra ventana
        if self.scraping_started and self.thread is None:
            self.close()
            return
        
        # si no ha iniciado comienzael scraping
        if not self.scraping_started and self.profile_path and self.group_name:
            self.scraping_started = True
            self.start_scrape()
        
    def start_scrape(self):
        self.thread = QThread()
        self.worker = ScraperWorker(self.profile_path, self.group_name)
        self.worker.moveToThread(self.thread)

        # conecta señales
        self.worker.started.connect(lambda: self.set_status("iniciando..."))
        self.worker.progress.connect(self.on_progress)
        self.worker.finished.connect(self.on_finished)
        self.worker.error.connect(self.on_error)

        self.thread.started.connect(self.worker.run)

        # conexiones de limpieza
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)

        self.worker.error.connect(self.thread.quit)
        self.worker.error.connect(self.worker.deleteLater)

        self.thread.start()

    def set_status(self, msg: str):
        self.ui.label_warning.setText(msg)

    def on_progress(self, pct: int, msg: str):
        self.set_status(msg)

    def on_finished(self, rows):
        self.set_status(f"completado: {len(rows)} participantes")
        self.completed.emit(rows)
        # la ventana permanece abierta hasta que el usuario haga clic en aceptar
        self.ui.label_warning.setText(f"extraccion finalizada: {len(rows)} participantes\npuedes descargar desde ventana principal")

    def on_error(self, msg: str):
        errors.log_error(msg)
        self.set_status("error during extraction")
        QMessageBox.critical(self, "scraping error", str(msg))


class Widget(QWidget, Ui_Widget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self._last_rows = []
        self._last_group_name = ""

        # botones principales
        self.ui.btnreiniciar.clicked.connect(self.reiniciar_programa)
        self.ui.btnsalir.clicked.connect(self.close)
        self.ui.btnextraer.clicked.connect(self.on_click_extraer)
        self.ui.btndescargar.clicked.connect(self.on_click_descargar)

    def reiniciar_programa(self):
        python = sys.executable
        script = os.path.abspath(sys.argv[0])
        subprocess.Popen([python, script])
        QApplication.quit()

    def on_click_extraer(self):
        profile = CHROME_USER_DATA_DIR
        try:
            group_name = self.ui.textEdit_2.toPlainText().strip()
        except Exception:
            group_name = self.ui.lineEdit.text().strip() if hasattr(self.ui, "lineEdit") else ""
        errors.log_info(f"group entered: '{group_name}'")

        if not group_name:
            QMessageBox.warning(self, "missing group name", "enter the name of the group to extract")
            return

        self._last_group_name = group_name

        self.process_window = ProccesScreen()
        self.process_window.completed.connect(self.on_extraction_completed)
        self.process_window.prepare_scrape(profile, group_name)
        self.process_window.show()

    def on_extraction_completed(self, rows):
        # guarda en memoria y actualizar contador en ui
        self._last_rows = rows or []
        try:
            self.ui.label_5.setText(str(len(self._last_rows)))
        except Exception:
            pass

    def on_click_descargar(self):
        if not self._last_rows:
            QMessageBox.information(self, "sin datos", "no hay datos para descargar ejecuta extraccion primero")
            return
        
        # obtiene numero de telefono y nomenclatura
        try:
            phone = self.ui.textEdit.toPlainText().strip() if hasattr(self.ui, "textEdit") else ""
        except Exception:
            phone = ""
        
        try:
            nomen = self.ui.textEdit_3.toPlainText().strip() if hasattr(self.ui, "textEdit_3") else ""
        except Exception:
            nomen = ""
        
        # construye nombre de archivo, telefono nomenclatura o usar grupo si faltan datos
        from src.scripts.save_data import save_to_csv
        if phone and nomen:
            filename_key = f"{phone} {nomen}"
        elif nomen:
            filename_key = nomen
        else:
            filename_key = self._last_group_name
        
        path = save_to_csv(self._last_rows, filename_key)
        if path:
            QMessageBox.information(self, "descarga lista", f"archivo guardado en:\n{path}")
        else:
            QMessageBox.critical(self, "error al guardar", "no se pudo guardar el archivo csv")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
