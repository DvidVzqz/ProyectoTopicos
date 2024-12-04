from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector

def crear_laboratorista(nombre, apellido, telefono, email):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO laboratoristas (nombre, apellido, telefono, email)
            VALUES (%s, %s, %s, %s)
        """, (nombre, apellido, telefono, email))
        conn.commit()
        print("Laboratorista creado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al crear laboratorista:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_laboratorista(tabla_laboratoristas):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM laboratoristas")
        resultados = cursor.fetchall()

        tabla_laboratoristas.setRowCount(len(resultados))
        tabla_laboratoristas.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_laboratoristas.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])


        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_laboratoristas.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al leer laboratoristas:", err)
    finally:
        cursor.close()
        conn.close()


def actualizar_laboratorista(id_laboratorista, nombre=None, apellido=None, telefono=None, email=None):
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
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        if email:
            campos.append("email = %s")
            valores.append(email)
        valores.append(id_laboratorista)

        cursor.execute(f"""
            UPDATE laboratoristas
            SET {", ".join(campos)}
            WHERE id_laboratorista = %s
        """, valores)
        conn.commit()
        print("Laboratorista actualizado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al actualizar laboratorista:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def eliminar_laboratorista(id_laboratorista):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM laboratoristas WHERE id_laboratorista = %s", (id_laboratorista))
        conn.commit()
        print("Laboratorista eliminado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar laboratorista:", err)
        return False
    finally:
        cursor.close()
        conn.close()
