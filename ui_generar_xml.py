# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\DELL\Documents\IPC2_Proyecto1_201445840\generar_xml.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 300)
        MainWindow.setMinimumSize(QtCore.QSize(800, 300))
        MainWindow.setMaximumSize(QtCore.QSize(800, 300))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(800, 300))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 800, 400))
        self.frame.setMinimumSize(QtCore.QSize(800, 400))
        self.frame.setMaximumSize(QtCore.QSize(800, 300))
        self.frame.setStyleSheet("QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel{\n"
"color: rgb(18, 82, 200);\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QLabel:hover{\n"
"color: white;\n"
"\n"
"\n"
"font: 75 12pt \"Arial Black\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}\n"
"\n"
"QTextEdit{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"font: 75 12pt \"Arial\";\n"
"    \n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.bt_regresar = QtWidgets.QPushButton(self.frame)
        self.bt_regresar.setGeometry(QtCore.QRect(630, 190, 141, 40))
        self.bt_regresar.setMinimumSize(QtCore.QSize(100, 40))
        self.bt_regresar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto1_201445840\\pngfind.com-back-png-1934895.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_regresar.setIcon(icon)
        self.bt_regresar.setIconSize(QtCore.QSize(32, 32))
        self.bt_regresar.setObjectName("bt_regresar")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(30, 0, 400, 35))
        self.label_8.setMinimumSize(QtCore.QSize(400, 35))
        self.label_8.setMaximumSize(QtCore.QSize(200, 30))
        self.label_8.setObjectName("label_8")
        self.lineEditpaciente = QtWidgets.QLineEdit(self.frame)
        self.lineEditpaciente.setGeometry(QtCore.QRect(230, 130, 231, 20))
        self.lineEditpaciente.setObjectName("lineEditpaciente")
        self.btnmostrar = QtWidgets.QPushButton(self.frame)
        self.btnmostrar.setGeometry(QtCore.QRect(650, 70, 81, 31))
        self.btnmostrar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        self.btnmostrar.setObjectName("btnmostrar")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(30, 120, 200, 35))
        self.label_9.setMinimumSize(QtCore.QSize(200, 35))
        self.label_9.setMaximumSize(QtCore.QSize(200, 30))
        self.label_9.setObjectName("label_9")
        self.textEditpaciente = QtWidgets.QTextEdit(self.frame)
        self.textEditpaciente.setGeometry(QtCore.QRect(30, 40, 591, 71))
        self.textEditpaciente.setObjectName("textEditpaciente")
        self.btngenerar = QtWidgets.QPushButton(self.frame)
        self.btngenerar.setGeometry(QtCore.QRect(50, 180, 141, 40))
        self.btngenerar.setMinimumSize(QtCore.QSize(100, 40))
        self.btngenerar.setStyleSheet("QPushButton{\n"
"background-color: rgb(18, 82, 200);\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: white;\n"
"border-top-left-radius: 20px;\n"
"border-bottom-left-radius: 20px;\n"
"\n"
"font: 75 11pt \"Arial Black\";\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("c:\\Users\\DELL\\Documents\\IPC2_Proyecto1_201445840\\escritura.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btngenerar.setIcon(icon1)
        self.btngenerar.setIconSize(QtCore.QSize(32, 32))
        self.btngenerar.setObjectName("btngenerar")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Editar_curso"))
        self.bt_regresar.setText(_translate("MainWindow", "Regresar"))
        self.label_8.setText(_translate("MainWindow", "Mostrar pacientes"))
        self.btnmostrar.setText(_translate("MainWindow", "Mostrar"))
        self.label_9.setText(_translate("MainWindow", "ingrese el paciente"))
        self.textEditpaciente.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:12pt; font-weight:72; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.btngenerar.setText(_translate("MainWindow", "Generar"))
