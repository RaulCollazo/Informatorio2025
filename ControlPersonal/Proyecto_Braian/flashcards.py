import tkinter as tk

def flashcards(root):
    ventana = tk.Toplevel(root)
    ventana.title("Creador de Flashcards")
    ventana.geometry("400x300")

    preguntas = []

    def guardar():
        q = pregunta.get()
        r = respuesta.get()
        if q and r:
            preguntas.append((q, r))
            pregunta.delete(0, tk.END)
            respuesta.delete(0, tk.END)
            mostrar.insert(tk.END, f"Q: {q} - A: {r}")

    tk.Label(ventana, text="Pregunta:").pack()
    pregunta = tk.Entry(ventana, width=40)
    pregunta.pack()

    tk.Label(ventana, text="Respuesta:").pack()
    respuesta = tk.Entry(ventana, width=40)
    respuesta.pack()

    tk.Button(ventana, text="Agregar Flashcard", command=guardar).pack(pady=10)

    mostrar = tk.Listbox(ventana, width=50)
    mostrar.pack(expand=True, fill=tk.BOTH)