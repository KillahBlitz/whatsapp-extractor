# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.setEnabled(True)
        Widget.resize(446, 617)
        Widget.setStyleSheet(u"QPushButton {\n"
"    border-radius: 12px; \n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton#btnextraer:hover {\n"
"    border: 2px solid white;\n"
"    box-shadow: 0 0 10px white;\n"
"}\n"
"\n"
"\n"
"QPushButton#btnsalir:hover {\n"
"    border: 2px solid white;\n"
"    box-shadow: 0 0 10px white;\n"
"}\n"
"\n"
"\n"
"QPushButton#btndescargar:hover {\n"
"    background-color: black;\n"
"}\n"
"\n"
"\n"
"QPushButton#btnreiniciar:hover {\n"
"    background-color: black;\n"
"}")
        self.label_telefono = QLabel(Widget)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setGeometry(QRect(20, 100, 131, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_telefono.setFont(font)
        self.label_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_caracteres = QLabel(Widget)
        self.label_caracteres.setObjectName(u"label_caracteres")
        self.label_caracteres.setGeometry(QRect(150, 100, 91, 21))
        self.label_caracteres.setFont(font)
        self.label_caracteres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(20, 130, 401, 31))
        self.textEdit_2 = QTextEdit(Widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(20, 210, 401, 31))
        self.label_grupo = QLabel(Widget)
        self.label_grupo.setObjectName(u"label_grupo")
        self.label_grupo.setGeometry(QRect(20, 180, 131, 21))
        self.label_grupo.setFont(font)
        self.label_grupo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_3 = QTextEdit(Widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(20, 290, 401, 31))
        self.label_nomen = QLabel(Widget)
        self.label_nomen.setObjectName(u"label_nomen")
        self.label_nomen.setGeometry(QRect(20, 260, 101, 21))
        self.label_nomen.setFont(font)
        self.label_nomen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_registrar = QLabel(Widget)
        self.label_registrar.setObjectName(u"label_registrar")
        self.label_registrar.setGeometry(QRect(120, 260, 91, 21))
        self.label_registrar.setFont(font)
        self.label_registrar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_telrec = QLabel(Widget)
        self.label_telrec.setObjectName(u"label_telrec")
        self.label_telrec.setGeometry(QRect(20, 340, 191, 21))
        self.label_telrec.setFont(font)
        self.label_telrec.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 379, 161, 21))
        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(250, 360, 161, 71))
        self.btnextraer = QPushButton(Widget)
        self.btnextraer.setObjectName(u"btnextraer")
        self.btnextraer.setGeometry(QRect(30, 440, 161, 61))
        palette = QPalette()
        brush = QBrush(QColor(36, 212, 103, 255))
        brush.setStyle(Qt.BrushStyle.SolidPattern)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Active, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Inactive, QPalette.ColorRole.Window, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Button, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Base, brush)
        palette.setBrush(QPalette.ColorGroup.Disabled, QPalette.ColorRole.Window, brush)
        self.btnextraer.setPalette(palette)
        self.btnextraer.setStyleSheet(u"QPushButton {\n"
"    background-color: #24d467;\n"
"}\n"
"")
        self.btndescargar = QPushButton(Widget)
        self.btndescargar.setObjectName(u"btndescargar")
        self.btndescargar.setGeometry(QRect(250, 440, 171, 61))
        self.btnreiniciar = QPushButton(Widget)
        self.btnreiniciar.setObjectName(u"btnreiniciar")
        self.btnreiniciar.setGeometry(QRect(30, 530, 161, 61))
        palette1 = QPalette()
        self.btnreiniciar.setPalette(palette1)
        self.btnsalir = QPushButton(Widget)
        self.btnsalir.setObjectName(u"btnsalir")
        self.btnsalir.setGeometry(QRect(250, 530, 171, 61))
        self.btnsalir.setStyleSheet(u"QPushButton {\n"
"    background-color: #e3171a;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(Widget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(80, 30, 267, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_titulo = QLabel(self.horizontalLayoutWidget)
        self.label_titulo.setObjectName(u"label_titulo")
        font1 = QFont()
        font1.setPointSize(20)
        self.label_titulo.setFont(font1)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_titulo)

        self.label_titulo_2 = QLabel(self.horizontalLayoutWidget)
        self.label_titulo_2.setObjectName(u"label_titulo_2")
        self.label_titulo_2.setFont(font1)
        self.label_titulo_2.setStyleSheet(u"color: #24d467")
        self.label_titulo_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_titulo_2)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_telefono.setText(QCoreApplication.translate("Widget", u"N\u00famero de telefono:", None))
        self.label_caracteres.setText(QCoreApplication.translate("Widget", u"(10 caracteres)", None))
        self.label_grupo.setText(QCoreApplication.translate("Widget", u"Nombre del Grupo", None))
        self.label_nomen.setText(QCoreApplication.translate("Widget", u"Nomenclatura:", None))
        self.label_registrar.setText(QCoreApplication.translate("Widget", u"(Para registrar)", None))
        self.label_telrec.setText(QCoreApplication.translate("Widget", u"No. de telefonos recuperados", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"-", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"\u00bfEl grupo est\u00e1 archivado? ", None))
        self.btnextraer.setText(QCoreApplication.translate("Widget", u"Extraer", None))
        self.btndescargar.setText(QCoreApplication.translate("Widget", u"Descargar", None))
        self.btnreiniciar.setText(QCoreApplication.translate("Widget", u"Reiniciar", None))
        self.btnsalir.setText(QCoreApplication.translate("Widget", u"Salir", None))
        self.label_titulo.setText(QCoreApplication.translate("Widget", u"ExtContact ", None))
        self.label_titulo_2.setText(QCoreApplication.translate("Widget", u"WhatsApp", None))
    # retranslateUi

