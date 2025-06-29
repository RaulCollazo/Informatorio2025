<<<<<<< HEAD
import tkinter as tk
from tkinter import messagebox
import os

def abrir_ventana_flashcard(parent, on_close_callback=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    FLASHCARD_FILE = os.path.join(script_dir, "flashcards.txt")
    flashcards = []
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 2:
                    flashcards.append({"pregunta": partes[0].strip(), "respuesta": partes[1].strip()})
    else:
        messagebox.showerror("Archivo no encontrado", f"No se encontró el archivo: {FLASHCARD_FILE}")
        if on_close_callback:
            on_close_callback()
        return None

    if not flashcards:
        messagebox.showerror("Sin datos", "El archivo de flashcards no contiene preguntas y respuestas válidas.")
        if on_close_callback:
            on_close_callback()
        return None

    win = tk.Toplevel(parent)
    win.title("Flashcards")
    win.geometry("400x250")
    win.resizable(False, False)

    idx = {"val": 0}
    mostrando_respuesta = {"val": False}

    pregunta_label = tk.Label(win, text=flashcards[0]["pregunta"], font=("Arial", 16), wraplength=380, justify="center")
    pregunta_label.pack(pady=20, padx=10, fill=tk.X)

    respuesta_label = tk.Label(win, text="", font=("Arial", 15, "italic"), fg="gray30", wraplength=380, justify="center")
    respuesta_label.pack(pady=5, padx=10, fill=tk.X)

    def mostrar_pregunta():
        mostrando_respuesta["val"] = False
        pregunta_label.config(text=flashcards[idx["val"]]["pregunta"])
        respuesta_label.config(text="")
        btn_mostrar.config(text="Mostrar respuesta")

    def mostrar_respuesta():
        mostrando_respuesta["val"] = True
        respuesta_label.config(text=flashcards[idx["val"]]["respuesta"])
        btn_mostrar.config(text="Ocultar respuesta")

    def toggle_respuesta():
        if mostrando_respuesta["val"]:
            mostrar_pregunta()
        else:
            mostrar_respuesta()

    def siguiente():
        idx["val"] = (idx["val"] + 1) % len(flashcards)
        mostrar_pregunta()

    def anterior():
        idx["val"] = (idx["val"] - 1) % len(flashcards)
        mostrar_pregunta()

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    btn_anterior = tk.Button(btn_frame, text="Anterior", width=10, command=anterior)
    btn_anterior.pack(side=tk.LEFT, padx=5)
    btn_mostrar = tk.Button(btn_frame, text="Mostrar respuesta", width=16, command=toggle_respuesta)
    btn_mostrar.pack(side=tk.LEFT, padx=5)
    btn_siguiente = tk.Button(btn_frame, text="Siguiente", width=10, command=siguiente)
    btn_siguiente.pack(side=tk.LEFT, padx=5)

    def on_close():
        if on_close_callback:
            on_close_callback()
        win.destroy()
    win.protocol("WM_DELETE_WINDOW", on_close)

    mostrar_pregunta()
=======
import tkinter as tk
from tkinter import messagebox
import os

def abrir_ventana_flashcard(parent, on_close_callback=None):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    FLASHCARD_FILE = os.path.join(script_dir, "flashcards.txt")
    flashcards = []
    if os.path.exists(FLASHCARD_FILE):
        with open(FLASHCARD_FILE, "r", encoding="utf-8") as f:
            for linea in f:
                partes = linea.strip().split("|")
                if len(partes) == 2:
                    flashcards.append({"pregunta": partes[0].strip(), "respuesta": partes[1].strip()})
    else:
        messagebox.showerror("Archivo no encontrado", f"No se encontró el archivo: {FLASHCARD_FILE}")
        if on_close_callback:
            on_close_callback()
        return None

    if not flashcards:
        messagebox.showerror("Sin datos", "El archivo de flashcards no contiene preguntas y respuestas válidas.")
        if on_close_callback:
            on_close_callback()
        return None

    win = tk.Toplevel(parent)
    win.title("Flashcards")
    win.geometry("400x250")
    win.resizable(False, False)

    idx = {"val": 0}
    mostrando_respuesta = {"val": False}

    pregunta_label = tk.Label(win, text=flashcards[0]["pregunta"], font=("Arial", 16), wraplength=380, justify="center")
    pregunta_label.pack(pady=20, padx=10, fill=tk.X)

    respuesta_label = tk.Label(win, text="", font=("Arial", 15, "italic"), fg="gray30", wraplength=380, justify="center")
    respuesta_label.pack(pady=5, padx=10, fill=tk.X)

    def mostrar_pregunta():
        mostrando_respuesta["val"] = False
        pregunta_label.config(text=flashcards[idx["val"]]["pregunta"])
        respuesta_label.config(text="")
        btn_mostrar.config(text="Mostrar respuesta")

    def mostrar_respuesta():
        mostrando_respuesta["val"] = True
        respuesta_label.config(text=flashcards[idx["val"]]["respuesta"])
        btn_mostrar.config(text="Ocultar respuesta")

    def toggle_respuesta():
        if mostrando_respuesta["val"]:
            mostrar_pregunta()
        else:
            mostrar_respuesta()

    def siguiente():
        idx["val"] = (idx["val"] + 1) % len(flashcards)
        mostrar_pregunta()

    def anterior():
        idx["val"] = (idx["val"] - 1) % len(flashcards)
        mostrar_pregunta()

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=10)

    btn_anterior = tk.Button(btn_frame, text="Anterior", width=10, command=anterior)
    btn_anterior.pack(side=tk.LEFT, padx=5)
    btn_mostrar = tk.Button(btn_frame, text="Mostrar respuesta", width=16, command=toggle_respuesta)
    btn_mostrar.pack(side=tk.LEFT, padx=5)
    btn_siguiente = tk.Button(btn_frame, text="Siguiente", width=10, command=siguiente)
    btn_siguiente.pack(side=tk.LEFT, padx=5)

    def on_close():
        if on_close_callback:
            on_close_callback()
        win.destroy()
    win.protocol("WM_DELETE_WINDOW", on_close)

    mostrar_pregunta()
>>>>>>> 0425495 (último commit)
    return win