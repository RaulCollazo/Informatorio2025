
import tkinter as tk
import math

def mostrar_calculadora():
    ventana = tk.Toplevel()
    ventana.title("Súper Calculadora Científica")
    ventana.geometry("500x700")
    ventana.configure(bg="#2c3e50")
    ventana.resizable(False, False)

    entrada = tk.StringVar()
    campo_entrada = tk.Entry(ventana, textvariable=entrada, font=("Arial", 28), bd=10, insertwidth=2,
                              width=22, borderwidth=4, justify="right")
    campo_entrada.grid(row=0, column=0, columnspan=6, pady=20)

    def agregar_caracter(caracter):
        entrada_actual = entrada.get()
        entrada.set(entrada_actual + str(caracter))

    def limpiar():
        entrada.set("")

    def calcular():
        try:
            expresion = entrada.get()
            expresion = expresion.replace("√", "math.sqrt")
            expresion = expresion.replace("ln", "math.log")
            expresion = expresion.replace("log", "math.log10")
            expresion = expresion.replace("sin", "math.sin")
            expresion = expresion.replace("cos", "math.cos")
            expresion = expresion.replace("tan", "math.tan")
            expresion = expresion.replace("pi", "math.pi")
            expresion = expresion.replace("e", "math.e")
            resultado = eval(expresion)
            entrada.set(resultado)
        except Exception:
            entrada.set("Error")

    botones = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3), ('sin(', 1, 4), ('cos(', 1, 5),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3), ('tan(', 2, 4), ('log(', 2, 5),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3), ('ln(', 3, 4), ('√(', 3, 5),
        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('(', 4, 3), (')', 4, 4), ('^', 4, 5),
        ('pi', 5, 0), ('e', 5, 1), ('C', 5, 2), ('=', 5, 3, 3)
    ]

    for boton in botones:
        texto = boton[0]
        fila = boton[1]
        columna = boton[2]
        columna_span = boton[3] if len(boton) == 4 else 1

        if texto == '=':
            comando = calcular
            color = "#27ae60"
        elif texto == 'C':
            comando = limpiar
            color = "#e74c3c"
        elif texto == '^':
            comando = lambda: agregar_caracter("**")
            color = "#34495e"
        else:
            comando = lambda t=texto: agregar_caracter(t)
            color = "#34495e"

        b = tk.Button(ventana, text=texto, padx=20, pady=20, font=("Arial", 18),
                      bg=color, fg="white", command=comando, relief="raised", bd=3)
        b.grid(row=fila, column=columna, columnspan=columna_span, sticky="nsew", padx=3, pady=3)

    for i in range(6):
        ventana.rowconfigure(i, weight=1)
        ventana.columnconfigure(i, weight=1)
