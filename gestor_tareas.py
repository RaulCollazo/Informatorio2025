
import tkinter as tk
from tkinter import messagebox
from config import COLOR_FONDO, COLOR_LISTA_FONDO, COLOR_TEXTO_GENERAL, COLOR_BOTON, COLOR_BOTON_TEXTO, FUENTE_TEXTO

def gestor_tareas():
    ventana = tk.Toplevel()
    ventana.title("Gestor de Tareas")
    ventana.geometry("400x400")
    ventana.config(bg=COLOR_FONDO)

    def agregar():
        tarea = entrada.get().strip()
        if tarea:
            lista.insert(tk.END, f"📝 {tarea}")
            entrada.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Por favor escribí una tarea antes de agregar.")
            return

    def eliminar():
        sel = lista.curselection()
        if sel:
            lista.delete(sel)
        else:
            messagebox.showinfo("Sin selección", "Seleccioná una tarea para eliminar.")
            return

    def completar():
        sel = lista.curselection()
        if sel:
            tarea = lista.get(sel)
            if not tarea.startswith("✅"):
                lista.delete(sel)
                lista.insert(sel, tarea.replace("📝", "✅"))
        else:
            messagebox.showinfo("Sin selección", "Seleccioná una tarea para marcar como completada.")
            return

    entrada = tk.Entry(ventana, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, insertbackground=COLOR_TEXTO_GENERAL)
    entrada.pack(pady=10, padx=10, fill=tk.X)

    btn_frame = tk.Frame(ventana, bg=COLOR_FONDO)
    btn_frame.pack()

    tk.Button(btn_frame, text="Agregar", command=agregar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Eliminar", command=eliminar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO).pack(side=tk.LEFT, padx=5)
    tk.Button(btn_frame, text="Completar", command=completar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO).pack(side=tk.LEFT, padx=5)

    lista = tk.Listbox(ventana, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, selectbackground=COLOR_BOTON)
    lista.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


    ventana.transient(root)
    ventana
    # wait_window(ventana)
