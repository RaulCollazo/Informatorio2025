
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from config import COLOR_FONDO, COLOR_BOTON, COLOR_BOTON_TEXTO, COLOR_TEXTO_GENERAL, COLOR_LISTA_FONDO, FUENTE_TEXTO

class RegistroPersonal:
    def __init__(self, app):
        self.app = app

    def abrir_ventana(self, tipo):
        self.ventana = tk.Toplevel(self.app.root)
        self.ventana.title(f"Registrar {tipo}")
        self.ventana.geometry("350x200")
        self.ventana.config(bg=COLOR_FONDO)
        self.ventana.transient(self.app.root)
        self.ventana.grab_set()
        

        label = tk.Label(self.ventana, text=f"Ingrese nombre del personal para {tipo.lower()}", font=FUENTE_TEXTO, bg=COLOR_FONDO, fg=COLOR_TEXTO_GENERAL)
        label.pack(pady=10)

        self.nombre = tk.Entry(self.ventana, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, insertbackground=COLOR_TEXTO_GENERAL)
        self.nombre.pack(pady=5, padx=20, fill=tk.X)
        self.nombre.focus_set()

        boton = tk.Button(self.ventana, text="Registrar", command=lambda: self.registrar(tipo), bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO)
        boton.pack(pady=10)

        self.app.root.wait_window(self.ventana)

    def registrar(self, tipo):
        nombre = self.nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Campo vacío", "Por favor ingresá un nombre.")
            return

        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if tipo == "Ingreso":
            self.app.lista_ingresos.agregar_registro(nombre, fecha_hora)
        elif tipo == "Salida":
            self.app.lista_salidas.agregar_registro(nombre, fecha_hora)

        messagebox.showinfo("Éxito", f"{tipo} registrado correctamente.")
        self.ventana.destroy()
