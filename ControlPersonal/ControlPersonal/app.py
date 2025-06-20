import tkinter as tk
from datetime import datetime
from menu import MenuPrincipal
from registro import RegistroPersonal
from lista_registros import ListaRegistros
from config import COLOR_FONDO

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Ingreso y Salida de Personal")
        self.root.geometry("600x500")
        self.root.configure(bg=COLOR_FONDO)

        self.registro = RegistroPersonal(self)
        self.menu = MenuPrincipal(self)
        self.menu.crear_menu()

        self.mostrar_reloj()

        self.frame_listas = tk.Frame(self.root, bg=COLOR_FONDO)
        self.frame_listas.pack(fill='both', expand=True, padx=10, pady=10)

        self.lista_ingresos = ListaRegistros(self.frame_listas, "Ingresos")
        self.lista_salidas = ListaRegistros(self.frame_listas, "Salidas")

    def mostrar_reloj(self):
        reloj = tk.Label(self.root, font=('Segoe UI', 14), fg='blue', bg=COLOR_FONDO)
        reloj.pack(pady=5)
        self.actualizar_reloj(reloj)

    def actualizar_reloj(self, label):
        fecha_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        label.config(text="Fecha y hora actual: " + fecha_hora)
        self.root.after(1000, lambda: self.actualizar_reloj(label))

    def registrar(self, tipo):
        self.registro.abrir_ventana(tipo)