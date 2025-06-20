import tkinter as tk

def biblioteca(root):
    ventana = tk.Toplevel(root)
    ventana.title("Biblioteca de Recursos")
    ventana.geometry("400x300")

    tk.Label(ventana, text="Recursos guardados", font=("Arial", 14)).pack(pady=10)

    lista = tk.Listbox(ventana)
    lista.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    recursos = [
        "📘 Guía de Python.pdf",
        "🔗 https://docs.python.org",
        "📄 Notas de clase.txt",
        "📺 Tutorial YouTube - POO"
    ]

    for r in recursos:
        lista.insert(tk.END, r)