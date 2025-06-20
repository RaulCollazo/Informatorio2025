import tkinter as tk
from gestor_tareas import gestor_tareas
from temporizador import temporizador
from flashcards import flashcards
from notas import notas_rapidas
from progreso import progreso
from biblioteca import biblioteca

root = tk.Tk()
root.title("Ventana Principal de Estudio")
root.geometry("400x500")
root.config(bg="#f5f5f5")

tk.Label(root, text="Centro de Productividad", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=20)

opciones = [
    ("Temporizador Pomodoro", temporizador),
    ("Creador de Flashcards", flashcards),
    ("Gestor de Tareas", gestor_tareas),
    ("Notas Rápidas", notas_rapidas),
    ("Seguimiento de Progreso", progreso),
    ("Biblioteca de Recursos", biblioteca)
]

for texto, funcion in opciones:
    tk.Button(root, text=texto, font=("Arial", 12), width=30, height=2,
              bg="#1976d2", fg="white", activebackground="#1565c0",
              command=lambda f=funcion: f(root)).pack(pady=5)

root.mainloop()