# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProccesScreen.ui'
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
        Form.resize(380, 167)
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
        self.label_warning = QLabel(Form)
        self.label_warning.setObjectName(u"label_warning")
        self.label_warning.setGeometry(QRect(30, 70, 321, 31))
        font = QFont()
        font.setFamilies([u"SansSerif"])
        self.label_warning.setFont(font)
        self.btn_aceptar = QPushButton(Form)
        self.btn_aceptar.setObjectName(u"btn_aceptar")
        self.btn_aceptar.setGeometry(QRect(140, 110, 91, 31))
        self.btn_aceptar.setFont(font)
        self.label_title_procces = QLabel(Form)
        self.label_title_procces.setObjectName(u"label_title_procces")
        self.label_title_procces.setGeometry(QRect(70, 40, 251, 31))
        palette = QPalette()
        brush = QBrush(QColor(36, 212, 103, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.WindowText, brush)
        self.label_title_procces.setPalette(palette)
        font1 = QFont()
        font1.setFamilies([u"SansSerif"])
        font1.setPointSize(18)
        font1.setBold(True)
        self.label_title_procces.setFont(font1)
        self.label_title_procces.setMouseTracking(False)
        self.label_title_procces.setTabletTracking(False)
        self.label_title_procces.setAcceptDrops(False)
        self.label_title_procces.setStyleSheet(u"QLabel{rgb(228, 23, 26)}")
        self.label_title_procces.setOpenExternalLinks(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_warning.setText(QCoreApplication.translate("Form", u"                                              -", None))
        self.btn_aceptar.setText(QCoreApplication.translate("Form", u"Aceptar", None))
        self.label_title_procces.setText(QCoreApplication.translate("Form", u"PROCESO INICIADO.", None))
    # retranslateUi

