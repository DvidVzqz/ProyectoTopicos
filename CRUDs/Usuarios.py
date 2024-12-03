from ..DB import conectar
# Crear un usuario
def crear_usuario(nombre, apellido, usuario, contraseña, rol):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO Usuarios (nombre, apellido, usuario, contraseña, rol)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, apellido, usuario, contraseña, rol))
        conn.commit()
        print("Usuario creado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al crear usuario:", err)
    finally:
        cursor.close()
        conn.close()

# Leer usuarios
def leer_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Usuarios")
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)
    except mysql.connector.Error as err:
        print("Error al leer usuarios:", err)
    finally:
        cursor.close()
        conn.close()
        
def leer_usuario_especifico(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM Usuarios WHERE id_usuario = %s", (id_usuario,))
        resultados = cursor.fetchall()
        for usuario in resultados:
            print(usuario)
    except mysql.connector.Error as err:
        print("Error al leer usuarios:", err)
    finally:
        cursor.close()
        conn.close()

# Actualizar un usuario
def actualizar_usuario(id_usuario, nombre=None, apellido=None, usuario=None, contraseña=None, rol=None):
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
        valores.append(id_usuario)

        cursor.execute(f"""
            UPDATE Usuarios
            SET {", ".join(campos)}
            WHERE id_usuario = %s
        """, valores)
        conn.commit()
        print("Usuario actualizado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al actualizar usuario:", err)
    finally:
        cursor.close()
        conn.close()

# Eliminar un usuario
def eliminar_usuario(id_usuario):
    conn = conectar()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Usuarios WHERE id_usuario = %s", (id_usuario,))
        conn.commit()
        print("Usuario eliminado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al eliminar usuario:", err)
    finally:
        cursor.close()
        conn.close()
