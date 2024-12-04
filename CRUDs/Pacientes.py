from PyQt5 import QtWidgets
from DB import conectar
import mysql.connector


def crear_paciente(nombre, apellido, usuario, contraseña, rol, telefono):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT 1 FROM usuarios WHERE usuario = %s", (usuario,))
        if cursor.fetchone():
            print(f"Error: El usuario '{usuario}' ya existe.")
            return False
        
        cursor.execute("""
            INSERT INTO usuarios (nombre, apellido, usuario, contraseña, rol, telefono)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (nombre, apellido, usuario, contraseña, rol, telefono))
        conn.commit()
        print("Usuario creado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al crear usuario:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def leer_pacientes(tabla_users):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM usuarios")
        resultados = cursor.fetchall()

        tabla_users.setRowCount(len(resultados))
        tabla_users.setColumnCount(len(resultados[0]) if resultados else 0)
        tabla_users.setHorizontalHeaderLabels([desc[0] for desc in cursor.description])


        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                tabla_users.setItem(row_idx, col_idx, QtWidgets.QTableWidgetItem(str(col_data)))

    except mysql.connector.Error as err:
        print("Error al leer usuarios:", err)
    finally:
        cursor.close()
        conn.close()


def actualizar_paciente(id_usuario, nombre=None, apellido=None, usuario=None, contraseña=None, rol=None, telefono=None):
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
        if usuario:
            campos.append("usuario = %s")
            valores.append(usuario)
        if contraseña:
            campos.append("contraseña = %s")
            valores.append(contraseña)
        if rol:
            campos.append("rol = %s")
            valores.append(rol)
        if telefono:
            campos.append("telefono = %s")
            valores.append(contraseña)
        valores.append(id_usuario)

        cursor.execute(f"""
            UPDATE usuarios
            SET {", ".join(campos)}
            WHERE id_usuario = %s
        """, valores)
        conn.commit()
        print("Usuario actualizado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al actualizar usuario:", err)
        return False
    finally:
        cursor.close()
        conn.close()


def eliminar_paciente(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        print("Usuario eliminado exitosamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al eliminar usuario:", err)
        return False
    finally:
        cursor.close()
        conn.close()
