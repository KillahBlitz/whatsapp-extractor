from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from ui_ErrorScreen import Ui_Form
from ui_form import Ui_Widget
import sys


class ErrorScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # La ventana de error está configurada - no hay botones para conectar por ahora

        

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        #al presionar el boton reiniciar se abre la ventana de error
        self.ui.btnreiniciar.clicked.connect(self.show_error_screen)
        
    def show_error_screen(self):
        """Método para mostrar la pantalla de error"""
        self.error_window = ErrorScreen()
        self.error_window.show()

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
