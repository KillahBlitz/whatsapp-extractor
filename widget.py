from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from ui_ErrorScreen import Ui_Form
from ui_form import Ui_Widget

import sys


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

class ErrorScreen(QWidget, Ui_Form):
    def __init__(self):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.setupUi(self)
        self.btnreiniciar.clicked.connect(self.close)
        

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.btnreiniciar.clicked.connect(self.errorscreen)

        self.error_screen =  ErrorScreen()

    def errorscreen(self):
        self.error_screen.show()
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
