from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import iniciosesion

class Ui_administrador(object):
    def setupUi(self, administrador):
        administrador.setObjectName("administrador")
        administrador.resize(1080, 700)
        administrador.setMinimumSize(QtCore.QSize(1080, 700))
        administrador.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(administrador)
        self.centralwidget.setObjectName("centralwidget")
        self.boton_salir2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir2.setGeometry(QtCore.QRect(920, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_salir2.setFont(font)
        self.boton_salir2.setStyleSheet("font-family: Decotura ICG;\n"
                                        "font-size: 30pt;\n"
                                        "background-color: #ff0000;\n"
                                        "border-radius: 20px;\n"
                                        "color: white;")
        self.boton_salir2.setObjectName("boton_salir2")
        self.boton_laboratoristas2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_laboratoristas2.setGeometry(QtCore.QRect(350, 430, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_laboratoristas2.setFont(font)
        self.boton_laboratoristas2.setStyleSheet("font-family: Decotura ICG;\n"
                                                 "font-size: 30pt;\n"
                                                 "background-color: #00aaff;\n"
                                                 "border-radius: 20px;\n"
                                                 "color: white;")
        self.boton_laboratoristas2.setObjectName("boton_laboratoristas2")
        self.titulo_menu_admin = QtWidgets.QLabel(self.centralwidget)
        self.titulo_menu_admin.setGeometry(QtCore.QRect(0, 50, 1081, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG Inline")
        font.setPointSize(50)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.titulo_menu_admin.setFont(font)
        self.titulo_menu_admin.setStyleSheet("font-family: Decotura ICG Inline;\n"
                                             "font-size: 50pt;")
        self.titulo_menu_admin.setTextFormat(QtCore.Qt.PlainText)
        self.titulo_menu_admin.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_menu_admin.setObjectName("titulo_menu_admin")
        self.boton_estudios2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_estudios2.setGeometry(QtCore.QRect(350, 550, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_estudios2.setFont(font)
        self.boton_estudios2.setStyleSheet("font-family: Decotura ICG;\n"
                                           "font-size: 30pt;\n"
                                           "background-color: #00aaff;\n"
                                           "border-radius: 20px;\n"
                                           "color: white;")
        self.boton_estudios2.setObjectName("boton_estudios2")
        self.boton_pacientes2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pacientes2.setGeometry(QtCore.QRect(350, 190, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_pacientes2.setFont(font)
        self.boton_pacientes2.setStyleSheet("font-family: Decotura ICG;\n"
                                            "font-size: 30pt;\n"
                                            "background-color: #00aaff;\n"
                                            "border-radius: 20px;\n"
                                            "color: white;")
        self.boton_pacientes2.setObjectName("boton_pacientes2")
        self.boton_medicos2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_medicos2.setGeometry(QtCore.QRect(350, 310, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_medicos2.setFont(font)
        self.boton_medicos2.setStyleSheet("font-family: Decotura ICG;\n"
                                          "font-size: 30pt;\n"
                                          "background-color: #00aaff;\n"
                                          "border-radius: 20px;\n"
                                          "color: white;")
        self.boton_medicos2.setObjectName("boton_medicos2")
        self.titulo_menu_admin.raise_()
        self.boton_salir2.raise_()
        self.boton_laboratoristas2.raise_()
        self.boton_estudios2.raise_()
        self.boton_pacientes2.raise_()
        self.boton_medicos2.raise_()
        administrador.setCentralWidget(self.centralwidget)

        self.retranslateUi(administrador)
        QtCore.QMetaObject.connectSlotsByName(administrador)

        self.boton_salir2.clicked.connect(self.salir)

    def retranslateUi(self, administrador):
        _translate = QtCore.QCoreApplication.translate
        administrador.setWindowTitle(_translate("administrador", "MainWindow"))
        self.boton_salir2.setText(_translate("administrador", "Salir"))
        self.boton_laboratoristas2.setText(_translate("administrador", "Laboratoristas"))
        self.titulo_menu_admin.setText(_translate("administrador", "Menú administradores"))
        self.boton_estudios2.setText(_translate("administrador", "Estudios"))
        self.boton_pacientes2.setText(_translate("administrador", "Pacientes"))
        self.boton_medicos2.setText(_translate("administrador", "Médicos"))

    def salir(self):
        self.cerrar_administrador()

    def cerrar_administrador(self):
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
    administrador = QtWidgets.QMainWindow()
    ui = Ui_administrador()
    ui.setupUi(administrador)
    administrador.show()
    sys.exit(app.exec_())