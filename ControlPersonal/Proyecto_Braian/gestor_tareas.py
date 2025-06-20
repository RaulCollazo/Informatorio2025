import tkinter as tk
from tkinter import messagebox

def gestor_tareas(root):
    ventana = tk.Toplevel(root)
    ventana.title("Gestor de Tareas")
    ventana.geometry("400x400")
    ventana.config(bg="#f8f8f8")

    def agregar():
        tarea = entrada.get().strip()
        if tarea:
            lista.insert(tk.END, f"📝 {tarea}")
            entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Vacío", "Escribe una tarea.")

    def eliminar():
        sel = lista.curselection()
        if sel:
            lista.delete(sel)

    def completar():
        sel = lista.curselection()
        if sel:
            tarea = lista.get(sel)
            if not tarea.startswith("✅"):
                lista.delete(sel)
                lista.insert(sel, tarea.replace("📝", "✅"))

    entrada = tk.Entry(ventana, font=("Arial", 12))
    entrada.pack(pady=10, padx=10, fill=tk.X)

    btn_frame = tk.Frame(ventana, bg="#f8f8f8")
    btn_frame.pack()

    tk.Button(btn_frame, text="Agregar", command=agregar, bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Eliminar", command=eliminar, bg="#f44336", fg="white").pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Completar", command=completar, bg="#2196f3", fg="white").pack(side=tk.LEFT, padx=5)

    lista = tk.Listbox(ventana, font=("Arial", 12), selectbackground="#cce5ff")
    lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)