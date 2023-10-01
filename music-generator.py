import tkinter as tk
import playsound as pSound

def reproducir_sonido():
    pSound("sonido.wav")

root = tk.Tk()

boton_reproducir = tk.Button(root, text="Reproducir", command=reproducir_sonido)
boton_reproducir.pack()

root.mainloop()
