import mysql.connector
from tkinter import messagebox, Tk, Label, Entry, Button, Toplevel, END, HIDDEN
from tkinter import ttk
from tkinter import *
import tkinter as tk




def login():
    # Se obtienen los valores de entrada 
 

    username = entry_username.get()
    password = entry_password.get()

    # Establecer la conexión con la base de datos
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456789",
            database="biblioteca"
        )
        
    except mysql.connector.Error as e:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {e}")
        exit()

    # Verificar si la conexión fue exitosa
    if conn.is_connected():

        # Crear un cursor para realizar consultas
        cursor = conn.cursor()

        if entry_username == '' or entry_password == '':
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
        else:

           
            # Realizar la consulta para verificar las credenciales
            query = "SELECT * FROM usuarios WHERE nombre_user = %s AND password_user = %s"
            cursor.execute(query, (username, password))

            def limpiar_campos():
                entry_username.delete(0, END)
                entry_password.delete(0, END) 

            


            # Obtener los resultados de la consulta
            result = cursor.fetchone()

            if result:
                # Cerrar la ventana de inicio de sesión
                ventana.withdraw()
                limpiar_campos()
                

                # Abrir la ventana de préstamo de biblioteca
                ventana_prestamo = Toplevel()
                ventana_prestamo.title("Préstamo de Biblioteca")
                ventana_prestamo.geometry("300x390")
                ventana_prestamo.config(bg="silver")

                # Campos de entrada para los datos del préstamo

                #Campo 1
                label_nombre = Label(ventana_prestamo, text="Nombre:", bg="silver")
                label_nombre.grid(row=0, column=0, pady=10)
                entry_nombre = Entry(ventana_prestamo)
                entry_nombre.grid(row=0, column=1, pady=10)
                
                #Campo 2
                label_apellido = Label(ventana_prestamo, text="Apellido:", bg="silver")
                label_apellido.grid(row=1, column=0, pady=10)
                entry_apellido = Entry(ventana_prestamo)
                entry_apellido.grid(row=1, column=1, pady=10)

                #Campo 3
                label_edad = Label(ventana_prestamo, text="Edad:", bg="silver")
                label_edad.grid(row=2, column=0, pady=10)
                entry_edad = Entry(ventana_prestamo)
                entry_edad.grid(row=2, column=1, pady=10)
                
                #Campo 4
                label_telefono = Label(ventana_prestamo, text="Teléfono:", bg="silver")
                label_telefono.grid(row=3, column=0, pady=10)
                entry_telefono = Entry(ventana_prestamo)
                entry_telefono.grid(row=3, column=1, pady=10)

                #Campo 5
                label_semestre = Label(ventana_prestamo, text="Semestre:", bg="silver")
                label_semestre.grid(row=4, column=0, pady=10)
                entry_semestre = Entry(ventana_prestamo)
                entry_semestre.grid(row=4, column=1, pady=10)

                #Campo 6
                label_carrera = Label(ventana_prestamo, text="Carrera:", bg="silver")
                label_carrera.grid(row=5, column=0, pady=10)
                entry_carrera = Entry(ventana_prestamo)
                entry_carrera.grid(row=5, column=1, pady=10)

                #Campo 7
                label_libros = Label(ventana_prestamo, text="Libro a prestar:", bg="silver")
                label_libros.grid(row=6, column=0, pady=10)
                entry_libro = Entry(ventana_prestamo)
                entry_libro.grid(row=6, column=1, pady=10)

                #Campo 8
                label_fecha_de_dev = Label(ventana_prestamo, text="Fecha de devolución:", bg="silver")
                label_fecha_de_dev.grid(row=7, column=0, pady=10)
                entry_Fecha_reg = Entry(ventana_prestamo)
                entry_Fecha_reg.grid(row=7, column=1, pady=10)


                def Limpiar_campos():
        
                    entry_nombre.delete(0, END)
                    entry_apellido.delete(0, END)
                    entry_edad.delete(0, END)
                    entry_telefono.delete(0, END)
                    entry_semestre.delete(0, END)
                    entry_carrera.delete(0, END)
                    entry_libro.delete(0, END)
                    entry_Fecha_reg.delete(0, END)


                # Función para guardar el préstamo en la base de datos
                def guardar_prestamo():

                    # Obtiene los valores en los campos de entrada
                    nombre = entry_nombre.get()
                    apellido = entry_apellido.get()
                    edad = entry_edad.get()
                    semestre = entry_semestre.get()
                    telefono = entry_telefono.get()
                    carrera = entry_carrera.get()
                    libro = entry_libro.get()
                    fecha_dev = entry_Fecha_reg.get()


                    if conn.is_connected():
                        
                        cursor = conn.cursor()

                        # Verificar si los campos están vacíos
                        if nombre == '' or apellido == '' or edad == '' or semestre == '' or telefono == '' or carrera == '' or libro == '' or fecha_dev == '':
                            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")
                        else:
                            # Realizar la inserción en la base de datos
                            query = "INSERT INTO estudiantes (nombre, apellido, edad, semestre, telefono, carrera, libro, Fecha_dev) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                            values = (nombre, apellido, edad, semestre, telefono, carrera, libro, fecha_dev)
                            cursor.execute(query, values)

                            # Confirmar los cambios en la base de datos
                            conn.commit()

                            # Mostrar un mensaje de éxito
                            messagebox.showinfo("Préstamo guardado", "El préstamo se ha registrado correctamente.")
                            Limpiar_campos()
                    else:
                        
                        messagebox.showerror("Error de conexión", "No se pudo establecer conexión con la base de datos.")

                

                # Botón para guardar el préstamo
                button_guardar = Button(ventana_prestamo, text="Prestar libro", command=guardar_prestamo, bg="silver", fg="black", relief="raised", padx=10, pady=5)
                button_guardar.grid(column=0, row=12, padx=4, pady=3)

                def cerrar_venta_prestamo():

                    print()   

                def abrir_registros():
                    ventana_prestamo.withdraw()
                    ventana_registros = Toplevel()
                    ventana_registros.title("Registros de Libros")
                    ventana_registros.geometry("800x350")

                    # Obtener los registros de libros desde la base de datos
                    query = "SELECT * FROM libreria"
                    cursor.execute(query)
                    libros = cursor.fetchall()

                    # Crear una tabla para mostrar los registros de libros
                    tabla = ttk.Treeview(ventana_registros, columns=("ID", "Nombre", "Autor", "Disponible"), show="headings")
                    tabla.heading("ID", text="ID")
                    tabla.heading("Nombre", text="Nombre del libro")
                    tabla.heading("Autor", text="Autor")
                    tabla.heading("Disponible", text="Disponible")

                    # Configurar el estilo de la tabla
                    estilo = ttk.Style()
                    estilo.configure("Treeview", background="silver", foreground="black", font=("Arial", 10))

                    # Configurar el estilo de las cabeceras de la tabla
                    estilo.configure("Treeview.Heading", background="silver", foreground="black", font=("Arial", 10, "bold"))

                    # Insertar los registros de libros en la tabla
                    for libro in libros:
                        tabla.insert("", "end", values=libro)

                    tabla.pack(fill="both", expand=True)

                    def cerrar_ventana_registros():
                        ventana_prestamo.deiconify()  # Regresa a la ventana de prestamo
                        ventana_registros.withdraw()   # Ocultar la ventana de los registros 

                    button_regresar = Button(ventana_registros, text="Regresar", command=cerrar_ventana_registros, bg="silver", fg="black", relief="raised", padx=10, pady=5)
                    button_regresar.pack(side="bottom", pady=10)


                # Botón para abrir los registros de libros
                button_registros = Button(ventana_prestamo, text="Ver disponibilidad de libros", command=abrir_registros, bg="silver", fg="black", relief="raised", padx=10, pady=5)
                button_registros.grid(column=1, row=12, padx=5, pady=3)

            else:

                messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas.")
    else:
        messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos.")
            
    
 

