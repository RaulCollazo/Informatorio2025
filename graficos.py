import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import defaultdict
import os
from datetime import datetime

ARCHIVO_INGRESOS = "ingresos.txt"
ARCHIVO_EGRESOS = "egresos.txt"

def abrir_grafico_ingresos_egresos(parent):
    if not os.path.exists(ARCHIVO_INGRESOS) and not os.path.exists(ARCHIVO_EGRESOS):
        messagebox.showinfo("Sin datos", "No hay datos de ingresos o egresos para mostrar.")
        return None

    # Lee los archivos y agrupa por día
    ingresos_por_fecha = defaultdict(float)
    egresos_por_fecha = defaultdict(float)
    for archivo, dic in [
        (ARCHIVO_INGRESOS, ingresos_por_fecha),
        (ARCHIVO_EGRESOS, egresos_por_fecha),
    ]:
        if os.path.exists(archivo):
            with open(archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    try:
                        partes = linea.split("|")
                        fecha = datetime.strptime(partes[0].strip(), "%d/%m/%Y %H:%M:%S").date()
                        monto = float(partes[1].replace("$", "").strip())
                        dic[fecha] += monto
                    except Exception:
                        continue  # Si hay líneas corruptas, las salta

    # Unifica fechas
    fechas = sorted(set(ingresos_por_fecha.keys()).union(egresos_por_fecha.keys()))
    ingresos = [ingresos_por_fecha.get(fecha, 0) for fecha in fechas]
    egresos = [egresos_por_fecha.get(fecha, 0) for fecha in fechas]

    # Crear ventana de gráfico
    win = tk.Toplevel(parent)
    win.title("Estadística de Ingresos y Egresos")
    win.geometry("720x480")

    fig, ax = plt.subplots(figsize=(8,4))
    ax.bar(fechas, ingresos, color="green", label="Ingresos")
    ax.bar(fechas, egresos, color="red", label="Egresos", bottom=ingresos)
    ax.set_title("Ingresos y Egresos por día")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Monto")
    ax.legend()
    plt.xticks(rotation=45)

    canvas = FigureCanvasTkAgg(fig, master=win)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    return win