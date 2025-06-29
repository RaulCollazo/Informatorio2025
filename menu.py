<<<<<<< HEAD
import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from menu_tareas import MenuPrincipal
from gestor_tareas import gestor_tareas
from calculadora_modular import mostrar_calculadora
from temporizador import temporizador
from gestor_ingresos_egresos import gestor_ingresos_egresos
from graficos import abrir_grafico_ingresos_egresos
from flashcards import abrir_ventana_flashcard

# Obtener el directorio donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener tamaño de pantalla
root = tk.Tk()
ancho = int(root.winfo_screenwidth())
alto = int(root.winfo_screenheight())
root.destroy()

# Crear ventana principal
menu = tk.Tk()
menu.title("Productorium")
menu.geometry(f"{ancho}x{alto}")

# --- Agrega la barra de menú a la ventana principal ---
MenuPrincipal(menu).crear_menu()

# Rutas de las imágenes relativas al directorio del script
tarea0_path = os.path.join(script_dir, "img", "Tarea.png")
tarea1_path = os.path.join(script_dir, "img", "Tarea_Anim.png")

pomo0_path = os.path.join(script_dir, "img", "Pomo.png")
pomo1_path = os.path.join(script_dir, "img", "Pomo_Anim1.png")
pomo2_path = os.path.join(script_dir, "img", "Pomo_Anim2.png")
pomo3_path = os.path.join(script_dir, "img", "Pomo_Anim3.png")
pomo4_path = os.path.join(script_dir, "img", "Pomo_Anim4.png")
pomo5_path = os.path.join(script_dir, "img", "Pomo_Anim5.png")

pizarra0_path = os.path.join(script_dir, "img", "Pizarra.png")
pizarra1_path = os.path.join(script_dir, "img", "Pizarra_Anim.png")

flashcard0_path = os.path.join(script_dir, "img", "flashcard.png")
flashcard1_path = os.path.join(script_dir, "img", "flashcard_Anim.png")

# Cargar imágenes
tarea0_img = ImageTk.PhotoImage(Image.open(tarea0_path))
tarea1_img = ImageTk.PhotoImage(Image.open(tarea1_path))
frames_tarea = [tarea0_img, tarea1_img]

pomo0_img = ImageTk.PhotoImage(Image.open(pomo0_path))
pomo1_img = ImageTk.PhotoImage(Image.open(pomo1_path))
pomo2_img = ImageTk.PhotoImage(Image.open(pomo2_path))
pomo3_img = ImageTk.PhotoImage(Image.open(pomo3_path))
pomo4_img = ImageTk.PhotoImage(Image.open(pomo4_path))
pomo5_img = ImageTk.PhotoImage(Image.open(pomo5_path))
frames_pomo = [pomo0_img, pomo1_img, pomo2_img, pomo3_img, pomo4_img, pomo5_img]

pizarra0_img = ImageTk.PhotoImage(Image.open(pizarra0_path))
pizarra1_img = ImageTk.PhotoImage(Image.open(pizarra1_path))
frames_pizarra = [pizarra0_img, pizarra1_img]

flashcard0_img = ImageTk.PhotoImage(Image.open(flashcard0_path))
flashcard1_img = ImageTk.PhotoImage(Image.open(flashcard1_path))
frames_flashcard = [flashcard0_img, flashcard1_img]

# --- Animación Tarea ---
current_frame_tarea = [0]
animation_running_tarea = [False]
def animate_tarea():
    if animation_running_tarea[0]:
        current_frame_tarea[0] = (current_frame_tarea[0] + 1) % 2
        bTarea.config(image=frames_tarea[current_frame_tarea[0]])
        menu.after(200, animate_tarea)
def on_enter_tarea(e):
    if bTarea["state"] == "normal":
        animation_running_tarea[0] = True
        animate_tarea()
def on_leave_tarea(e):
    animation_running_tarea[0] = False
    bTarea.config(image=frames_tarea[0])

