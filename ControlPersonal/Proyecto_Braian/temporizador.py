import tkinter as tk

def temporizador(root):
    ventana = tk.Toplevel(root)
    ventana.title("Temporizador Pomodoro")
    ventana.geometry("300x200")

    tiempo = 25 * 60
    contador = tk.StringVar()
    contador.set("25:00")

    def actualizar():
        nonlocal tiempo
        if tiempo > 0:
            tiempo -= 1
            minutos = tiempo // 60
            segundos = tiempo % 60
            contador.set(f"{minutos:02d}:{segundos:02d}")
            ventana.after(1000, actualizar)
        else:
            contador.set("¡Fin!")

    label = tk.Label(ventana, textvariable=contador, font=("Arial", 36))
    label.pack(pady=20)

    tk.Button(ventana, text="Iniciar", command=actualizar).pack()