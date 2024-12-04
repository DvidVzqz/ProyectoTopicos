from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector


def crear_cita_clinica(nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, fecha_cita, hora_cita):
    conn = conectar()
    cursor = conn.cursor()
    try:
        # Verificar disponibilidad de la hora para estudios clínicos
        cursor.execute("""
            SELECT 1 
            FROM citas_clinicas 
            WHERE fecha_cita = %s AND hora_cita = %s
        """, (fecha_cita, hora_cita))
        if cursor.fetchone():
            print(f"Error: Ya existe una cita registrada en esa fecha y hora.")
            return False

        # Insertar la cita
        cursor.execute("""
            INSERT INTO citas_clinicas (nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, fecha_cita, hora_cita)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, fecha_cita, hora_cita))
        conn.commit()
        print("Cita registrada exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al registrar cita:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_citas_clinicas(tabla_citas):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            SELECT id_cita, nombre_paciente, apellido_paciente, telefono_paciente, tipo_estudio, fecha_cita, hora_cita 
            FROM citas_clinicas
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


def actualizar_cita_clinica(id_cita, nombre_paciente=None, apellido_paciente=None, telefono_paciente=None, tipo_estudio=None, fecha_cita=None, hora_cita=None):
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
            UPDATE citas_clinicas
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


def eliminar_cita_clinica(id_cita):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM citas_clinicas WHERE id_cita = %s", (id_cita,))
        conn.commit()
        print("Cita eliminada exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar cita:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def obtener_horas_disponibles(fecha_cita, tabla_horarios):
    conn = conectar()
    cursor = conn.cursor()
    try:
        # Consultar horas ya ocupadas
        cursor.execute("""
            SELECT hora_cita 
            FROM citas_clinicas 
            WHERE fecha_cita = %s
        """, (fecha_cita,))
        horas_ocupadas = {row[0] for row in cursor.fetchall()}

        # Definir todas las horas disponibles en un día
        todas_las_horas = [f"{hora:02}:00:00" for hora in range(8, 18)]  # Horario: 8 AM a 5 PM
        horas_disponibles = [hora for hora in todas_las_horas if hora not in horas_ocupadas]

        tabla_horarios.setRowCount(len(horas_disponibles))
        tabla_horarios.setColumnCount(1)
        tabla_horarios.setHorizontalHeaderLabels(["Hora Disponible"])

        for row_idx, hora in enumerate(horas_disponibles):
            tabla_horarios.setItem(row_idx, 0, QtWidgets.QTableWidgetItem(hora))

    except mysql.connector.Error as err:
        print("Error al obtener horas disponibles:", err)
    finally:
        cursor.close()
        conn.close()