# --- Menú de selección al hacer click en Tareas ---
def mostrar_menu_tareas(parent):
    bTarea.config(state="disabled")
    ventana = tk.Toplevel(parent)
    ventana.title("Menú de Tareas")
    ventana.geometry("320x300")
    ventana.configure(bg="#2c3e50")
    ventana.transient(parent)
    ventana.attributes("-topmost", True)
    # NO usar grab_set()

    def close_menu():
        bTarea.config(state="normal")
        ventana.destroy()

    tk.Label(ventana, text="Elige una opción:", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=20)

    tk.Button(
        ventana, text="Gestor de Tareas", font=("Arial", 14), width=22,
        command=lambda: [gestor_tareas(parent), close_menu()]
    ).pack(pady=10)

    tk.Button(
        ventana, text="Gestor Ingresos/Egresos", font=("Arial", 14), width=22,
        command=lambda: [gestor_ingresos_egresos(parent), close_menu()]
    ).pack(pady=10)


    tk.Button(
        ventana, text="Gestor Ingresos/Egresos", font=("Arial", 14), width=22,
        command=lambda: [gestor_ingresos_egresos(parent), close_menu()]
    ).pack(pady=10)

    def abrir_calculadora():
        btn_calc.config(state="disabled")
        calc_open = {"ventana": None}
        def on_close():
            btn_calc.config(state="normal")
            if calc_open["ventana"]:
                calc_open["ventana"].destroy()
                calc_open["ventana"] = None
        import calculadora_modular
        orig_Toplevel = tk.Toplevel
        def fake_Toplevel(*args, **kwargs):
            if not calc_open["ventana"]:
                calc_open["ventana"] = orig_Toplevel(ventana)
                calc_open["ventana"].transient(menu)
                calc_open["ventana"].attributes("-topmost", True)
                calc_open["ventana"].protocol("WM_DELETE_WINDOW", on_close)
            return calc_open["ventana"]
        calculadora_modular.mostrar_calculadora.__globals__['tk'].Toplevel = fake_Toplevel
        calculadora_modular.mostrar_calculadora()
        calculadora_modular.mostrar_calculadora.__globals__['tk'].Toplevel = orig_Toplevel

    btn_calc = tk.Button(
        ventana, text="Calculadora", font=("Arial", 14), width=22,
        command=abrir_calculadora
    )
    btn_calc.pack(pady=10)

    tk.Button(
        ventana, text="Cerrar", font=("Arial", 12), width=10, command=close_menu
    ).pack(pady=20)

    ventana.protocol("WM_DELETE_WINDOW", close_menu)

# --- Botón Tarea como Button ---
bTarea = tk.Button(menu, image=frames_tarea[0], cursor="hand2", borderwidth=0, command=lambda: mostrar_menu_tareas(menu))
bTarea.place(relx=0.5, y=200, anchor="n", x=-450)
bTarea.bind("<Enter>", on_enter_tarea)
bTarea.bind("<Leave>", on_leave_tarea)

# --- Animación Pomo ---
current_frame_pomo = [0]
animation_running_pomo = [False]
def animate_pomo():
    if animation_running_pomo[0]:
        current_frame_pomo[0] = (current_frame_pomo[0] + 1) if current_frame_pomo[0] < 5 else 1
        bPomo.config(image=frames_pomo[current_frame_pomo[0]])
        menu.after(100, animate_pomo)
def on_enter_pomo(e):
    if bPomo['state'] == "normal":
        animation_running_pomo[0] = True
        current_frame_pomo[0] = 1
        animate_pomo()
def on_leave_pomo(e):
    if bPomo['state'] == "normal":
        animation_running_pomo[0] = False
        current_frame_pomo[0] = 0
        bPomo.config(image=frames_pomo[0])

def abrir_temporizador():
    temporizador(menu, on_close_temporizador)
    bPomo.config(state="disabled")

def on_close_temporizador():
    bPomo.config(state="normal")
    on_leave_pomo(None)

bPomo = tk.Button(menu, image=frames_pomo[0], cursor="hand2", command=abrir_temporizador, borderwidth=0)
bPomo.place(relx=0.5, y=200, anchor="n", x=+450)
bPomo.bind("<Enter>", on_enter_pomo)
bPomo.bind("<Leave>", on_leave_pomo)

# --- Animación Pizarra ---
current_frame_pizarra = [0]
animation_running_pizarra = [False]
def animate_pizarra():
    if animation_running_pizarra[0]:
        current_frame_pizarra[0] = (current_frame_pizarra[0] + 1) % 2
        bPizarra.config(image=frames_pizarra[current_frame_pizarra[0]])
        menu.after(200, animate_pizarra)
def on_enter_pizarra(e):
    if bPizarra["state"] == "normal":
        animation_running_pizarra[0] = True
        animate_pizarra()
def on_leave_pizarra(e):
    animation_running_pizarra[0] = False
    bPizarra.config(image=frames_pizarra[0])

