# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui
from DB import conectar
from your_functions import (
    crear_cita_clinica,
    leer_citas_clinicas,
    actualizar_cita_clinica,
    eliminar_cita_clinica,
    obtener_horas_disponibles,
)


class Ui_CitasClinicas(object):
    def setupUi(self, CitasClinicas):
        CitasClinicas.setObjectName("CitasClinicas")
        CitasClinicas.resize(1200, 800)

        # Central widget
        self.centralwidget = QtWidgets.QWidget(CitasClinicas)
        self.centralwidget.setObjectName("centralwidget")

        # Title
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 20, 1200, 60))
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setFont(QtGui.QFont("Arial", 24))
        self.title.setText("Gestión de Citas Clínicas")

        # Table for displaying citas
        self.tabla_citas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_citas.setGeometry(QtCore.QRect(50, 100, 1100, 300))
        self.tabla_citas.setObjectName("tabla_citas")

        # Input fields for cita details
        self.nombre_input = QtWidgets.QLineEdit(self.centralwidget)
        self.nombre_input.setGeometry(QtCore.QRect(50, 450, 250, 40))
        self.nombre_input.setPlaceholderText("Nombre del Paciente")

        self.apellido_input = QtWidgets.QLineEdit(self.centralwidget)
        self.apellido_input.setGeometry(QtCore.QRect(320, 450, 250, 40))
        self.apellido_input.setPlaceholderText("Apellido del Paciente")

        self.telefono_input = QtWidgets.QLineEdit(self.centralwidget)
        self.telefono_input.setGeometry(QtCore.QRect(590, 450, 250, 40))
        self.telefono_input.setPlaceholderText("Teléfono")

        self.tipo_estudio_input = QtWidgets.QLineEdit(self.centralwidget)
        self.tipo_estudio_input.setGeometry(QtCore.QRect(860, 450, 250, 40))
        self.tipo_estudio_input.setPlaceholderText("Tipo de Estudio")

        self.fecha_input = QtWidgets.QDateEdit(self.centralwidget)
        self.fecha_input.setGeometry(QtCore.QRect(50, 510, 250, 40))
        self.fecha_input.setCalendarPopup(True)
        self.fecha_input.setDisplayFormat("yyyy-MM-dd")

        self.hora_input = QtWidgets.QTimeEdit(self.centralwidget)
        self.hora_input.setGeometry(QtCore.QRect(320, 510, 250, 40))
        self.hora_input.setDisplayFormat("HH:mm:ss")

        # Buttons for CRUD operations
        self.boton_crear = QtWidgets.QPushButton(self.centralwidget)
        self.boton_crear.setGeometry(QtCore.QRect(50, 600, 200, 50))
        self.boton_crear.setText("Crear Cita")

        self.boton_leer = QtWidgets.QPushButton(self.centralwidget)
        self.boton_leer.setGeometry(QtCore.QRect(270, 600, 200, 50))
        self.boton_leer.setText("Leer Citas")

        self.boton_actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_actualizar.setGeometry(QtCore.QRect(490, 600, 200, 50))
        self.boton_actualizar.setText("Actualizar Cita")

        self.boton_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_eliminar.setGeometry(QtCore.QRect(710, 600, 200, 50))
        self.boton_eliminar.setText("Eliminar Cita")

        # Table for displaying available times
        self.tabla_horas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_horas.setGeometry(QtCore.QRect(950, 500, 200, 200))
        self.tabla_horas.setObjectName("tabla_horas")

        self.boton_horas_disponibles = QtWidgets.QPushButton(self.centralwidget)
        self.boton_horas_disponibles.setGeometry(QtCore.QRect(950, 450, 200, 40))
        self.boton_horas_disponibles.setText("Horas Disponibles")

        CitasClinicas.setCentralWidget(self.centralwidget)

        # Connect button actions
        self.boton_crear.clicked.connect(self.crear_cita)
        self.boton_leer.clicked.connect(self.mostrar_citas)
        self.boton_actualizar.clicked.connect(self.actualizar_cita)
        self.boton_eliminar.clicked.connect(self.eliminar_cita)
        self.boton_horas_disponibles.clicked.connect(self.mostrar_horas_disponibles)

    def crear_cita(self):
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        telefono = self.telefono_input.text()
        tipo = self.tipo_estudio_input.text()
        fecha = self.fecha_input.text()
        hora = self.hora_input.text()
        crear_cita_clinica(nombre, apellido, telefono, tipo, fecha, hora)

    def mostrar_citas(self):
        leer_citas_clinicas(self.tabla_citas)

    def actualizar_cita(self):
        id_cita = self.tabla_citas.currentRow()
        nombre = self.nombre_input.text()
        apellido = self.apellido_input.text()
        telefono = self.telefono_input.text()
        tipo = self.tipo_estudio_input.text()
        fecha = self.fecha_input.text()
        hora = self.hora_input.text()
        actualizar_cita_clinica(id_cita, nombre, apellido, telefono, tipo, fecha, hora)

    def eliminar_cita(self):
        id_cita = self.tabla_citas.currentRow()
        eliminar_cita_clinica(id_cita)

    def mostrar_horas_disponibles(self):
        fecha = self.fecha_input.text()
        obtener_horas_disponibles(fecha, self.tabla_horas)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CitasClinicas = QtWidgets.QMainWindow()
    ui = Ui_CitasClinicas()
    ui.setupUi(CitasClinicas)
    CitasClinicas.show()
    sys.exit(app.exec_())
