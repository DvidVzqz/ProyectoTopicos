import tkinter as tk
from tkinter import messagebox
from ..DB import conectar  # Importa la función conectar

def login():
    usuario = usuario_entry.get()
    contrasena = contrasena_entry.get()

    mydb = conectar()  # Establece la conexión a la base de datos
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE usuario = %s AND contrasena = %s", (usuario, contrasena))
    user = cursor.fetchone()

    if user:
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso!")
        ventana.destroy()
        # Aquí puedes abrir la ventana principal o realizar otras acciones
    else:
        messagebox.showerror("Error", "Usuario o contraseña 

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Inicio de sesión")

# Crear etiquetas y campos de entrada
usuario_label = tk.Label(ventana, text="Usuario:")
usuario_label.pack()
usuario_entry = tk.Entry(ventana)
usuario_entry.pack()

contrasena_label = tk.Label(ventana, text="Contraseña:")
contrasena_label.pack()
contrasena_entry = tk.Entry(ventana, show="*") 1 
contrasena_entry.pack()

# Crear botón de inicio de sesión
login_button = tk.Button(ventana, text="Iniciar sesión", command=login)
login_button.pack()

ventana.mainloop()