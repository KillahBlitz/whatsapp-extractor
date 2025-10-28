from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from UI.ui_ErrorScreen import Ui_ErrorForm
from UI.ui_form import Ui_Widget
from UI.ui_ProccesScreen import Ui_ProcessForm
import os
import sys
import subprocess


class ErrorScreen(QWidget, Ui_ErrorForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ErrorForm()  # Usar la UI específica para error
        self.setupUi(self)

class ProccesScreen(QWidget, Ui_ProcessForm):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ProcessForm()  # Usar la UI específica para proceso
        self.setupUi(self)
        # La ventana de error está configurada - no hay botones para conectar por ahora

        

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #al presionar el boton reiniciar se abre la ventana de error
        self.ui.btnreiniciar.clicked.connect(self.reiniciar_programa)
        self.ui.btnsalir.clicked.connect(self.close)
        self.ui.btnextraer.clicked.connect(self.show_process_screen)
        
    def show_error_screen(self):
        self.error_window = ErrorScreen()
        self.error_window.show()

    def show_process_screen(self):
        self.process_window = ProccesScreen()
        self.process_window.show()

    def reiniciar_programa(self):
        python = sys.executable 
        script = os.path.abspath(sys.argv[0]) 
        subprocess.Popen([python, script]) 
        QApplication.quit() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

#Prueba para subir mis cambios