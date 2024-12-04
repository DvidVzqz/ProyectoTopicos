import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel, QTableWidget, QTableWidgetItem, QMessageBox
)
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import mysql.connector


class FacturacionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Facturación - Pacientes")
        self.setGeometry(100, 100, 800, 600)

        # Configurar conexión MySQL
        self.conn = self.mysql_connect()
        self.cursor = self.conn.cursor(dictionary=True)

        self.initUI()

    def mysql_connect(self):
        """Establece la conexión con la base de datos MySQL."""
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="facturacion"
            )
            return conn
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error de conexión", f"No se pudo conectar a MySQL: {err}")
            sys.exit()

    def initUI(self):
        layout = QVBoxLayout()

        # Campo de búsqueda de pacientes
        self.buscar_paciente_label = QLabel("Buscar Paciente:")
        self.buscar_paciente_input = QLineEdit()
        self.buscar_paciente_input.setPlaceholderText("Nombre del paciente")
        self.buscar_paciente_input.textChanged.connect(self.buscar_paciente)
        layout.addWidget(self.buscar_paciente_label)
        layout.addWidget(self.buscar_paciente_input)

        # Tabla de resultados de pacientes
        self.tabla_pacientes = QTableWidget()
        self.tabla_pacientes.setColumnCount(3)
        self.tabla_pacientes.setHorizontalHeaderLabels(["ID", "Nombre", "Email"])
        layout.addWidget(self.tabla_pacientes)

        # Botón para generar factura
        self.generar_factura_btn = QPushButton("Generar Factura")
        self.generar_factura_btn.clicked.connect(self.generar_factura)
        layout.addWidget(self.generar_factura_btn)

        # Establecer layout
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def buscar_paciente(self):
        """Busca pacientes por nombre."""
        texto = self.buscar_paciente_input.text()
        query = "SELECT id, nombre, email FROM pacientes WHERE nombre LIKE %s"
        self.cursor.execute(query, (f"%{texto}%",))
        resultados = self.cursor.fetchall()

        # Actualizar tabla de pacientes
        self.tabla_pacientes.setRowCount(0)
        for fila, datos in enumerate(resultados):
            self.tabla_pacientes.insertRow(fila)
            self.tabla_pacientes.setItem(fila, 0, QTableWidgetItem(str(datos["id"])))
            self.tabla_pacientes.setItem(fila, 1, QTableWidgetItem(datos["nombre"]))
            self.tabla_pacientes.setItem(fila, 2, QTableWidgetItem(datos["email"]))

    def generar_factura(self):
        """Genera un PDF con la factura."""
        paciente_seleccionado = self.tabla_pacientes.currentRow()
        if paciente_seleccionado == -1:
            QMessageBox.warning(self, "Error", "Debe seleccionar un paciente")
            return

        paciente_id = self.tabla_pacientes.item(paciente_seleccionado, 0).text()
        paciente_nombre = self.tabla_pacientes.item(paciente_seleccionado, 1).text()

        # Datos de ejemplo para la factura
        self.cursor.execute("SELECT clave, nombre, precio FROM estudios")
        estudios = self.cursor.fetchall()
        total = sum(estudio["precio"] for estudio in estudios)

        # Generar el PDF
        self.crear_pdf_factura(paciente_nombre, estudios, total)

        QMessageBox.information(self, "Éxito", "Factura generada correctamente")

    def crear_pdf_factura(self, paciente_nombre, estudios, total):
        """Crea un PDF de la factura."""
        pdf_path = f"factura_{paciente_nombre.replace(' ', '_')}.pdf"
        c = canvas.Canvas(pdf_path, pagesize=letter)
        c.setFont("Helvetica", 12)

        # Encabezado
        c.drawString(50, 750, "Sistema de Facturación")
        c.drawString(50, 735, f"Paciente: {paciente_nombre}")
        c.drawString(50, 720, f"Fecha: {mysql.connector.datetime.datetime.now().strftime('%Y-%m-%d')}")

        # Tabla de estudios
        c.drawString(50, 700, "Detalles de la Factura:")
        y = 680
        for estudio in estudios:
            c.drawString(50, y, f"{estudio['clave']} - {estudio['nombre']} - ${estudio['precio']:.2f}")
            y -= 20

        # Total
        c.drawString(50, y - 20, f"Total: ${total:.2f}")

        c.save()
        print(f"Factura guardada en: {pdf_path}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FacturacionApp()
    window.show()
    sys.exit(app.exec_())
