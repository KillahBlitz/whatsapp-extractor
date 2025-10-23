# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'formZgAWDq.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(460, 572)
        Widget.setStyleSheet(u"QMainWindow {\n"
"    background-color: #000000;\n"
"    color: #000000;\n"
"    font-family: \"Inter Regular\", \"Roboto\", \"Arial\";\n"
"    font-size: 12pt;\n"
"}\n"
"\n"
"/* --- Botones --- */\n"
"QPushButton {\n"
"    background-color: #151515;\n"
"    color: #FFFFFF;\n"
"    border: 2px solid #444444;\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    border-color: #00E5FF;\n"
"    color: #00E5FF;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #202020;\n"
"}")
        self.label_titulo = QLabel(Widget)
        self.label_titulo.setObjectName(u"label_titulo")
        self.label_titulo.setGeometry(QRect(90, 10, 271, 41))
        font = QFont()
        font.setPointSize(20)
        self.label_titulo.setFont(font)
        self.label_titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_telefono = QLabel(Widget)
        self.label_telefono.setObjectName(u"label_telefono")
        self.label_telefono.setGeometry(QRect(30, 60, 131, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.label_telefono.setFont(font1)
        self.label_telefono.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_caracteres = QLabel(Widget)
        self.label_caracteres.setObjectName(u"label_caracteres")
        self.label_caracteres.setGeometry(QRect(160, 60, 91, 21))
        self.label_caracteres.setFont(font1)
        self.label_caracteres.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit = QTextEdit(Widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 90, 401, 31))
        self.textEdit_2 = QTextEdit(Widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(30, 170, 401, 31))
        self.label_grupo = QLabel(Widget)
        self.label_grupo.setObjectName(u"label_grupo")
        self.label_grupo.setGeometry(QRect(30, 140, 131, 21))
        self.label_grupo.setFont(font1)
        self.label_grupo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textEdit_3 = QTextEdit(Widget)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(30, 250, 401, 31))
        self.label_nomen = QLabel(Widget)
        self.label_nomen.setObjectName(u"label_nomen")
        self.label_nomen.setGeometry(QRect(30, 220, 101, 21))
        self.label_nomen.setFont(font1)
        self.label_nomen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_registrar = QLabel(Widget)
        self.label_registrar.setObjectName(u"label_registrar")
        self.label_registrar.setGeometry(QRect(130, 220, 91, 21))
        self.label_registrar.setFont(font1)
        self.label_registrar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_telrec = QLabel(Widget)
        self.label_telrec.setObjectName(u"label_telrec")
        self.label_telrec.setGeometry(QRect(30, 300, 191, 21))
        self.label_telrec.setFont(font1)
        self.label_telrec.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 339, 161, 21))
        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(260, 320, 161, 71))
        self.btnextraer = QPushButton(Widget)
        self.btnextraer.setObjectName(u"btnextraer")
        self.btnextraer.setGeometry(QRect(40, 400, 161, 61))
        self.btndescargar = QPushButton(Widget)
        self.btndescargar.setObjectName(u"btndescargar")
        self.btndescargar.setGeometry(QRect(250, 400, 171, 61))
        self.btnreiniciar = QPushButton(Widget)
        self.btnreiniciar.setObjectName(u"btnreiniciar")
        self.btnreiniciar.setGeometry(QRect(40, 470, 161, 61))
        self.btnsalir = QPushButton(Widget)
        self.btnsalir.setObjectName(u"btnsalir")
        self.btnsalir.setGeometry(QRect(250, 470, 171, 61))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_titulo.setText(QCoreApplication.translate("Widget", u"ExtContact WhatsApp", None))
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
    # retranslateUi

