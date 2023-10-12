import tkinter as tk

# Función para abrir la pantalla de registro de gastos
def abrir_registro():
    ventana_principal.destroy()  

# Función para abrir la pantalla de resumen de gastos
def abrir_resumen():
    ventana_principal.destroy()  

# Configuración de la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Gastos")
ventana_principal.geometry("500x400")
ventana_principal.configure(bg="orange")

# Crear etiqueta de bienvenida
etiqueta_bienvenida = tk.Label(ventana_principal, text="Bienvenido a la Calculadora de Gastos", width=400, height=3, bg="red", font=("Segoe Script", 15))
etiqueta_bienvenida.pack(pady=20)

#Crear botones para registrar gastos y ver resumen
boton_registrar_gasto = tk.Button(ventana_principal, text="Registrar Gasto", command=abrir_registro, width=20, height=3)
boton_ver_resumen = tk.Button(ventana_principal, text="Ver Resumen", command=abrir_resumen, width=20, height=3)

# Colocar los botones en la ventana principal
boton_registrar_gasto.pack(pady=30)
boton_ver_resumen.pack()

# Iniciar la aplicación
ventana_principal.mainloop()