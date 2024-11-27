import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host="localhost",
        user="tu_usuario",
        password="tu_contraseña",
        database="nombre_de_tu_base_de_datos"
    )
    return mydb