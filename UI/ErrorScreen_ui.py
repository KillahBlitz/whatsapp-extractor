# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ErrorScreen.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(379, 166)
        palette = QPalette()
        Form.setPalette(palette)
        Form.setMouseTracking(False)
        Form.setTabletTracking(False)
        Form.setStyleSheet(u"QPushButton {\n"
"	background-color:  black;\n"
"    border-radius: 12px;  \n"
"}\n"
"\n"
"\n"
"QPushButton#btn_aceptar:hover {\n"
"    border: 2px solid white;\n"
"    box-shadow: 0 0 10px white;\n"
"}")
        self.label_title_error = QLabel(Form)
        self.label_title_error.setObjectName(u"label_title_error")
        self.label_title_error.setGeometry(QRect(140, 40, 91, 31))
        palette1 = QPalette()
        brush = QBrush(QColor(170, 0, 0, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.BrushStyle.SolidPattern)
        palette1.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Text, brush1)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        palette1.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Text, brush1)
        self.label_title_error.setPalette(palette1)
        font = QFont()
        font.setFamilies([u"SansSerif"])
        font.setPointSize(18)
        font.setBold(True)
        self.label_title_error.setFont(font)
        self.label_title_error.setMouseTracking(False)
        self.label_title_error.setTabletTracking(False)
        self.label_title_error.setAcceptDrops(False)
        self.label_title_error.setStyleSheet(u"QLabel{rgb(228, 23, 26)}")
        self.label_title_error.setOpenExternalLinks(False)
        self.label_error = QLabel(Form)
        self.label_error.setObjectName(u"label_error")
        self.label_error.setGeometry(QRect(30, 70, 321, 31))
        font1 = QFont()
        font1.setFamilies([u"SansSerif"])
        self.label_error.setFont(font1)
        self.btn_aceptar = QPushButton(Form)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(140, 110, 91, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush1)
        palette2.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush1)
        self.btn_aceptar.setPalette(palette2)
        self.btn_aceptar.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_title_error.setText(QCoreApplication.translate("Form", u"ERROR.", None))
        self.label_error.setText(QCoreApplication.translate("Form", u"                                              -", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Form", u"Aceptar", None))
    # retranslateUi