# --- Botón Pizarra como Button ---
pizarra_window = {"ventana": None}
def abrir_pizarra():
    if pizarra_window["ventana"] is None or not pizarra_window["ventana"].winfo_exists():
        bPizarra.config(state="disabled")
        pizarra_window["ventana"] = abrir_grafico_ingresos_egresos(menu)
        def on_close():
            bPizarra.config(state="normal")
            if pizarra_window["ventana"]:
                pizarra_window["ventana"].destroy()
                pizarra_window["ventana"] = None
        if pizarra_window["ventana"]:
            pizarra_window["ventana"].protocol("WM_DELETE_WINDOW", on_close)
bPizarra = tk.Button(menu, image=frames_pizarra[0], cursor="hand2", borderwidth=0, command=abrir_pizarra)
bPizarra.place(relx=0.5, y=500, anchor="n", x=450)
bPizarra.bind("<Enter>", on_enter_pizarra)
bPizarra.bind("<Leave>", on_leave_pizarra)

# --- Animación Flashcard ---
current_frame_flashcard = [0]
animation_running_flashcard = [False]
def animate_flashcard():
    if animation_running_flashcard[0]:
        current_frame_flashcard[0] = (current_frame_flashcard[0] + 1) % 2
        bFlashcard.config(image=frames_flashcard[current_frame_flashcard[0]])
        menu.after(200, animate_flashcard)
def on_enter_flashcard(e):
    if bFlashcard["state"] == "normal":
        animation_running_flashcard[0] = True
        animate_flashcard()
def on_leave_flashcard(e):
    animation_running_flashcard[0] = False
    bFlashcard.config(image=frames_flashcard[0])

# --- Botón Flashcard modularizado ---
flashcard_window = {"ventana": None}
def abrir_flashcard_modular():
    if flashcard_window["ventana"] is None or not (flashcard_window["ventana"] and flashcard_window["ventana"].winfo_exists()):
        bFlashcard.config(state="disabled")
        # Llama a la ventana modular y pásale el parent y un callback para reactivar el botón
        def on_close():
            flashcard_window["ventana"] = None
            bFlashcard.config(state="normal")
        flashcard_window["ventana"] = abrir_ventana_flashcard(menu, on_close)

bFlashcard = tk.Button(menu, image=frames_flashcard[0], cursor="hand2", borderwidth=0, command=abrir_flashcard_modular)
bFlashcard.place(relx=0.5, y=500, anchor="n", x=-450)
bFlashcard.bind("<Enter>", on_enter_flashcard)
bFlashcard.bind("<Leave>", on_leave_flashcard)

=======
import os
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from menu_tareas import MenuPrincipal
from gestor_tareas import gestor_tareas
from calculadora_modular import mostrar_calculadora
from temporizador import temporizador
from gestor_ingresos_egresos import gestor_ingresos_egresos
from graficos import abrir_grafico_ingresos_egresos
from flashcards import abrir_ventana_flashcard

# Obtener el directorio donde se encuentra el script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtener tamaño de pantalla
root = tk.Tk()
ancho = int(root.winfo_screenwidth())
alto = int(root.winfo_screenheight())
root.destroy()

# Crear ventana principal
menu = tk.Tk()
menu.title("Productorium")
menu.geometry(f"{ancho}x{alto}")

# --- Agrega la barra de menú a la ventana principal ---
MenuPrincipal(menu).crear_menu()

# Rutas de las imágenes relativas al directorio del script
tarea0_path = os.path.join(script_dir, "img", "Tarea.png")
tarea1_path = os.path.join(script_dir, "img", "Tarea_Anim.png")

pomo0_path = os.path.join(script_dir, "img", "Pomo.png")
pomo1_path = os.path.join(script_dir, "img", "Pomo_Anim1.png")
pomo2_path = os.path.join(script_dir, "img", "Pomo_Anim2.png")
pomo3_path = os.path.join(script_dir, "img", "Pomo_Anim3.png")
pomo4_path = os.path.join(script_dir, "img", "Pomo_Anim4.png")
pomo5_path = os.path.join(script_dir, "img", "Pomo_Anim5.png")

pizarra0_path = os.path.join(script_dir, "img", "Pizarra.png")
pizarra1_path = os.path.join(script_dir, "img", "Pizarra_Anim.png")

flashcard0_path = os.path.join(script_dir, "img", "flashcard.png")
flashcard1_path = os.path.join(script_dir, "img", "flashcard_Anim.png")

# Cargar imágenes
tarea0_img = ImageTk.PhotoImage(Image.open(tarea0_path))
tarea1_img = ImageTk.PhotoImage(Image.open(tarea1_path))
frames_tarea = [tarea0_img, tarea1_img]

