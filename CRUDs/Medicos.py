from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector

def crear_medico(nombre, apellido, especialidad, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO medicos (nombre, apellido, especialidad, telefono, email)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellido, especialidad, telefono, email))
        conn.commit()
        print("Medico creado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al crear medico:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_medico(tabla_medicos):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM medicos")
        resultados = cursor.fetchall()

        tabla_medicos.setRowCount(len(resultados))
        tabla_medicos.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_medicos.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])


        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_medicos.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al leer medicos:", err)
    finally:
        cursor.close()
        conn.close()


def actualizar_medico(id_medico, nombre=None, apellido=None, especialidad=None, telefono=None, email=None):
    conn = conectar()
    cursor = conn.cursor()
    try:
        campos = []
        valores = []
        if nombre:
            campos.append("nombre = %s")
            valores.append(nombre)
        if apellido:
            campos.append("apellido = %s")
            valores.append(apellido)
        if especialidad:
            campos.append("especialidad = %s")
            valores.append(especialidad)
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if email:
            campos.append("email = %s")
            valores.append(email)
        valores.append(id_medico)

        cursor.execute(f"""
            UPDATE medicos
            SET {", ".join(campos)}
            WHERE id_medico = %s
        """, valores)
        conn.commit()
        print("Medico actualizado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al actualizar medico:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def eliminar_medico(id_medico):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM medicos WHERE id_medico = %s", (id_medico))
        conn.commit()
        print("Medico eliminado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar medico:", err)
        return False
    finally:
        cursor.close()
        conn.close()
