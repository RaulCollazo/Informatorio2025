<<<<<<< HEAD
import tkinter as tk
from datetime import date, datetime
import time
import calendar
import os

from config import COLOR_FONDO, COLOR_LISTA_FONDO, COLOR_TEXTO_GENERAL, COLOR_BOTON, COLOR_BOTON_TEXTO, FUENTE_TEXTO, FUENTE_TITULO

ARCHIVO_INGRESOS = "ingresos.txt"
ARCHIVO_EGRESOS = "egresos.txt"

class GestorIngresosEgresosApp:
    def __init__(self, parent):
        # Creamos una ventana secundaria (Toplevel) que NO cierra la principal
        self.root = tk.Toplevel(parent)
        self.root.title("Gestor de Ingresos y Egresos")
        self.root.geometry("700x600")
        self.root.configure(bg=COLOR_FONDO)
        self.root.transient(parent)
        self.root.grab_set()  # Opcional: para que la ventana tenga el foco

        # --- Resto del código igual ---
        self.hora_Actual = tk.Label(self.root, font=('Digital-7', 40, 'bold'), bg='black', fg='cyan')
        self.hora_Actual.pack(anchor='center', pady=10)

        self.boton_fecha = tk.Button(self.root, text='Ver Fecha', command=self.mostrar_fecha,
                                     font=('Arial', 12, 'bold'), background='black', foreground='grey')
        self.boton_fecha.pack(pady=5)

        self.fecha_Actual = tk.Label(self.root, font=('Arial', 20, 'bold'), background='black', foreground='cyan')
        self.fecha_Actual.pack_forget()

        self.calendario_Actual = tk.Label(self.root, font=('Courier New', 10), background='black', foreground='white')
        self.calendario_Actual.pack_forget()

        self.actualizar_hora()

        # Frame de registro
        frame_registro = tk.Frame(self.root, bg=COLOR_FONDO)
        frame_registro.pack(padx=10, pady=10, fill='x')

        self.tipo_var = tk.StringVar(value="Ingreso")
        tk.Label(frame_registro, text="Tipo:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=0, sticky="e")
        tk.Radiobutton(frame_registro, text="Ingreso", variable=self.tipo_var, value="Ingreso", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=1, sticky="w")
        tk.Radiobutton(frame_registro, text="Egreso", variable=self.tipo_var, value="Egreso", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=2, sticky="w")

        tk.Label(frame_registro, text="Monto:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=1, column=0, sticky="e", pady=5)
        self.monto_var = tk.StringVar()
        tk.Entry(frame_registro, textvariable=self.monto_var, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=1, column=1, columnspan=2, sticky="we", pady=5)

        tk.Label(frame_registro, text="Descripción:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=2, column=0, sticky="e", pady=5)
        self.desc_var = tk.StringVar()
        tk.Entry(frame_registro, textvariable=self.desc_var, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=2, column=1, columnspan=2, sticky="we", pady=5)

        tk.Button(frame_registro, text="Registrar", command=self.registrar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO).grid(row=3, column=0, columnspan=3, pady=10)

        frame_registro.columnconfigure(1, weight=1)
        frame_registro.columnconfigure(2, weight=1)

        # Frame para listas de ingresos y egresos
        frame_listas = tk.Frame(self.root, bg=COLOR_FONDO)
        frame_listas.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(frame_listas, text="Ingresos", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=0, column=0, sticky="w", padx=10)
        tk.Label(frame_listas, text="Egresos", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=0, column=1, sticky="w", padx=10)

        self.lista_ingresos = tk.Listbox(frame_listas, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, width=40)
        self.lista_ingresos.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.lista_egresos = tk.Listbox(frame_listas, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, width=40)
        self.lista_egresos.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        frame_listas.columnconfigure(0, weight=1)
        frame_listas.columnconfigure(1, weight=1)
        frame_listas.rowconfigure(1, weight=1)

        self.cargar_listas()

    def actualizar_hora(self):
        tiempo = time.strftime('%H:%M:%S %p')
        self.hora_Actual.config(text=tiempo)
        self.root.after(1000, self.actualizar_hora)

    def mostrar_fecha(self):
        hoy = date.today()
        fecha_formateada = hoy.strftime("%d/%m/%Y")  
        dia = time.strftime('%A')
        dias_es = {
            'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
            'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
        }
        dia_es = dias_es.get(dia, dia)
        self.fecha_Actual.config(text=f"{dia_es}, {fecha_formateada}")

        mes = hoy.month
        año = hoy.year
        calendario_mensual = calendar.TextCalendar(calendar.SUNDAY).formatmonth(año, mes)

        dias_en = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        dias_es = ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa']
        for i in range(7):
            calendario_mensual = calendario_mensual.replace(dias_en[i], dias_es[i])

        meses_en = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
        meses_es = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        mes_nombre = calendar.month_name[mes]
        mes_traducido = dict(zip(meses_en, meses_es)).get(mes_nombre, mes_nombre)
        calendario_mensual = calendario_mensual.replace(mes_nombre, mes_traducido)

        self.calendario_Actual.config(text=calendario_mensual)

        self.boton_fecha.pack_forget()
        self.fecha_Actual.pack(anchor='center', pady=10)
        self.calendario_Actual.pack(anchor='center', pady=10)

    def registrar(self):
        tipo = self.tipo_var.get()
        monto = self.monto_var.get().strip()
        desc = self.desc_var.get().strip()
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if not monto or not desc:
            tk.messagebox.showwarning("Faltan datos", "Por favor ingresa monto y descripción.")
            return
        try:
            monto_float = float(monto.replace(",", "."))
        except ValueError:
            tk.messagebox.showerror("Error de monto", "El monto debe ser un número.")
            return
        linea = f"{fecha_hora} | ${monto_float:.2f} | {desc}"
        archivo = ARCHIVO_INGRESOS if tipo == "Ingreso" else ARCHIVO_EGRESOS
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
        self.monto_var.set("")
        self.desc_var.set("")
        self.cargar_listas()
        tk.messagebox.showinfo("Registrado", f"{tipo} registrado correctamente.")

    def cargar_listas(self):
        self.lista_ingresos.delete(0, tk.END)
        self.lista_egresos.delete(0, tk.END)
        if os.path.exists(ARCHIVO_INGRESOS):
            with open(ARCHIVO_INGRESOS, "r", encoding="utf-8") as f:
                for linea in f:
                    self.lista_ingresos.insert(tk.END, linea.strip())
        if os.path.exists(ARCHIVO_EGRESOS):
            with open(ARCHIVO_EGRESOS, "r", encoding="utf-8") as f:
                for linea in f:
                    self.lista_egresos.insert(tk.END, linea.strip())

# Esta función es la que debes importar y llamar desde tu menú
def gestor_ingresos_egresos(parent):
=======
import tkinter as tk
from datetime import date, datetime
import time
import calendar
import os

from config import COLOR_FONDO, COLOR_LISTA_FONDO, COLOR_TEXTO_GENERAL, COLOR_BOTON, COLOR_BOTON_TEXTO, FUENTE_TEXTO, FUENTE_TITULO

ARCHIVO_INGRESOS = "ingresos.txt"
ARCHIVO_EGRESOS = "egresos.txt"

class GestorIngresosEgresosApp:
    def __init__(self, parent):
        # Creamos una ventana secundaria (Toplevel) que NO cierra la principal
        self.root = tk.Toplevel(parent)
        self.root.title("Gestor de Ingresos y Egresos")
        self.root.geometry("700x600")
        self.root.configure(bg=COLOR_FONDO)
        self.root.transient(parent)
        self.root.grab_set()  # Opcional: para que la ventana tenga el foco

        # --- Resto del código igual ---
        self.hora_Actual = tk.Label(self.root, font=('Digital-7', 40, 'bold'), bg='black', fg='cyan')
        self.hora_Actual.pack(anchor='center', pady=10)

        self.boton_fecha = tk.Button(self.root, text='Ver Fecha', command=self.mostrar_fecha,
                                     font=('Arial', 12, 'bold'), background='black', foreground='grey')
        self.boton_fecha.pack(pady=5)

        self.fecha_Actual = tk.Label(self.root, font=('Arial', 20, 'bold'), background='black', foreground='cyan')
        self.fecha_Actual.pack_forget()

        self.calendario_Actual = tk.Label(self.root, font=('Courier New', 10), background='black', foreground='white')
        self.calendario_Actual.pack_forget()

        self.actualizar_hora()

        # Frame de registro
        frame_registro = tk.Frame(self.root, bg=COLOR_FONDO)
        frame_registro.pack(padx=10, pady=10, fill='x')

        self.tipo_var = tk.StringVar(value="Ingreso")
        tk.Label(frame_registro, text="Tipo:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=0, sticky="e")
        tk.Radiobutton(frame_registro, text="Ingreso", variable=self.tipo_var, value="Ingreso", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=1, sticky="w")
        tk.Radiobutton(frame_registro, text="Egreso", variable=self.tipo_var, value="Egreso", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=0, column=2, sticky="w")

        tk.Label(frame_registro, text="Monto:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=1, column=0, sticky="e", pady=5)
        self.monto_var = tk.StringVar()
        tk.Entry(frame_registro, textvariable=self.monto_var, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=1, column=1, columnspan=2, sticky="we", pady=5)

        tk.Label(frame_registro, text="Descripción:", bg=COLOR_FONDO, font=FUENTE_TEXTO).grid(row=2, column=0, sticky="e", pady=5)
        self.desc_var = tk.StringVar()
        tk.Entry(frame_registro, textvariable=self.desc_var, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=2, column=1, columnspan=2, sticky="we", pady=5)

        tk.Button(frame_registro, text="Registrar", command=self.registrar, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, font=FUENTE_TEXTO).grid(row=3, column=0, columnspan=3, pady=10)

        frame_registro.columnconfigure(1, weight=1)
        frame_registro.columnconfigure(2, weight=1)

        # Frame para listas de ingresos y egresos
        frame_listas = tk.Frame(self.root, bg=COLOR_FONDO)
        frame_listas.pack(fill='both', expand=True, padx=10, pady=10)

        tk.Label(frame_listas, text="Ingresos", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=0, column=0, sticky="w", padx=10)
        tk.Label(frame_listas, text="Egresos", font=FUENTE_TITULO, bg=COLOR_FONDO, fg=COLOR_TEXTO_GENERAL).grid(row=0, column=1, sticky="w", padx=10)

        self.lista_ingresos = tk.Listbox(frame_listas, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, width=40)
        self.lista_ingresos.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
        self.lista_egresos = tk.Listbox(frame_listas, font=FUENTE_TEXTO, bg=COLOR_LISTA_FONDO, fg=COLOR_TEXTO_GENERAL, width=40)
        self.lista_egresos.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")

        frame_listas.columnconfigure(0, weight=1)
        frame_listas.columnconfigure(1, weight=1)
        frame_listas.rowconfigure(1, weight=1)

        self.cargar_listas()

    def actualizar_hora(self):
        tiempo = time.strftime('%H:%M:%S %p')
        self.hora_Actual.config(text=tiempo)
        self.root.after(1000, self.actualizar_hora)

    def mostrar_fecha(self):
        hoy = date.today()
        fecha_formateada = hoy.strftime("%d/%m/%Y")  
        dia = time.strftime('%A')
        dias_es = {
            'Monday': 'Lunes', 'Tuesday': 'Martes', 'Wednesday': 'Miércoles',
            'Thursday': 'Jueves', 'Friday': 'Viernes', 'Saturday': 'Sábado', 'Sunday': 'Domingo'
        }
        dia_es = dias_es.get(dia, dia)
        self.fecha_Actual.config(text=f"{dia_es}, {fecha_formateada}")

        mes = hoy.month
        año = hoy.year
        calendario_mensual = calendar.TextCalendar(calendar.SUNDAY).formatmonth(año, mes)

        dias_en = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
        dias_es = ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa']
        for i in range(7):
            calendario_mensual = calendario_mensual.replace(dias_en[i], dias_es[i])

        meses_en = ['January', 'February', 'March', 'April', 'May', 'June',
                    'July', 'August', 'September', 'October', 'November', 'December']
        meses_es = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
                    'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']
        mes_nombre = calendar.month_name[mes]
        mes_traducido = dict(zip(meses_en, meses_es)).get(mes_nombre, mes_nombre)
        calendario_mensual = calendario_mensual.replace(mes_nombre, mes_traducido)

        self.calendario_Actual.config(text=calendario_mensual)

        self.boton_fecha.pack_forget()
        self.fecha_Actual.pack(anchor='center', pady=10)
        self.calendario_Actual.pack(anchor='center', pady=10)

    def registrar(self):
        tipo = self.tipo_var.get()
        monto = self.monto_var.get().strip()
        desc = self.desc_var.get().strip()
        fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        if not monto or not desc:
            tk.messagebox.showwarning("Faltan datos", "Por favor ingresa monto y descripción.")
            return
        try:
            monto_float = float(monto.replace(",", "."))
        except ValueError:
            tk.messagebox.showerror("Error de monto", "El monto debe ser un número.")
            return
        linea = f"{fecha_hora} | ${monto_float:.2f} | {desc}"
        archivo = ARCHIVO_INGRESOS if tipo == "Ingreso" else ARCHIVO_EGRESOS
        with open(archivo, "a", encoding="utf-8") as f:
            f.write(linea + "\n")
        self.monto_var.set("")
        self.desc_var.set("")
        self.cargar_listas()
        tk.messagebox.showinfo("Registrado", f"{tipo} registrado correctamente.")

    def cargar_listas(self):
        self.lista_ingresos.delete(0, tk.END)
        self.lista_egresos.delete(0, tk.END)
        if os.path.exists(ARCHIVO_INGRESOS):
            with open(ARCHIVO_INGRESOS, "r", encoding="utf-8") as f:
                for linea in f:
                    self.lista_ingresos.insert(tk.END, linea.strip())
        if os.path.exists(ARCHIVO_EGRESOS):
            with open(ARCHIVO_EGRESOS, "r", encoding="utf-8") as f:
                for linea in f:
                    self.lista_egresos.insert(tk.END, linea.strip())

# Esta función es la que debes importar y llamar desde tu menú
def gestor_ingresos_egresos(parent):
>>>>>>> 0425495 (último commit)
    GestorIngresosEgresosApp(parent)