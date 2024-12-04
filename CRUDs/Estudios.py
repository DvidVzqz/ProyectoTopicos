from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector


def crear_cita(nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, medico_asignado, fecha_cita, hora_cita):
    conn = conectar()
    cursor = conn.cursor()
    try:
        # Verificar disponibilidad del médico
        cursor.execute("""
            SELECT 1 
            FROM citas 
            WHERE medico_asignado = %s AND fecha_cita = %s AND hora_cita = %s
        """, (medico_asignado, fecha_cita, hora_cita))
        if cursor.fetchone():
            print(f"Error: El médico '{medico_asignado}' no está disponible en esa fecha y hora.")
            return False

        # Insertar la cita
        cursor.execute("""
            INSERT INTO citas (nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, medico_asignado, fecha_cita, hora_cita)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, medico_asignado, fecha_cita, hora_cita))
        conn.commit()
        print("Cita registrada exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al registrar cita:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_citas(tabla_citas):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id_cita, nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, 
                   medico_asignado, fecha_cita, hora_cita 
            FROM citas
        """)
        resultados = cursor.fetchall()

        tabla_citas.setRowCount(len(resultados))
        tabla_citas.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_citas.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])

        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_citas.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al leer citas:", err)
    finally:
        cursor.close()
        conn.close()


def actualizar_cita(id_cita, nombre_paciente=None, apellido_paciente=None, telefono_paciente=None, tipo_estudio=None, fecha_cita=None, hora_cita=None):
    conn = conectar()
    cursor = conn.cursor()
    try:
        campos = []
        valores = []
        if nombre_paciente:
            campos.append("nombre_paciente = %s")
            valores.append(nombre_paciente)
        if apellido_paciente:
            campos.append("apellido_paciente = %s")
            valores.append(apellido_paciente)
        if telefono_paciente:
            campos.append("telefono_paciente = %s")
            valores.append(telefono_paciente)
        if tipo_estudio:
            campos.append("tipo_estudio = %s")
            valores.append(tipo_estudio)
        if fecha_cita:
            campos.append("fecha_cita = %s")
            valores.append(fecha_cita)
        if hora_cita:
            campos.append("hora_cita = %s")
            valores.append(hora_cita)
        valores.append(id_cita)

        cursor.execute(f"""
            UPDATE citas
            SET {", ".join(campos)}
            WHERE id_cita = %s
        """, valores)
        conn.commit()
        print("Cita actualizada exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al actualizar cita:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def eliminar_cita(id_cita):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM citas WHERE id_cita = %s", (id_cita,))
        conn.commit()
        print("Cita eliminada exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar cita:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def obtener_horarios_medico(medico_asignado, tabla_horarios):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT dia, hora_inicio, hora_fin 
            FROM horarios 
            WHERE medico_asignado = %s
        """, (medico_asignado,))
        resultados = cursor.fetchall()

        tabla_horarios.setRowCount(len(resultados))
        tabla_horarios.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_horarios.setHorizontalHeaderLabels(["Día", "Hora Inicio", "Hora Fin"])

        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_horarios.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al obtener horarios del médico:", err)
    finally:
        cursor.close()
        conn.close()
