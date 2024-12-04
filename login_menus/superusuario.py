from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import iniciosesion

class Ui_superusuario(object):
    def setupUi(self, superusuario):
        superusuario.setObjectName("superusuario")
        superusuario.resize(1080, 700)
        superusuario.setMinimumSize(QtCore.QSize(1080, 700))
        superusuario.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(superusuario)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo_menu_su = QtWidgets.QLabel(self.centralwidget)
        self.titulo_menu_su.setGeometry(QtCore.QRect(0, 50, 1081, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG Inline")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titulo_menu_su.setFont(font)
        self.titulo_menu_su.setStyleSheet("font-family: Decotura ICG Inline;\n"
                                          "font-size: 50pt;")
        self.titulo_menu_su.setTextFormat(QtCore.Qt.PlainText)
        self.titulo_menu_su.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_menu_su.setObjectName("titulo_menu_su")
        self.boton_salir = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir.setGeometry(QtCore.QRect(910, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_salir.setFont(font)
        self.boton_salir.setStyleSheet("font-family: Decotura ICG;\n"
                                       "font-size: 30pt;\n"
                                       "background-color: #ff0000;\n"
                                       "border-radius: 20px;\n"
                                       "color: white;")
        self.boton_salir.setObjectName("boton_salir")
        self.boton_pacientes = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pacientes.setGeometry(QtCore.QRect(50, 190, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_pacientes.setFont(font)
        self.boton_pacientes.setStyleSheet("font-family: Decotura ICG;\n"
                                           "font-size: 30pt;\n"
                                           "background-color: #00aaff;\n"
                                           "border-radius: 20px;\n"
                                           "color: white;")
        self.boton_pacientes.setObjectName("boton_pacientes")
        self.boton_citas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_citas.setGeometry(QtCore.QRect(650, 310, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_citas.setFont(font)
        self.boton_citas.setStyleSheet("font-family: Decotura ICG;\n"
                                       "font-size: 30pt;\n"
                                       "background-color: #00aaff;\n"
                                       "border-radius: 20px;\n"
                                       "color: white;")
        self.boton_citas.setObjectName("boton_citas")
        self.boton_facturas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_facturas.setGeometry(QtCore.QRect(650, 430, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_facturas.setFont(font)
        self.boton_facturas.setStyleSheet("font-family: Decotura ICG;\n"
                                          "font-size: 30pt;\n"
                                          "background-color: #00aaff;\n"
                                          "border-radius: 20px;\n"
                                          "color: white;")
        self.boton_facturas.setObjectName("boton_facturas")
        self.boton_estudios = QtWidgets.QPushButton(self.centralwidget)
        self.boton_estudios.setGeometry(QtCore.QRect(650, 180, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_estudios.setFont(font)
        self.boton_estudios.setStyleSheet("font-family: Decotura ICG;\n"
                                          "font-size: 30pt;\n"
                                          "background-color: #00aaff;\n"
                                          "border-radius: 20px;\n"
                                          "color: white;")
        self.boton_estudios.setObjectName("boton_estudios")
        self.boton_laboratoristas = QtWidgets.QPushButton(self.centralwidget)
        self.boton_laboratoristas.setGeometry(QtCore.QRect(50, 430, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_laboratoristas.setFont(font)
        self.boton_laboratoristas.setStyleSheet("font-family: Decotura ICG;\n"
                                               "font-size: 30pt;\n"
                                               "background-color: #00aaff;\n"
                                               "border-radius: 20px;\n"
                                               "color: white;")
        self.boton_laboratoristas.setObjectName("boton_laboratoristas")
        self.boton_medicos = QtWidgets.QPushButton(self.centralwidget)
        self.boton_medicos.setGeometry(QtCore.QRect(50, 310, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_medicos.setFont(font)
        self.boton_medicos.setStyleSheet("font-family: Decotura ICG;\n"
                                         "font-size: 30pt;\n"
                                         "background-color: #00aaff;\n"
                                         "border-radius: 20px;\n"
                                         "color: white;")
        self.boton_medicos.setObjectName("boton_medicos")
        self.boton_usuarios = QtWidgets.QPushButton(self.centralwidget)
        self.boton_usuarios.setGeometry(QtCore.QRect(350, 550, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_usuarios.setFont(font)
        self.boton_usuarios.setStyleSheet("font-family: Decotura ICG;\n"
                                          "font-size: 30pt;\n"
                                          "background-color: #00aaff;\n"
                                          "border-radius: 20px;\n"
                                          "color: white;")
        self.boton_usuarios.setObjectName("boton_usuarios")
        superusuario.setCentralWidget(self.centralwidget)

        self.retranslateUi(superusuario)
        QtCore.QMetaObject.connectSlotsByName(superusuario)
        
        self.boton_salir.clicked.connect(self.salir)

    def retranslateUi(self, superusuario):
        _translate = QtCore.QCoreApplication.translate
        superusuario.setWindowTitle(_translate("superusuario", "MainWindow"))
        self.titulo_menu_su.setText(_translate("superusuario", "Menú super usuario"))
        self.boton_salir.setText(_translate("superusuario", "Salir"))
        self.boton_pacientes.setText(_translate("superusuario", "Pacientes"))
        self.boton_citas.setText(_translate("superusuario", "Citas"))
        self.boton_facturas.setText(_translate("superusuario", "Facturas"))
        self.boton_estudios.setText(_translate("superusuario", "Estudios"))
        self.boton_laboratoristas.setText(_translate("superusuario", "Laboratoristas"))
        self.boton_medicos.setText(_translate("superusuario", "Médicos"))
        self.boton_usuarios.setText(_translate("superusuario", "Usuarios"))

    def salir(self):
        self.cerrar_superusuario()
        
    def cerrar_superusuario(self):
        app = QtWidgets.QApplication.instance()
        for widget in app.topLevelWidgets():
            if widget.isVisible():
                widget.close()
        self.abrir_iniciosesion()

    def abrir_iniciosesion(self):
        self.inicio_sesion_window = QtWidgets.QMainWindow()
        self.ui = iniciosesion.Ui_iniciosesion()
        self.ui.setupUi(self.inicio_sesion_window)
        self.inicio_sesion_window.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    superusuario = QtWidgets.QMainWindow()
    ui = Ui_superusuario()
    ui.setupUi(superusuario)
    superusuario.show()
    sys.exit(app.exec_())