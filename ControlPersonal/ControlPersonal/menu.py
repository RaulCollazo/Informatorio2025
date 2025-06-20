import tkinter as tk

class MenuPrincipal:
    def __init__(self, app):
        self.app = app

    def crear_menu(self):
        barra_menu = tk.Menu(self.app.root)
        self.app.root.config(menu=barra_menu)

        menu_principal = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Opciones", menu=menu_principal)
        menu_principal.add_command(label="Registrar Ingreso", command=lambda: self.app.registrar("Ingreso"))
        menu_principal.add_command(label="Registrar Salida", command=lambda: self.app.registrar("Salida"))
        menu_principal.add_separator()
        menu_principal.add_command(label="Salir", command=self.app.root.quit)