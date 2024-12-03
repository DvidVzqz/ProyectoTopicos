# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crud_lab.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_crud_lab(object):
    def setupUi(self, crud_lab):
        crud_lab.setObjectName("crud_lab")
        crud_lab.resize(1080, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(crud_lab.sizePolicy().hasHeightForWidth())
        crud_lab.setSizePolicy(sizePolicy)
        crud_lab.setMinimumSize(QtCore.QSize(1080, 700))
        crud_lab.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(crud_lab)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo_crud_lab = QtWidgets.QLabel(self.centralwidget)
        self.titulo_crud_lab.setGeometry(QtCore.QRect(0, 50, 1081, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG Inline")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titulo_crud_lab.setFont(font)
        self.titulo_crud_lab.setStyleSheet("font-family: Decotura ICG Inline;\n"
"font-size: 50pt;")
        self.titulo_crud_lab.setTextFormat(QtCore.Qt.PlainText)
        self.titulo_crud_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_crud_lab.setObjectName("titulo_crud_lab")
        self.tabla_lab = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_lab.setGeometry(QtCore.QRect(50, 140, 981, 192))
        self.tabla_lab.setObjectName("tabla_lab")
        self.tabla_lab.setColumnCount(0)
        self.tabla_lab.setRowCount(0)
        self.introducir_email2 = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_email2.setGeometry(QtCore.QRect(60, 570, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.introducir_email2.setFont(font)
        self.introducir_email2.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"border-radius: 20px;\n"
"border: 3px solid #c0c0c0;\n"
"padding: 5px;")
        self.introducir_email2.setObjectName("introducir_email2")
        self.introducir_ap4 = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_ap4.setGeometry(QtCore.QRect(390, 490, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.introducir_ap4.setFont(font)
        self.introducir_ap4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"border-radius: 20px;\n"
"border: 3px solid #c0c0c0;\n"
"padding: 5px;")
        self.introducir_ap4.setObjectName("introducir_ap4")
        self.boton_salir7 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir7.setGeometry(QtCore.QRect(920, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_salir7.setFont(font)
        self.boton_salir7.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 30pt;\n"
"background-color: #ff0000;\n"
"border-radius: 20px;\n"
"color: white;")
        self.boton_salir7.setObjectName("boton_salir7")
        self.boton_actualizar4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_actualizar4.setGeometry(QtCore.QRect(390, 350, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.boton_actualizar4.setFont(font)
        self.boton_actualizar4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"background-color: #00aaff;\n"
"border-radius: 20px;\n"
"color: white;")
        self.boton_actualizar4.setObjectName("boton_actualizar4")
        self.boton_eliminar4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_eliminar4.setGeometry(QtCore.QRect(720, 350, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.boton_eliminar4.setFont(font)
        self.boton_eliminar4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"background-color: #ff0000;\n"
"border-radius: 20px;\n"
"color: white;")
        self.boton_eliminar4.setObjectName("boton_eliminar4")
        self.introducir_nom4 = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_nom4.setGeometry(QtCore.QRect(60, 490, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.introducir_nom4.setFont(font)
        self.introducir_nom4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"border-radius: 20px;\n"
"border: 3px solid #c0c0c0;\n"
"padding: 5px;")
        self.introducir_nom4.setObjectName("introducir_nom4")
        self.titulo_intro_datos = QtWidgets.QLabel(self.centralwidget)
        self.titulo_intro_datos.setGeometry(QtCore.QRect(0, 430, 1081, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo_intro_datos.sizePolicy().hasHeightForWidth())
        self.titulo_intro_datos.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.titulo_intro_datos.setFont(font)
        self.titulo_intro_datos.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;")
        self.titulo_intro_datos.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_intro_datos.setObjectName("titulo_intro_datos")
        self.boton_agregar4 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregar4.setGeometry(QtCore.QRect(60, 350, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.boton_agregar4.setFont(font)
        self.boton_agregar4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"background-color: #00ff00;\n"
"border-radius: 20px;\n"
"color: white;")
        self.boton_agregar4.setObjectName("boton_agregar4")
        self.introducir_tel4 = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_tel4.setGeometry(QtCore.QRect(720, 490, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(20)
        self.introducir_tel4.setFont(font)
        self.introducir_tel4.setStyleSheet("font-family: Decotura ICG;\n"
"font-size: 20pt;\n"
"border-radius: 20px;\n"
"border: 3px solid #c0c0c0;\n"
"padding: 5px;")
        self.introducir_tel4.setObjectName("introducir_tel4")
        crud_lab.setCentralWidget(self.centralwidget)

        self.retranslateUi(crud_lab)
        QtCore.QMetaObject.connectSlotsByName(crud_lab)

    def retranslateUi(self, crud_lab):
        _translate = QtCore.QCoreApplication.translate
        crud_lab.setWindowTitle(_translate("crud_lab", "MainWindow"))
        self.titulo_crud_lab.setText(_translate("crud_lab", "Datos de laboratorista"))
        self.introducir_email2.setPlaceholderText(_translate("crud_lab", "email"))
        self.introducir_ap4.setPlaceholderText(_translate("crud_lab", "apellido"))
        self.boton_salir7.setText(_translate("crud_lab", "Salir"))
        self.boton_actualizar4.setText(_translate("crud_lab", "Actualizar"))
        self.boton_eliminar4.setText(_translate("crud_lab", "Eliminar"))
        self.introducir_nom4.setPlaceholderText(_translate("crud_lab", "nombre"))
        self.titulo_intro_datos.setText(_translate("crud_lab", "Introducir datos"))
        self.boton_agregar4.setText(_translate("crud_lab", "Agregar"))
        self.introducir_tel4.setPlaceholderText(_translate("crud_lab", "teléfono"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    crud_lab = QtWidgets.QMainWindow()
    ui = Ui_crud_lab()
    ui.setupUi(crud_lab)
    crud_lab.show()
    sys.exit(app.exec_())