# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets, QtCore, QtGui


class Ui_CitasCrud(object):
    def setupUi(self, CitasCrud):
        CitasCrud.setObjectName("CitasCrud")
        CitasCrud.resize(1080, 700)
        CitasCrud.setMinimumSize(QtCore.QSize(1080, 700))
        CitasCrud.setMaximumSize(QtCore.QSize(1080, 700))
        self.centralwidget = QtWidgets.QWidget(CitasCrud)
        self.centralwidget.setObjectName("centralwidget")

        # Título
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(0, 20, 1080, 50))
        font = QtGui.QFont()
        font.setFamily("Decotura ICG Inline")
        font.setPointSize(36)
        self.titulo.setFont(font)
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setText("Gestión de Citas")
        self.titulo.setObjectName("titulo")

        # Tabla de citas
        self.tabla_citas = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_citas.setGeometry(QtCore.QRect(50, 80, 980, 250))
        self.tabla_citas.setObjectName("tabla_citas")
        self.tabla_citas.setColumnCount(0)
        self.tabla_citas.setRowCount(0)

        # Botones CRUD
        self.boton_agregar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_agregar.setGeometry(QtCore.QRect(50, 350, 200, 50))
        self.boton_agregar.setStyleSheet("background-color: #00ff00; color: white; font-size: 18px; border-radius: 10px;")
        self.boton_agregar.setText("Agregar Cita")
        self.boton_agregar.setObjectName("boton_agregar")

        self.boton_actualizar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_actualizar.setGeometry(QtCore.QRect(280, 350, 200, 50))
        self.boton_actualizar.setStyleSheet("background-color: #00aaff; color: white; font-size: 18px; border-radius: 10px;")
        self.boton_actualizar.setText("Actualizar Cita")
        self.boton_actualizar.setObjectName("boton_actualizar")

        self.boton_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_eliminar.setGeometry(QtCore.QRect(510, 350, 200, 50))
        self.boton_eliminar.setStyleSheet("background-color: #ff0000; color: white; font-size: 18px; border-radius: 10px;")
        self.boton_eliminar.setText("Eliminar Cita")
        self.boton_eliminar.setObjectName("boton_eliminar")

        # Campos para agregar/editar citas
        self.label_paciente = QtWidgets.QLabel(self.centralwidget)
        self.label_paciente.setGeometry(QtCore.QRect(50, 420, 200, 30))
        self.label_paciente.setText("Nombre del Paciente:")
        self.label_paciente.setObjectName("label_paciente")

        self.campo_paciente = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_paciente.setGeometry(QtCore.QRect(260, 420, 300, 30))
        self.campo_paciente.setObjectName("campo_paciente")

        self.label_medico = QtWidgets.QLabel(self.centralwidget)
        self.label_medico.setGeometry(QtCore.QRect(50, 460, 200, 30))
        self.label_medico.setText("Médico Asignado:")
        self.label_medico.setObjectName("label_medico")

        self.campo_medico = QtWidgets.QLineEdit(self.centralwidget)
        self.campo_medico.setGeometry(QtCore.QRect(260, 460, 300, 30))
        self.campo_medico.setObjectName("campo_medico")

        self.label_fecha = QtWidgets.QLabel(self.centralwidget)
        self.label_fecha.setGeometry(QtCore.QRect(50, 500, 200, 30))
        self.label_fecha.setText("Fecha de la Cita:")
        self.label_fecha.setObjectName("label_fecha")

        self.campo_fecha = QtWidgets.QDateEdit(self.centralwidget)
        self.campo_fecha.setGeometry(QtCore.QRect(260, 500, 300, 30))
        self.campo_fecha.setCalendarPopup(True)
        self.campo_fecha.setObjectName("campo_fecha")

        self.label_hora = QtWidgets.QLabel(self.centralwidget)
        self.label_hora.setGeometry(QtCore.QRect(50, 540, 200, 30))
        self.label_hora.setText("Hora de la Cita:")
        self.label_hora.setObjectName("label_hora")

        self.campo_hora = QtWidgets.QTimeEdit(self.centralwidget)
        self.campo_hora.setGeometry(QtCore.QRect(260, 540, 300, 30))
        self.campo_hora.setObjectName("campo_hora")

        # Tabla de horarios
        self.tabla_horarios = QtWidgets.QTableWidget(self.centralwidget)
        self.tabla_horarios.setGeometry(QtCore.QRect(600, 420, 400, 150))
        self.tabla_horarios.setObjectName("tabla_horarios")
        self.tabla_horarios.setColumnCount(0)
        self.tabla_horarios.setRowCount(0)

        # Botón para salir
        self.boton_salir = QtWidgets.QPushButton(self.centralwidget)
        self.boton_salir.setGeometry(QtCore.QRect(900, 600, 150, 50))
        self.boton_salir.setStyleSheet("background-color: #ff0000; color: white; font-size: 18px; border-radius: 10px;")
        self.boton_salir.setText("Salir")
        self.boton_salir.setObjectName("boton_salir")

        CitasCrud.setCentralWidget(self.centralwidget)

        self.retranslateUi(CitasCrud)
        QtCore.QMetaObject.connectSlotsByName(CitasCrud)

    def retranslateUi(self, CitasCrud):
        CitasCrud.setWindowTitle("Gestión de Citas Médicas")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CitasCrud = QtWidgets.QMainWindow()
    ui = Ui_CitasCrud()
    ui.setupUi(CitasCrud)
    CitasCrud.show()
    sys.exit(app.exec_())