pomo0_img = ImageTk.PhotoImage(Image.open(pomo0_path))
pomo1_img = ImageTk.PhotoImage(Image.open(pomo1_path))
pomo2_img = ImageTk.PhotoImage(Image.open(pomo2_path))
pomo3_img = ImageTk.PhotoImage(Image.open(pomo3_path))
pomo4_img = ImageTk.PhotoImage(Image.open(pomo4_path))
pomo5_img = ImageTk.PhotoImage(Image.open(pomo5_path))
frames_pomo = [pomo0_img, pomo1_img, pomo2_img, pomo3_img, pomo4_img, pomo5_img]

pizarra0_img = ImageTk.PhotoImage(Image.open(pizarra0_path))
pizarra1_img = ImageTk.PhotoImage(Image.open(pizarra1_path))
frames_pizarra = [pizarra0_img, pizarra1_img]

flashcard0_img = ImageTk.PhotoImage(Image.open(flashcard0_path))
flashcard1_img = ImageTk.PhotoImage(Image.open(flashcard1_path))
frames_flashcard = [flashcard0_img, flashcard1_img]

# --- Animación Tarea ---
current_frame_tarea = [0]
animation_running_tarea = [False]
def animate_tarea():
    if animation_running_tarea[0]:
        current_frame_tarea[0] = (current_frame_tarea[0] + 1) % 2
        bTarea.config(image=frames_tarea[current_frame_tarea[0]])
        menu.after(200, animate_tarea)
def on_enter_tarea(e):
    if bTarea["state"] == "normal":
        animation_running_tarea[0] = True
        animate_tarea()
def on_leave_tarea(e):
    animation_running_tarea[0] = False
    bTarea.config(image=frames_tarea[0])

