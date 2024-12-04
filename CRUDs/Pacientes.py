from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector


def crear_paciente(nombre, apellido, fecha_nacimiento, sexo, telefono):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO pacientes (nombre, apellido, fecha_nacimiento, sexo, telefono)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellido, fecha_nacimiento, sexo, telefono))
        conn.commit()
        print("Paciente creado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al crear paciente:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_pacientes(tabla_pacientes):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM pacientes")
        resultados = cursor.fetchall()

        tabla_pacientes.setRowCount(len(resultados))
        tabla_pacientes.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_pacientes.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])


        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_pacientes.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al leer pacientes:", err)
    finally:
        cursor.close()
        conn.close()


def actualizar_paciente(id_paciente, nombre=None, apellido=None, fecha_nacimiento=None, sexo=None, telefono=None):
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
        if fecha_nacimiento:
            campos.append("fecha_nacimiento = %s")
            valores.append(fecha_nacimiento)
        if sexo:
            campos.append("sexo = %s")
            valores.append(sexo)
        if telefono:
            campos.append("telefono = %s")
            valores.append(telefono)
        valores.append(id_paciente)

        cursor.execute(f"""
            UPDATE pacientes
            SET {", ".join(campos)}
            WHERE id_paciente = %s
        """, valores)
        conn.commit()
        print("Paciente actualizado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al actualizar paciente:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def eliminar_paciente(id_paciente):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM pacientes WHERE id_paciente = %s", (id_paciente,))
        conn.commit()
        print("Paciente eliminado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar paciente:", err)
        return False
    finally:
        cursor.close()
        conn.close()
