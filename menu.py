import os
import tkinter as tk
from PIL import Image, ImageTk

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

# Cargar imágenes Tarea
tarea0_img = ImageTk.PhotoImage(Image.open(tarea0_path))
tarea1_img = ImageTk.PhotoImage(Image.open(tarea1_path))
frames_tarea = [tarea0_img, tarea1_img]

# Cargar imágenes Pomo
pomo0_img = ImageTk.PhotoImage(Image.open(pomo0_path))
pomo1_img = ImageTk.PhotoImage(Image.open(pomo1_path))
pomo2_img = ImageTk.PhotoImage(Image.open(pomo2_path))
pomo3_img = ImageTk.PhotoImage(Image.open(pomo3_path))
pomo4_img = ImageTk.PhotoImage(Image.open(pomo4_path))
pomo5_img = ImageTk.PhotoImage(Image.open(pomo5_path))
frames_pomo = [pomo0_img, pomo1_img, pomo2_img, pomo3_img, pomo4_img, pomo5_img]

# Cargar imágenes Pizarra
pizarra0_img = ImageTk.PhotoImage(Image.open(pizarra0_path))
pizarra1_img = ImageTk.PhotoImage(Image.open(pizarra1_path))
frames_pizarra = [pizarra0_img, pizarra1_img]

# Cargar imágenes Flashcard
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
    animation_running_tarea[0] = True
    animate_tarea()

def on_leave_tarea(e):
    animation_running_tarea[0] = False
    bTarea.config(image=frames_tarea[0])

bTarea = tk.Label(menu, image=frames_tarea[0])
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
    animation_running_pomo[0] = True
    current_frame_pomo[0] = 1
    animate_pomo()

def on_leave_pomo(e):
    animation_running_pomo[0] = False
    current_frame_pomo[0] = 0
    bPomo.config(image=frames_pomo[0])

bPomo = tk.Label(menu, image=frames_pomo[0])
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
    animation_running_pizarra[0] = True
    animate_pizarra()

def on_leave_pizarra(e):
    animation_running_pizarra[0] = False
    bPizarra.config(image=frames_pizarra[0])

bPizarra = tk.Label(menu, image=frames_pizarra[0])
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
    animation_running_flashcard[0] = True
    animate_flashcard()

def on_leave_flashcard(e):
    animation_running_flashcard[0] = False
    bFlashcard.config(image=frames_flashcard[0])

bFlashcard = tk.Label(menu, image=frames_flashcard[0])
bFlashcard.place(relx=0.5, y=500, anchor="n", x=-450)
bFlashcard.bind("<Enter>", on_enter_flashcard)
bFlashcard.bind("<Leave>", on_leave_flashcard)

menu.mainloop()