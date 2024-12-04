from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
import sys
import superusuario
import administrador
import recepcionista
from PyQt5.QtWidgets import QMessageBox

class Ui_iniciosesion(object):
    def setupUi(self, iniciosesion):
        iniciosesion.setObjectName("iniciosesion")
        iniciosesion.resize(1080, 700)
        iniciosesion.setMinimumSize(QtCore.QSize(1080, 700))
        iniciosesion.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(iniciosesion)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo_app = QtWidgets.QLabel(self.centralwidget)
        self.titulo_app.setGeometry(QtCore.QRect(0, 60, 1081, 101))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG Inline")
        font.setPointSize(75)
        self.titulo_app.setFont(font)
        self.titulo_app.setStyleSheet("font-family: Decotura ICG Inline;\n"
                                      "font-size: 75pt;")
        self.titulo_app.setTextFormat(QtCore.Qt.PlainText)
        self.titulo_app.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_app.setObjectName("titulo_app")
        self.titulo_inicio = QtWidgets.QLabel(self.centralwidget)
        self.titulo_inicio.setGeometry(QtCore.QRect(0, 210, 1081, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo_inicio.sizePolicy().hasHeightForWidth())
        self.titulo_inicio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.titulo_inicio.setFont(font)
        self.titulo_inicio.setStyleSheet("font-family: Decotura ICG;\n"
                                         "font-size: 30pt;")
        self.titulo_inicio.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo_inicio.setObjectName("titulo_inicio")
        self.introducir_user = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_user.setGeometry(QtCore.QRect(350, 310, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.introducir_user.setFont(font)
        self.introducir_user.setStyleSheet("font-family: Decotura ICG;\n"
                                           "font-size: 30pt;\n"
                                           "border-radius: 20px;\n"
                                           "border: 3px solid #c0c0c0;\n"
                                           "padding: 5px;")
        self.introducir_user.setObjectName("introducir_user")
        self.introducir_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.introducir_pass.setGeometry(QtCore.QRect(350, 430, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.introducir_pass.setFont(font)
        self.introducir_pass.setStyleSheet("font-family: Decotura ICG;\n"
                                           "font-size: 30pt;\n"
                                           "border-radius: 20px;\n"
                                           "border: 3px solid #c0c0c0;\n"
                                           "padding: 5px;")
        self.introducir_pass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.introducir_pass.setObjectName("introducir_pass")
        self.boton_is = QtWidgets.QPushButton(self.centralwidget)
        self.boton_is.setGeometry(QtCore.QRect(350, 550, 381, 71))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG")
        font.setPointSize(30)
        self.boton_is.setFont(font)
        self.boton_is.setStyleSheet("font-family: Decotura ICG;\n"
                                    "font-size: 30pt;\n"
                                    "background-color: #0ff000;\n"
                                    "border-radius: 20px;\n"
                                    "color: white;")
        self.boton_is.setObjectName("boton_is")
        iniciosesion.setCentralWidget(self.centralwidget)

        self.retranslateUi(iniciosesion)
        QtCore.QMetaObject.connectSlotsByName(iniciosesion)
        
        self.boton_is.clicked.connect(self.login)

    def retranslateUi(self, iniciosesion):
        _translate = QtCore.QCoreApplication.translate
        iniciosesion.setWindowTitle(_translate("iniciosesion", "MainWindow"))
        self.titulo_app.setText(_translate("iniciosesion", "Medical Solution"))
        self.titulo_inicio.setText(_translate("iniciosesion", "Inicio de sesión"))
        self.introducir_user.setPlaceholderText(_translate("iniciosesion", "Usuario"))
        self.introducir_pass.setPlaceholderText(_translate("iniciosesion", "Contraseña"))
        self.boton_is.setText(_translate("iniciosesion", "Iniciar sesión"))

    def login(self):
        username = self.introducir_user.text()
        password = self.introducir_pass.text()
        
        #Conectar a la base de datos
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="laboratorio_clinico"
        )

        cursor = connection.cursor()
        cursor.execute("SELECT usuario, contraseña, rol FROM usuarios WHERE usuario=%s AND contraseña=%s", (username, password))
        result = cursor.fetchone()

        if result:
            usuario, contrasena, rol = result
            if rol == 'superusuario':
                self.open_superusuario_menu()
            elif rol == 'administrador':
                self.open_administrador_menu()
            elif rol == 'recepcionista':
                self.open_recepcionista_menu()
            else:
                self.show_message("Rol no reconocido")
        else:
            self.show_message("Usuario o contraseña incorrectos")

        cursor.close()
        connection.close()

    def open_superusuario_menu(self):
        self.cerrar_iniciosesion()
        self.superusuario_window = QtWidgets.QMainWindow()
        self.ui = superusuario.Ui_superusuario()
        self.ui.setupUi(self.superusuario_window)
        self.superusuario_window.show()

    def open_administrador_menu(self):
        self.cerrar_iniciosesion()
        self.administrador_window = QtWidgets.QMainWindow()
        self.ui = administrador.Ui_administrador()
        self.ui.setupUi(self.administrador_window)
        self.administrador_window.show()

    def open_recepcionista_menu(self):
        self.cerrar_iniciosesion()
        self.recepcionista_window = QtWidgets.QMainWindow()
        self.ui = recepcionista.Ui_recepcionista()
        self.ui.setupUi(self.recepcionista_window)
        self.recepcionista_window.show()

    def show_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle("Mensaje")
        msg.exec_()

    def cerrar_iniciosesion(self):
        app = QtWidgets.QApplication.instance()
        for widget in app.topLevelWidgets():
            if widget.isVisible():
                widget.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    iniciosesion = QtWidgets.QMainWindow()
    ui = Ui_iniciosesion()
    ui.setupUi(iniciosesion)
    iniciosesion.show()
    sys.exit(app.exec_())