# Crear la ventana del formulario principal
ventana = Tk()
ventana.title("Iniciar sesión")
ventana.geometry("400x300")
ventana.configure(bg="#f2f2f2")


# Agregar una imagen
imagen = BitmapImage(file="")  
label_imagen = Label(ventana, image=imagen, bg="#f2f2f2")
label_imagen.pack(pady=20)

# Agregar etiquetas y campos de entrada
label_usuario = Label(ventana,  text="Matricula:",  font=("Arial", 14), bg="#f2f2f2")
label_usuario.pack()
entry_username = Entry(ventana,  font=("Arial", 14))
entry_username.pack()

label_contrasena = Label(ventana, text="Contraseña:", font=("Arial", 14), bg="#f2f2f2")
label_contrasena.pack()
entry_password = Entry(ventana,  show="*", font=("Arial", 14))
entry_password.pack()

label_mayus = Label(ventana, text="", fg="red")
label_mayus.pack()

# Agregar botón de inicio de sesión
button_iniciar_sesion = Button(ventana, text="Iniciar Sesión", font=("Arial", 14), bg="#4caf50", fg="white" , command=login)
button_iniciar_sesion.pack(pady=20)

# Agregar etiqueta para mostrar el estado del inicio de sesión
label_estado = Label(ventana, text="", font=("Arial", 14), bg="#f2f2f2")
label_estado.pack()

ventana.mainloop()



