import tkinter as tk

def notas_rapidas(root):
    ventana = tk.Toplevel(root)
    ventana.title("Notas Rápidas")
    ventana.geometry("400x300")

    texto = tk.Text(ventana, wrap=tk.WORD, font=("Arial", 12))
    texto.pack(fill=tk.BOTH, expand=True)