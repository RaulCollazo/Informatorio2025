import tkinter as tk
from config import COLOR_FONDO, COLOR_LISTA_FONDO, FUENTE_TEXTO, FUENTE_TITULO

class ListaRegistros:
    def __init__(self, parent, tipo):
        self.parent = parent
        self.tipo = tipo

        marco = tk.Frame(self.parent, bg=COLOR_FONDO)
        marco.pack(side=tk.LEFT, fill='both', expand=True, padx=5)

        self.label = tk.Label(marco, text=f"{tipo} registrados:", font=FUENTE_TITULO, bg=COLOR_FONDO)
        self.label.pack(anchor='w', padx=5)

        frame_con_scroll = tk.Frame(marco)
        frame_con_scroll.pack(fill='both', expand=True)

        self.scrollbar = tk.Scrollbar(frame_con_scroll)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lista = tk.Listbox(frame_con_scroll, yscrollcommand=self.scrollbar.set,
                                bg=COLOR_LISTA_FONDO, font=FUENTE_TEXTO, height=10)
        self.lista.pack(side=tk.LEFT, fill='both', expand=True)

        self.scrollbar.config(command=self.lista.yview)

    def agregar_registro(self, nombre, fecha_hora):
        self.lista.insert(tk.END, f"{nombre} - {fecha_hora}")