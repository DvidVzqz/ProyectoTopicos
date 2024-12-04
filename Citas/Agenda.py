import os
import mysql.connector
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView,QMessageBox
from PyQt5.QtGui import QColor, QBrush
from PyQt5.QtCore import Qt
from datetime import datetime, timedelta, date, time

class SemanaApp(QMainWindow):
    def __init__(self):
        super().__init__()
        ruta_ui = os.path.join(os.path.dirname(__file__), "CitasWindow.ui")
        loadUi(ruta_ui, self)

        # Configurar timeEditHora para deshabilitar minutos
        self.timeEditHora.setDisplayFormat("hh:00")  # Formato de visualización solo para horas
        self.timeEditHora.setWrapping(False)  # No permitir valores fuera del rango
        self.timeEditHora.setTimeRange(time(7, 0), time(19, 0))  # Limitar el rango de horas
        self.timeEditHora.timeChanged.connect(self.restringirMinutos)  # Conectar al evento de cambio de hora

        
        # Ajustar el tamaño de las celdas y encabezados
        self.tableWidgetSemana.horizontalHeader().setDefaultSectionSize(120)  # Ancho predeterminado
        self.tableWidgetSemana.verticalHeader().setDefaultSectionSize(30)    # Altura predeterminada
        self.tableWidgetSemana.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidgetSemana.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        self.inicio_semana = (datetime.now() - timedelta(days=datetime.now().weekday())).date()
        self.citas_por_celda = {}  
        self.citas_actuales = []  
        self.indice_cita_actual = 0  

        self.btnGuardarNuevaCita.setVisible(False)
        self.btnGuardarCita.setVisible(False)
        self.btnEliminarCita.setVisible(False)
        self.btnGuardarNuevaCita.setVisible(False)
        
        self.btnEliminarCita.clicked.connect(self.eliminarCita)
        self.btnGuardarCita.clicked.connect(self.guardarCita)
        self.btnGuardarNuevaCita.clicked.connect(self.guardarNuevaCita)
        self.btnSiguiente.clicked.connect(self.mostrarSiguienteSemana)
        self.btnAnterior.clicked.connect(self.mostrarSemanaAnterior)
        self.tableWidgetSemana.cellClicked.connect(self.mostrarDetallesCita)  # Conectar el evento
        self.btnAnteriorDetalles.clicked.connect(self.mostrarCitaAnterior)
        self.btnSiguienteDetalles.clicked.connect(self.mostrarCitaSiguiente)

        self.actualizarFechas()
        self.cargarPacientes() 
        
    def conectar_db(self):
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="clinica"
        )
    
    def restringirMinutos(self):
        hora_actual = self.timeEditHora.time()
        hora_sin_minutos = hora_actual.hour()
        self.timeEditHora.setTime(time(hora_sin_minutos, 0))  # Ajustar a hora sin minutos
    
    def inicializarComboBox(self, comboBox):
        comboBox.clear()  # Limpiar cualquier dato previo
        comboBox.addItem("Seleccionar")
    
    def mostrarBotonesCita(self, guardar_visible, eliminar_visible, nueva_cita_visible):
        self.btnGuardarCita.setVisible(guardar_visible)
        self.btnEliminarCita.setVisible(eliminar_visible)
        self.btnGuardarNuevaCita.setVisible(nueva_cita_visible)

    def mostrarBotonNuevaCita(self, visible):
        self.btnGuardarNuevaCita.setVisible(visible)
    
    def habilitarPanelDetalles(self, habilitar=True):
        self.comboBoxPaciente.setEnabled(habilitar)
        self.lineEditMotivo.setEnabled(habilitar)
        self.dateEditFecha.setEnabled(habilitar)
        self.timeEditHora.setEnabled(habilitar)
        self.comboBoxEstado.setEnabled(habilitar)
        self.comboBoxDentista.setEnabled(habilitar)
        self.btnGuardarCita.setEnabled(habilitar)
        self.btnEliminarCita.setEnabled(habilitar)

    def eliminarCita(self):
        if not self.citas_actuales:
            return

        respuesta = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            "¿Estás seguro de que deseas eliminar esta cita?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            cita = self.citas_actuales[self.indice_cita_actual]
            fecha, hora, id_paciente, motivo, estado, dentista = cita

            try:
                conn = self.conectar_db()
                cursor = conn.cursor()
                
                query_eliminar = """
                    UPDATE CitasMedicas
                    SET estado = 'Cancelada'
                    WHERE fecha = %s AND hora = %s AND id_dentista = (
                        SELECT id FROM dentistas WHERE nombre = %s
                    )
                """
                cursor.execute(query_eliminar, (fecha, hora, dentista))
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Cita Eliminada", "La cita ha sido eliminada exitosamente.")

                # Actualizar la vista de la tabla después de eliminar la cita
                self.actualizarFechas()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al eliminar la cita: {e}")

    def guardarCita(self):
        if not self.citas_actuales:
            QMessageBox.warning(self, "Sin Cita Seleccionada", "No hay una cita seleccionada para guardar.")
            return

        # Obtener los datos actuales del panel de detalles
        fecha = self.dateEditFecha.date().toPyDate()
        hora = self.timeEditHora.time().toPyTime()
        paciente = self.comboBoxPaciente.currentText()
        motivo = self.lineEditMotivo.text()
        estado = self.comboBoxEstado.currentText().lower()
        dentista = self.comboBoxDentista.currentText()

        # Validar que los campos no tengan "Seleccionar"
        if paciente == "Seleccionar" or dentista == "Seleccionar" or not motivo or estado == "seleccionar":
            QMessageBox.warning(self, "Campos Inválidos", "Todos los campos deben estar completos y válidos.")
            return

        # Confirmación de actualización
        respuesta = QMessageBox.question(
            self,
            "Confirmar Guardar",
            "¿Estás seguro de que deseas guardar los cambios en esta cita?",
            QMessageBox.Yes | QMessageBox.No
        )

        if respuesta == QMessageBox.Yes:
            try:
                # Obtener los datos de la cita actual seleccionada
                cita_actual = self.citas_actuales[self.indice_cita_actual]
                fecha_original, hora_original, nombre_paciente_original, motivo_original, estado_original, dentista_original = cita_actual

                conn = self.conectar_db()
                cursor = conn.cursor()

                # Actualizar los datos en la base de datos
                query_actualizar = """
                    UPDATE CitasMedicas
                    SET fecha = %s, hora = %s, id_paciente = (
                        SELECT id FROM Pacientes WHERE nombre = %s
                    ), motivo = %s, estado = %s, id_dentista = (
                        SELECT id FROM dentistas WHERE nombre = %s
                    )
                    WHERE fecha = %s AND hora = %s AND id_dentista = (
                        SELECT id FROM dentistas WHERE nombre = %s
                    )
                """
                cursor.execute(query_actualizar, (
                    fecha, hora, paciente, motivo, estado, dentista,
                    fecha_original, hora_original, dentista_original
                ))
                conn.commit()
                conn.close()

                QMessageBox.information(self, "Cita Guardada", "Los cambios en la cita se han guardado exitosamente.")

                # Refrescar la vista de la tabla
                self.actualizarFechas()

            except Exception as e:
                QMessageBox.critical(self, "Error", f"Ocurrió un error al guardar los cambios: {e}")

    def guardarNuevaCita(self):
        # Obtener los datos del panel de detalles
        fecha = self.dateEditFecha.date().toPyDate()
        hora = self.timeEditHora.time().toPyTime()
        paciente = self.comboBoxPaciente.currentText()
        dentista = self.comboBoxDentista.currentText()
        motivo = self.lineEditMotivo.text()
        estado = self.comboBoxEstado.currentText()

        # Validar que los campos no tengan "Seleccionar"
        if paciente == "Seleccionar" or dentista == "Seleccionar" or not motivo or estado == "Seleccionar":
            QMessageBox.warning(self, "Campos Inválidos", "Todos los campos deben estar completos y válidos.")
            return

        try:
            conn = self.conectar_db()
            cursor = conn.cursor()

            # Validar si la cita ya existe
            query_validar = """
                SELECT COUNT(*)
                FROM CitasMedicas
                WHERE fecha = %s AND hora = %s AND id_dentista = (
                    SELECT id FROM dentistas WHERE nombre = %s
                ) AND estado != 'Cancelada'
            """
            cursor.execute(query_validar, (fecha, hora, dentista))
            resultado = cursor.fetchone()

            if resultado[0] > 0:
                QMessageBox.warning(self, "Error", "Ya existe una cita con el mismo dentista, fecha y hora.")
                conn.close()
                return

            # Insertar la nueva cita
            query_insertar = """
                INSERT INTO CitasMedicas (fecha, hora, id_paciente, id_dentista, motivo, estado)
                VALUES (
                    %s, %s,
                    (SELECT id FROM Pacientes WHERE nombre = %s),
                    (SELECT id FROM dentistas WHERE nombre = %s),
                    %s, %s
                )
            """
            cursor.execute(query_insertar, (fecha, hora, paciente, dentista, motivo, estado))
            conn.commit()

            QMessageBox.information(self, "Éxito", "Cita guardada correctamente.")
            conn.close()

            # Recargar la tabla de citas
            self.cargarCitas()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al guardar la cita: {e}")

    def cargarPacientes(self, fecha=None, hora=None):
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()

            # Consulta para obtener los pacientes que no tienen citas ese día y hora
            query = """
                SELECT nombre 
                FROM Pacientes 
                WHERE id NOT IN (
                    SELECT id_paciente 
                    FROM CitasMedicas 
                    WHERE fecha = %s AND hora = %s AND estado != 'Cancelada'
                )
            """
            # Usar fecha y hora actuales si no se proporcionan
            if not fecha:
                fecha = self.dateEditFecha.date().toPyDate()
            if not hora:
                hora = self.timeEditHora.time().toPyTime()

            # Ejecutar la consulta con fecha y hora como parámetros
            cursor.execute(query, (fecha, hora))
            pacientes = cursor.fetchall()

            # Preserva la opción "Seleccionar" en el ComboBox
            self.comboBoxPaciente.clear()
            self.comboBoxPaciente.addItem("Seleccionar")

            for paciente in pacientes:
                self.comboBoxPaciente.addItem(paciente[0])  # Agregar cada nombre al combo box

            conn.close()
        except Exception as e:
            print(f"Error al cargar los pacientes: {e}")

    def cargarDentistasDisponibles(self, fecha, hora):
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()
            
            # Consulta para obtener los dentistas disponibles
            query = """
                SELECT d.nombre
                FROM dentistas d
                WHERE d.id NOT IN (
                    SELECT c.id_dentista
                    FROM CitasMedicas c
                    WHERE c.fecha = %s AND c.hora = %s AND c.estado != 'cancelada'
                )
            """
            cursor.execute(query, (fecha, hora))
            dentistas = cursor.fetchall()

            self.inicializarComboBox(self.comboBoxDentista)  # Agregar opción "Seleccionar" primero

            for dentista in dentistas:
                self.comboBoxDentista.addItem(dentista[0])  # Agregar cada dentista al combo box

            conn.close()
        except Exception as e:
            print(f"Error al cargar los dentistas disponibles: {e}")

    def actualizarFechas(self, ajustar_inicio=True):
        if ajustar_inicio:
            nueva_semana, _ = self.encontrarPrimeraCeldaDisponible()
            self.inicio_semana = nueva_semana  # Solo ajustar al iniciar o cuando se indique

        for i in range(7):  # 7 días de la semana
            fecha = self.inicio_semana + timedelta(days=i)
            self.tableWidgetSemana.setHorizontalHeaderItem(i, QTableWidgetItem(fecha.strftime("%d - %A")))

        # Establecer las horas en el encabezado vertical
        horas = [
            "07:00 AM", "08:00 AM", "09:00 AM", "10:00 AM", "11:00 AM",
            "12:00 PM", "01:00 PM", "02:00 PM", "03:00 PM", "04:00 PM",
            "05:00 PM", "06:00 PM", "07:00 PM"
        ]
        for i, hora in enumerate(horas):
            self.tableWidgetSemana.setVerticalHeaderItem(i, QTableWidgetItem(hora))

        self.tableWidgetSemana.clearContents()
        self.desactivarCeldasPasadas()
        self.cargarCitas()
        self.mostrarHorasDisponibles()

    def encontrarPrimeraCeldaDisponible(self):
        hora_actual = datetime.now().time()
        fecha_actual = datetime.now().date()
        semana_inicio = self.inicio_semana  # Usar una copia temporal

        while True:
            for dia in range(7):  # Días de la semana
                fecha_celda = semana_inicio + timedelta(days=dia)
                for hora_index, hora in enumerate([
                    "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
                    "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00",
                    "17:00:00", "18:00:00", "19:00:00"
                ]):
                    hora_celda = datetime.strptime(hora, "%H:%M:%S").time()
                    item = self.tableWidgetSemana.item(hora_index, dia)

                    # Si la celda está en el futuro y está vacía
                    if fecha_celda >= fecha_actual and (fecha_celda > fecha_actual or hora_celda > hora_actual):
                        if item is None or not item.text():
                            # Retornar la semana y posición encontrada
                            return semana_inicio, (hora_index, dia)

            # Avanzar una semana si no se encontró ninguna celda disponible
            semana_inicio += timedelta(weeks=1)

    def desactivarCeldasPasadas(self):
        hora_actual = datetime.now().time()
        fecha_actual = datetime.now().date()

        for dia in range(7):  # 7 días de la semana
            fecha_celda = self.inicio_semana + timedelta(days=dia)
            for hora_index, hora in enumerate([
                "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
                "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00",
                "17:00:00", "18:00:00", "19:00:00"
            ]):
                hora_celda = datetime.strptime(hora, "%H:%M:%S").time()

                if fecha_celda < fecha_actual or (fecha_celda == fecha_actual and hora_celda <= hora_actual):
                    item = QTableWidgetItem("")
                    item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                    item.setBackground(QBrush(QColor(200, 200, 200)))
                    self.tableWidgetSemana.setItem(hora_index, dia, item)

    def cargarCitas(self):
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()

            fecha_inicio = self.inicio_semana.strftime("%Y-%m-%d")
            fecha_fin = (self.inicio_semana + timedelta(days=6)).strftime("%Y-%m-%d")
            query = """
                SELECT CitasMedicas.fecha, CitasMedicas.hora, Pacientes.nombre, 
                    CitasMedicas.motivo, CitasMedicas.estado, dentistas.nombre
                FROM CitasMedicas
                JOIN Pacientes ON CitasMedicas.id_paciente = Pacientes.id
                JOIN dentistas ON CitasMedicas.id_dentista = dentistas.id
                WHERE CitasMedicas.fecha BETWEEN %s AND %s
            """
            cursor.execute(query, (fecha_inicio, fecha_fin))
            self.citas = cursor.fetchall()

            self.citas_por_celda = {}

            for cita in self.citas:
                fecha, hora, nombre_paciente, motivo, estado, dentista = cita

                if estado.lower() == "cancelada":
                    continue

                # Convertir hora a datetime.time si es timedelta
                if isinstance(hora, timedelta):
                    hora = (datetime.min + hora).time()

                fecha_date = fecha if isinstance(fecha, date) else fecha.date()
                dia_semana = (fecha_date - self.inicio_semana).days

                hora_str = hora.strftime("%H:%M:%S")
                hora_index = self.hora_a_indice(hora_str)

                if 0 <= dia_semana < 7 and 0 <= hora_index < 13:
                    clave_celda = (hora_index, dia_semana)
                    if clave_celda not in self.citas_por_celda:
                        self.citas_por_celda[clave_celda] = []
                    self.citas_por_celda[clave_celda].append(cita)

                    # Mostrar el nombre del primer paciente y "+N" si hay más citas
                    primer_paciente = self.citas_por_celda[clave_celda][0][2]
                    total_citas = len(self.citas_por_celda[clave_celda])
                    texto_celda = primer_paciente
                    if total_citas > 1:
                        texto_celda += f" +{total_citas - 1}"

                    item = QTableWidgetItem(texto_celda)

                    # Asignar color según el estado de la primera cita
                    primer_estado = self.citas_por_celda[clave_celda][0][4]
                    if primer_estado.lower() == "pendiente":
                        item.setBackground(QBrush(QColor(255, 140, 0)))  # Naranja oscuro
                    elif primer_estado.lower() == "confirmada":
                        item.setBackground(QBrush(QColor(0, 102, 204)))  # Azul oscuro

                    item.setForeground(QBrush(QColor(255, 255, 255)))  # Texto blanco
                    item.setTextAlignment(Qt.AlignCenter)
                    self.tableWidgetSemana.setItem(hora_index, dia_semana, item)

            conn.close()
        except Exception as e:
            print(f"Error al cargar las citas: {e}")

    def actualizarCeldaCita(self, fila, columna, cita):
        nombre_paciente, estado = cita[2], cita[4]
        texto_celda = nombre_paciente
        if len(self.citas_por_celda.get((fila, columna), [])) > 1:
            texto_celda += f" +{len(self.citas_por_celda[(fila, columna)]) - 1}"

        item = self.tableWidgetSemana.item(fila, columna)
        if not item:
            item = QTableWidgetItem()
            self.tableWidgetSemana.setItem(fila, columna, item)

        item.setText(texto_celda)

        # Actualizar color según el estado
        if estado.lower() == "pendiente":
            item.setBackground(QBrush(QColor(255, 140, 0)))  # Naranja oscuro
        elif estado.lower() == "confirmada":
            item.setBackground(QBrush(QColor(0, 102, 204)))  # Azul oscuro
        item.setForeground(QBrush(QColor(255, 255, 255)))  # Texto blanco
        item.setTextAlignment(Qt.AlignCenter)

    def mostrarDetallesCita(self, fila, columna):
        # Calcular fecha y hora de la celda seleccionada
        fecha = self.inicio_semana + timedelta(days=columna)
        horas = [
            "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
            "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00",
            "17:00:00", "18:00:00", "19:00:00"
        ]
        hora = datetime.strptime(horas[fila], "%H:%M:%S").time()

        # Asignar la fecha y hora seleccionadas al panel de detalles
        self.dateEditFecha.setDate(fecha)
        self.timeEditHora.setTime(hora)

        # Comparar con la fecha y hora actual para habilitar o deshabilitar creación de nuevas citas
        fecha_hora_actual = datetime.now()
        fecha_hora_seleccionada = datetime.combine(fecha, hora)
        es_futuro = fecha_hora_seleccionada >= fecha_hora_actual

        # Identificar las citas asociadas a la celda seleccionada
        clave_celda = (fila, columna)
        self.citas_actuales = self.citas_por_celda.get(clave_celda, [])
        self.indice_cita_actual = 0

        if self.citas_actuales:
            # Si hay citas, mostrar los detalles de la primera cita
            self.mostrarBotonesCita(guardar_visible=es_futuro, eliminar_visible=es_futuro, nueva_cita_visible=False)
            self.actualizarPanelCita(self.citas_actuales[0])
            self.habilitarPanelDetalles(es_futuro)  # Permitir edición solo si es futuro
            self.actualizarCeldaCita(fila, columna, self.citas_actuales[0])  # Sincronizar con la tabla
        else:
            # Si no hay citas, permitir crear nuevas citas solo en horarios futuros
            if es_futuro:
                self.limpiarPanel()
                self.mostrarBotonesCita(guardar_visible=False, eliminar_visible=False, nueva_cita_visible=True)
                self.habilitarPanelDetalles(True)
                self.cargarDentistasDisponibles(fecha, hora)
            else:
                # Mostrar panel vacío pero deshabilitar creación
                self.limpiarPanel()
                self.habilitarPanelDetalles(False)  # Deshabilitar la funcionalidad
                self.mostrarBotonesCita(guardar_visible=False, eliminar_visible=False, nueva_cita_visible=False)

    def actualizarPanelCita(self, cita):
        fecha, hora, nombre_paciente, motivo, estado, dentista_asignado = cita
        hora_str = (datetime.min + hora).strftime("%H:%M:%S")

        # Establecer los valores en el panel
        if nombre_paciente not in [self.comboBoxPaciente.itemText(i) for i in range(self.comboBoxPaciente.count())]:
            self.comboBoxPaciente.addItem(nombre_paciente)
        self.comboBoxPaciente.setCurrentText(nombre_paciente)

        self.lineEditMotivo.setText(motivo)
        self.dateEditFecha.setDate(fecha)
        self.timeEditHora.setTime(datetime.strptime(hora_str, "%H:%M:%S").time())
        self.comboBoxEstado.setCurrentText(estado.capitalize())

        # Cargar dentistas disponibles para la fecha y hora
        try:
            conn = self.conectar_db()
            cursor = conn.cursor()
            
            query = """
                SELECT d.nombre
                FROM dentistas d
                WHERE d.id NOT IN (
                    SELECT c.id_dentista
                    FROM CitasMedicas c
                    WHERE c.fecha = %s AND c.hora = %s AND c.estado != 'cancelada'
                )
            """
            cursor.execute(query, (fecha, hora))
            dentistas_disponibles = cursor.fetchall()
            
            conn.close()

            # Actualizar el combo box con los dentistas disponibles y el asignado
            self.comboBoxDentista.clear()
            
            for dentista in dentistas_disponibles:
                self.comboBoxDentista.addItem(dentista[0])
            
            # Asegurar que el dentista asignado esté en la lista y seleccionado
            if dentista_asignado not in [self.comboBoxDentista.itemText(i) for i in range(self.comboBoxDentista.count())]:
                self.comboBoxDentista.addItem(dentista_asignado)
            self.comboBoxDentista.setCurrentText(dentista_asignado)

        except Exception as e:
            print(f"Error al cargar los dentistas disponibles: {e}")

    def limpiarPanel(self):
        self.inicializarComboBox(self.comboBoxPaciente)
        self.cargarPacientes()  # Recargar para mantener los pacientes
        self.inicializarComboBox(self.comboBoxDentista)
        self.comboBoxEstado.setCurrentIndex(-1)  # Seleccionar ningún estado
        self.lineEditMotivo.clear()
        # No limpiar la fecha y hora para mantenerlas

    def mostrarCitaAnterior(self):
        if self.citas_actuales and self.indice_cita_actual > 0:
            # Retroceder a la cita anterior
            self.indice_cita_actual -= 1
            cita_actual = self.citas_actuales[self.indice_cita_actual]
            self.actualizarPanelCita(cita_actual)
            self.actualizarCeldaCita(self.obtenerCeldaDeCita(cita_actual)[0], self.obtenerCeldaDeCita(cita_actual)[1], cita_actual)
            self.mostrarBotonesCita(guardar_visible=True, eliminar_visible=True, nueva_cita_visible=False)
        else:
            QMessageBox.information(self, "Aviso", "No hay citas anteriores.")

    def mostrarCitaSiguiente(self):
        if self.citas_actuales and self.indice_cita_actual < len(self.citas_actuales) - 1:
            # Avanzar a la siguiente cita
            self.indice_cita_actual += 1
            cita_actual = self.citas_actuales[self.indice_cita_actual]

            # Convertir hora a datetime.time si es timedelta
            hora = cita_actual[1]
            if isinstance(hora, timedelta):
                hora = (datetime.min + hora).time()

            fecha_hora_cita = datetime.combine(cita_actual[0], hora)
            fecha_hora_actual = datetime.now()
            es_futuro = fecha_hora_cita >= fecha_hora_actual

            self.actualizarPanelCita(cita_actual)
            self.mostrarBotonesCita(guardar_visible=es_futuro, eliminar_visible=es_futuro, nueva_cita_visible=False)
            self.habilitarPanelDetalles(es_futuro)  # Permitir edición solo si es futuro

            # Actualizar la celda en la tabla para reflejar la cita actual mostrada
            self.actualizarCeldaCita(self.obtenerCeldaDeCita(cita_actual)[0], self.obtenerCeldaDeCita(cita_actual)[1], cita_actual)
        else:
            # No hay más citas, verificar si se puede mostrar el panel vacío
            fecha = self.dateEditFecha.date().toPyDate()
            hora = self.timeEditHora.time().toPyTime()

            # Validar si la fecha y hora son futuras
            fecha_hora_actual = datetime.now()
            fecha_hora_seleccionada = datetime.combine(fecha, hora)

            if fecha_hora_seleccionada >= fecha_hora_actual:
                # Mostrar panel vacío para nueva cita
                self.limpiarPanel()
                self.mostrarBotonesCita(guardar_visible=False, eliminar_visible=False, nueva_cita_visible=True)
                self.habilitarPanelDetalles(True)  # Habilitar campos para la nueva cita
                self.cargarDentistasDisponibles(fecha, hora)
            else:
                QMessageBox.information(self, "Aviso", "No puedes agregar nuevas citas en horarios pasados.")

    def obtenerCeldaDeCita(self, cita):
        fecha, hora = cita[0], cita[1]
        fecha_date = fecha if isinstance(fecha, date) else fecha.date()
        dia_semana = (fecha_date - self.inicio_semana).days

        hora_str = (datetime.min + hora).strftime("%H:%M:%S")
        hora_index = self.hora_a_indice(hora_str)

        return hora_index, dia_semana

    def mostrarHorasDisponibles(self):
        horas_disponibles = 0
        hora_actual = datetime.now().time()
        fecha_actual = datetime.now().date()

        for dia in range(7):  # 7 días de la semana
            fecha_celda = self.inicio_semana + timedelta(days=dia)
            for hora_index, hora in enumerate([
                "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
                "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00",
                "17:00:00", "18:00:00", "19:00:00"
            ]):
                hora_celda = datetime.strptime(hora, "%H:%M:%S").time()
                item = self.tableWidgetSemana.item(hora_index, dia)
                if fecha_celda >= fecha_actual and (fecha_celda > fecha_actual or hora_celda > hora_actual):
                    if item is None or not item.text():
                        horas_disponibles += 1

        self.labelHorasDisponibles.setText(f"Horas disponibles en la semana: {horas_disponibles}")

    def hora_a_indice(self, hora):
        horas = [
            "07:00:00", "08:00:00", "09:00:00", "10:00:00", "11:00:00",
            "12:00:00", "13:00:00", "14:00:00", "15:00:00", "16:00:00",
            "17:00:00", "18:00:00", "19:00:00"
        ]
        try:
            return horas.index(hora)
        except ValueError:
            return -1

    def mostrarSiguienteSemana(self):
        self.inicio_semana += timedelta(weeks=1)
        self.actualizarFechas(ajustar_inicio=False)  # No ajustar la vista inicial

    def mostrarSemanaAnterior(self):
        self.inicio_semana -= timedelta(weeks=1)
        self.actualizarFechas(ajustar_inicio=False)  # No ajustar la vista inicial

if __name__ == "__main__":
    app = QApplication([])
    window = SemanaApp()
    window.show()
    app.exec_()