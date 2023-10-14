import tkinter as tk
from tkinter import messagebox

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
    
    def check_empty_fields():
        if not nombre_entry.get() or not monto_entry.get():
            return False
        return True

    def registrar_gasto():
        if not check_empty_fields():
            messagebox.showerror("Error", "Por favor complete todos los campos.")
            return

        nombre = nombre_entry.get()
        monto = monto_entry.get()
        # Aquí puedes implementar la lógica para registrar el gasto en tu aplicación

        messagebox.showinfo("Gasto registrado", f"Se registró un gasto de {monto} en {nombre}")

    registrar_button = tk.Button(ventana_registro, text="Registrar", command=registrar_gasto)
    registrar_button.pack(pady=20)

    if not check_empty_fields():
        registrar_button.config(state="disabled")

    def on_change(event):
        if check_empty_fields():
            registrar_button.config(state="normal")
        else:
            registrar_button.config(state="disabled")

    nombre_entry.bind("<KeyRelease>", on_change)
    monto_entry.bind("<KeyRelease>", on_change)


# Función para abrir la pantalla de resumen de gastos
def abrir_resumen():
    ventana_principal.destroy()

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Gastos")
ventana_principal.geometry("500x400")
ventana_principal.configure(bg="black")

# Crear etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana_principal, text="Bienvenido a la Calculadora de Gastos", width=400, height=3, bg="gray", font=("Segoe Script", 15), relief=tk.RAISED)
etiqueta_bienvenida.pack(pady=20)

# Crear botones para registrar gastos y ver resumen con bordes redondos

boton_registrar_gasto = tk.Button(ventana_principal, text="Registrar Gasto ->", compound="center", command=crear_ventana_registro, width=200, height=3, bg="blue", fg="white", font=("Arial", 12), relief=tk.RAISED)
boton_ver_resumen = tk.Button(ventana_principal, text="Ver Resumen ->", compound="center", command=abrir_resumen, width=200, height=3, bg="blue", fg="white", font=("Arial", 12), relief=tk.RAISED)

boton_registrar_gasto.pack(pady=30)
boton_ver_resumen.pack()

# Iniciar la aplicación
ventana_principal.mainloop()
