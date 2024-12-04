from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import iniciosesion

class Ui_recepcionista(object):
    def setupUi(self, recepcionista):
        recepcionista.setObjectName("recepcionista")
        recepcionista.resize(1080, 700)
        recepcionista.setMinimumSize(QtCore.QSize(1080, 700))
        recepcionista.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(recepcionista)
        self.centralwidget.setObjectName("centralwidget")
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
        self.boton_facturas2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_facturas2.setGeometry(QtCore.QRect(350, 430, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_facturas2.setFont(font)
        self.boton_facturas2.setStyleSheet("font-family: Decotura ICG;\n"
                                           "font-size: 30pt;\n"
                                           "background-color: #00aaff;\n"
                                           "border-radius: 20px;\n"
                                           "color: white;")
        self.boton_facturas2.setObjectName("boton_facturas2")
        self.boton_citas2 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_citas2.setGeometry(QtCore.QRect(350, 310, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_citas2.setFont(font)
        self.boton_citas2.setStyleSheet("font-family: Decotura ICG;\n"
                                        "font-size: 30pt;\n"
                                        "background-color: #00aaff;\n"
                                        "border-radius: 20px;\n"
                                        "color: white;")
        self.boton_citas2.setObjectName("boton_citas2")
        self.boton_salir3 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir3.setGeometry(QtCore.QRect(920, 50, 111, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_salir3.setFont(font)
        self.boton_salir3.setStyleSheet("font-family: Decotura ICG;\n"
                                        "font-size: 30pt;\n"
                                        "background-color: #ff0000;\n"
                                        "border-radius: 20px;\n"
                                        "color: white;")
        self.boton_salir3.setObjectName("boton_salir3")
        self.boton_pacientes3 = QtWidgets.QPushButton(self.centralwidget)
        self.boton_pacientes3.setGeometry(QtCore.QRect(350, 190, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_pacientes3.setFont(font)
        self.boton_pacientes3.setStyleSheet("font-family: Decotura ICG;\n"
                                            "font-size: 30pt;\n"
                                            "background-color: #00aaff;\n"
                                            "border-radius: 20px;\n"
                                            "color: white;")
        self.boton_pacientes3.setObjectName("boton_pacientes3")
        recepcionista.setCentralWidget(self.centralwidget)

        self.retranslateUi(recepcionista)
        QtCore.QMetaObject.connectSlotsByName(recepcionista)

        self.boton_salir3.clicked.connect(self.salir)

    def retranslateUi(self, recepcionista):
        _translate = QtCore.QCoreApplication.translate
        recepcionista.setWindowTitle(_translate("recepcionista", "MainWindow"))
        self.titulo_menu_admin.setText(_translate("recepcionista", "Menú recepcionistas"))
        self.boton_facturas2.setText(_translate("recepcionista", "Facturas"))
        self.boton_citas2.setText(_translate("recepcionista", "Citas"))
        self.boton_salir3.setText(_translate("recepcionista", "Salir"))
        self.boton_pacientes3.setText(_translate("recepcionista", "Pacientes"))

    def salir(self):
        self.cerrar_recepcionista()

    def cerrar_recepcionista(self):
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
    recepcionista = QtWidgets.QMainWindow()
    ui = Ui_recepcionista()
    ui.setupUi(recepcionista)
    recepcionista.show()
    sys.exit(app.exec_())