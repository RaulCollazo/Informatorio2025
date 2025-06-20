import tkinter as tk

def progreso(root):
    ventana = tk.Toplevel(root)
    ventana.title("Seguimiento de Progreso")
    ventana.geometry("300x200")

    tk.Label(ventana, text="Progreso de Estudio", font=("Arial", 14)).pack(pady=10)
    barra = tk.DoubleVar()
    progreso = tk.Scale(ventana, from_=0, to=100, orient=tk.HORIZONTAL, variable=barra, length=250)
    progreso.pack(pady=20)

    porcentaje = tk.Label(ventana, text="0%")
    porcentaje.pack()

    def actualizar(val):
        porcentaje.config(text=f"{barra.get():.0f}%")

    progreso.config(command=actualizar)