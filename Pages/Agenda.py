import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCalendarWidget
from PyQt5.QtCore import QDate

interefazAgenda="../Resouces/InterfazAgenda.ui"
from .Agenda import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Conectar la señal selectionChanged del calendario a la función obtener_fecha
        self.calendarWidget.selectionChanged.connect(self.obtener_fecha)

    def obtener_fecha(self):
        fecha_seleccionada = self.calendarWidget.selectedDate()
        dia = fecha_seleccionada.day()
        mes = fecha_seleccionada.month()
        anio = fecha_seleccionada.year()

        # Imprimir la fecha en la consola (puedes modificarlo para usar la fecha como necesites)
        print(f"Fecha seleccionada: {dia}/{mes}/{anio}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())