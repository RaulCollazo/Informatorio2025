import tkinter as tk
from tkinter import messagebox
from config import COLOR_FONDO, COLOR_BOTON, COLOR_BOTON_TEXTO, FUENTE_TEXTO
from datetime import datetime

class RegistroPersonal:
    def __init__(self, app):
        self.app = app

    def abrir_ventana(self, tipo):
        ventana = tk.Toplevel(self.app.root)
        ventana.title(f"Registrar {tipo}")
        ventana.geometry("320x180")
        ventana.configure(bg=COLOR_FONDO)

        tk.Label(ventana, text=f"Ingrese nombre del personal para {tipo.lower()}",
                 bg=COLOR_FONDO, font=FUENTE_TEXTO).pack(pady=10)

        entrada_nombre = tk.Entry(ventana, font=FUENTE_TEXTO)
        entrada_nombre.pack(pady=5, ipadx=5, ipady=3)

        def registrar():
            nombre = entrada_nombre.get()
            fecha_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            if nombre:
                if tipo == "Ingreso":
                    self.app.lista_ingresos.agregar_registro(nombre, fecha_hora)
                else:
                    self.app.lista_salidas.agregar_registro(nombre, fecha_hora)
                ventana.destroy()
            else:
                messagebox.showwarning("Campo vacío", "Debe ingresar un nombre")

        boton = tk.Button(ventana, text="Registrar", command=registrar,
                          bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO)
        boton.pack(pady=10)