# --- Menú de selección al hacer click en Tareas ---
def mostrar_menu_tareas(parent):
    bTarea.config(state="disabled")
    ventana = tk.Toplevel(parent)
    ventana.title("Menú de Tareas")
    ventana.geometry("320x300")
    ventana.configure(bg="#2c3e50")
    ventana.transient(parent)
    ventana.attributes("-topmost", True)
    # NO usar grab_set()

    def close_menu():
        bTarea.config(state="normal")
        ventana.destroy()

    tk.Label(ventana, text="Elige una opción:", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50").pack(pady=20)

    tk.Button(
        ventana, text="Gestor de Tareas", font=("Arial", 14), width=22,
        command=lambda: [gestor_tareas(parent), close_menu()]
    ).pack(pady=10)

    tk.Button(
        ventana, text="Gestor Ingresos/Egresos", font=("Arial", 14), width=22,
        command=lambda: [gestor_ingresos_egresos(parent), close_menu()]
    ).pack(pady=10)


    tk.Button(
        ventana, text="Gestor Ingresos/Egresos", font=("Arial", 14), width=22,
        command=lambda: [gestor_ingresos_egresos(parent), close_menu()]
    ).pack(pady=10)

    def abrir_calculadora():
        btn_calc.config(state="disabled")
        calc_open = {"ventana": None}
        def on_close():
            btn_calc.config(state="normal")
            if calc_open["ventana"]:
                calc_open["ventana"].destroy()
                calc_open["ventana"] = None
        import calculadora_modular
        orig_Toplevel = tk.Toplevel
        def fake_Toplevel(*args, **kwargs):
            if not calc_open["ventana"]:
                calc_open["ventana"] = orig_Toplevel(ventana)
                calc_open["ventana"].transient(menu)
                calc_open["ventana"].attributes("-topmost", True)
                calc_open["ventana"].protocol("WM_DELETE_WINDOW", on_close)
            return calc_open["ventana"]
        calculadora_modular.mostrar_calculadora.__globals__['tk'].Toplevel = fake_Toplevel
        calculadora_modular.mostrar_calculadora()
        calculadora_modular.mostrar_calculadora.__globals__['tk'].Toplevel = orig_Toplevel

    btn_calc = tk.Button(
        ventana, text="Calculadora", font=("Arial", 14), width=22,
        command=abrir_calculadora
    )
    btn_calc.pack(pady=10)

    tk.Button(
        ventana, text="Cerrar", font=("Arial", 12), width=10, command=close_menu
    ).pack(pady=20)

    ventana.protocol("WM_DELETE_WINDOW", close_menu)

# --- Botón Tarea como Button ---
bTarea = tk.Button(menu, image=frames_tarea[0], cursor="hand2", borderwidth=0, command=lambda: mostrar_menu_tareas(menu))
bTarea.place(relx=0.5, y=200, anchor="n", x=-450)
bTarea.bind("<Enter>", on_enter_tarea)
bTarea.bind("<Leave>", on_leave_tarea)

# --- Animación Pomo ---
current_frame_pomo = [0]
animation_running_pomo = [False]
def animate_pomo():
    if animation_running_pomo[0]:
        current_frame_pomo[0] = (current_frame_pomo[0] + 1) if current_frame_pomo[0] < 5 else 1
        bPomo.config(image=frames_pomo[current_frame_pomo[0]])
        menu.after(100, animate_pomo)
def on_enter_pomo(e):
    if bPomo['state'] == "normal":
        animation_running_pomo[0] = True
        current_frame_pomo[0] = 1
        animate_pomo()
def on_leave_pomo(e):
    if bPomo['state'] == "normal":
        animation_running_pomo[0] = False
        current_frame_pomo[0] = 0
        bPomo.config(image=frames_pomo[0])

def abrir_temporizador():
    temporizador(menu, on_close_temporizador)
    bPomo.config(state="disabled")

def on_close_temporizador():
    bPomo.config(state="normal")
    on_leave_pomo(None)

bPomo = tk.Button(menu, image=frames_pomo[0], cursor="hand2", command=abrir_temporizador, borderwidth=0)
bPomo.place(relx=0.5, y=200, anchor="n", x=+450)
bPomo.bind("<Enter>", on_enter_pomo)
bPomo.bind("<Leave>", on_leave_pomo)

# --- Animación Pizarra ---
current_frame_pizarra = [0]
animation_running_pizarra = [False]
def animate_pizarra():
    if animation_running_pizarra[0]:
        current_frame_pizarra[0] = (current_frame_pizarra[0] + 1) % 2
        bPizarra.config(image=frames_pizarra[current_frame_pizarra[0]])
        menu.after(200, animate_pizarra)
def on_enter_pizarra(e):
    if bPizarra["state"] == "normal":
        animation_running_pizarra[0] = True
        animate_pizarra()
def on_leave_pizarra(e):
    animation_running_pizarra[0] = False
    bPizarra.config(image=frames_pizarra[0])

# --- Botón Pizarra como Button ---
pizarra_window = {"ventana": None}
def abrir_pizarra():
    if pizarra_window["ventana"] is None or not pizarra_window["ventana"].winfo_exists():
        bPizarra.config(state="disabled")
        pizarra_window["ventana"] = abrir_grafico_ingresos_egresos(menu)
        def on_close():
            bPizarra.config(state="normal")
            if pizarra_window["ventana"]:
                pizarra_window["ventana"].destroy()
                pizarra_window["ventana"] = None
        if pizarra_window["ventana"]:
            pizarra_window["ventana"].protocol("WM_DELETE_WINDOW", on_close)
bPizarra = tk.Button(menu, image=frames_pizarra[0], cursor="hand2", borderwidth=0, command=abrir_pizarra)
bPizarra.place(relx=0.5, y=500, anchor="n", x=450)
bPizarra.bind("<Enter>", on_enter_pizarra)
bPizarra.bind("<Leave>", on_leave_pizarra)

# --- Animación Flashcard ---
current_frame_flashcard = [0]
animation_running_flashcard = [False]
def animate_flashcard():
    if animation_running_flashcard[0]:
        current_frame_flashcard[0] = (current_frame_flashcard[0] + 1) % 2
        bFlashcard.config(image=frames_flashcard[current_frame_flashcard[0]])
        menu.after(200, animate_flashcard)
def on_enter_flashcard(e):
    if bFlashcard["state"] == "normal":
        animation_running_flashcard[0] = True
        animate_flashcard()
def on_leave_flashcard(e):
    animation_running_flashcard[0] = False
    bFlashcard.config(image=frames_flashcard[0])

# --- Botón Flashcard modularizado ---
flashcard_window = {"ventana": None}
def abrir_flashcard_modular():
    if flashcard_window["ventana"] is None or not (flashcard_window["ventana"] and flashcard_window["ventana"].winfo_exists()):
        bFlashcard.config(state="disabled")
        # Llama a la ventana modular y pásale el parent y un callback para reactivar el botón
        def on_close():
            flashcard_window["ventana"] = None
            bFlashcard.config(state="normal")
        flashcard_window["ventana"] = abrir_ventana_flashcard(menu, on_close)

bFlashcard = tk.Button(menu, image=frames_flashcard[0], cursor="hand2", borderwidth=0, command=abrir_flashcard_modular)
bFlashcard.place(relx=0.5, y=500, anchor="n", x=-450)
bFlashcard.bind("<Enter>", on_enter_flashcard)
bFlashcard.bind("<Leave>", on_leave_flashcard)

>>>>>>> 0425495 (último commit)
menu.mainloop()