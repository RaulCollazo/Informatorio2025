
import tkinter as tk
from gestor_tareas import gestor_tareas
from calculadora_modular import mostrar_calculadora

class MenuPrincipal:
    def __init__(self, app):
        self.app = app  # Puede ser la ventana root directamente

    def crear_menu(self):
        barra_menu = tk.Menu(self.app)
        self.app.config(menu=barra_menu)

        # Menú principal
        menu_principal = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Opciones", menu=menu_principal)
        menu_principal.add_command(label="Registrar Ingreso", command=lambda: self.app.registrar("Ingreso"))
        menu_principal.add_command(label="Registrar Salida", command=lambda: self.app.registrar("Salida"))
        menu_principal.add_separator()
        menu_principal.add_command(label="Salir", command=self.app.quit)


        # Menú de tareas
        menu_tareas = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Tareas", menu=menu_tareas)
        menu_tareas.add_command(label="Gestor de Tareas", command=gestor_tareas)

        # Menú de herramientas
        menu_herramientas = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Herramientas", menu=menu_herramientas)
        menu_herramientas.add_command(label="Calculadora", command=mostrar_calculadora)
