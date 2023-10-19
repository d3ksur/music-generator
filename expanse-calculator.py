import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

gastos = {}

# Crear la ventana de registro de gasto
def crear_ventana_registro():
    ventana_registro = tk.Toplevel(ventana_principal)
    ventana_registro.title("Registrar Nuevo Gasto")
    ventana_registro.geometry("300x250")
    ventana_registro.configure(bg="black")

    # Elementos de la interfaz de usuario para el registro de gastos
    nombre_label = tk.Label(ventana_registro, text="Nombre del gasto:", bg="gray", font=("Segoe Script", 10), relief=tk.RAISED)
    nombre_label.pack(pady=10)
    nombre_entry = tk.Entry(ventana_registro)
    nombre_entry.pack(pady=5)

    def validate_input(new_text):
        if not new_text:
            return True
        try:
            float(new_text)
            return True
        except ValueError:
            return False

    validation = ventana_registro.register(validate_input)
    monto_label = tk.Label(ventana_registro, text="Monto del gasto:", bg="gray", font=("Segoe Script", 10), relief=tk.RAISED)
    monto_label.pack(pady=10)
    monto_entry = tk.Entry(ventana_registro, validate="key", validatecommand=(validation, '%P'))
    monto_entry.pack(pady=5)

    #Funcion que controla que los entries esten completos.
    def check_empty_fields():
        if not nombre_entry.get() or not monto_entry.get():
            return False
        return True

    #Funcion para registrar el gasto en el array de objetos y ademas usa la funcion check_empty_fields.
    def registrar_gasto():
        if not check_empty_fields():
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        nombre = nombre_entry.get()
        monto = float(monto_entry.get())

        if nombre in gastos:
            gastos[nombre].append(monto)
        else:
            gastos[nombre] = [monto]

        messagebox.showinfo("Gasto registrado", f"Se registró un gasto de {monto} en {nombre}")

    registrar_button = tk.Button(ventana_registro, text="Registrar", command=registrar_gasto)
    registrar_button.pack(pady=20)

    if not check_empty_fields():
        registrar_button.config(state="disabled")

    #Funcion que desactiva el boton de regsitrar si los entries no estan completos.
    def on_change(event):
        if check_empty_fields():
            registrar_button.config(state="normal")
        else:
            registrar_button.config(state="disabled")

    nombre_entry.bind("<KeyRelease>", on_change)
    monto_entry.bind("<KeyRelease>", on_change)

#Funcion para crear el grafico con los datos guardados.
def update_graph():
    nombres = list(gastos.keys())
    montos = [sum(gastos[nombre]) for nombre in nombres]

    plt.figure(figsize=(6, 4))
    plt.bar(nombres, montos, color='skyblue')
    plt.xlabel('Gastos')
    plt.ylabel('Monto total')
    plt.title('Gastos Registrados')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Función para abrir la pantalla de resumen de gastos
def abrir_resumen():
    update_graph()

#Crear la ventana principal.
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Gastos")
ventana_principal.geometry("500x400")
ventana_principal.configure(bg="black")
ventana_principal.iconbitmap('icons8-calculator-16.ico')

etiqueta_bienvenida = tk.Label(ventana_principal, text="Bienvenido a la Calculadora de Gastos", width=400, height=3, bg="gray", font=("Segoe Script", 15), relief=tk.RAISED)
etiqueta_bienvenida.pack(pady=20)


boton_registrar_gasto = tk.Button(ventana_principal, text="Registrar Gasto ->", compound="center", command=crear_ventana_registro, width=200, height=3, bg="blue", fg="white", font=("Arial", 12), relief=tk.RAISED)
boton_ver_resumen = tk.Button(ventana_principal, text="Ver Resumen ->", compound="center", command=abrir_resumen, width=200, height=3, bg="blue", fg="white", font=("Arial", 12), relief=tk.RAISED)

boton_registrar_gasto.pack(pady=30)
boton_ver_resumen.pack()

ventana_principal.mainloop()