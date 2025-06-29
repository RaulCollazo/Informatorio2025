
import tkinter as tk
from datetime import date, datetime
import time
import calendar

from menu import MenuPrincipal
from registro import RegistroPersonal
from lista_registros import ListaRegistros
from config import COLOR_FONDO

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Control de Ingreso y Salida de Personal")
        self.root.geometry("600x600")
        self.root.configure(bg=COLOR_FONDO)

        self.registro = RegistroPersonal(self)
        self.menu = MenuPrincipal(self)
        self.menu.crear_menu()

        # Sección de reloj y calendario integrados
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

        # Frame para listas
        self.frame_listas = tk.Frame(self.root, bg=COLOR_FONDO)
        self.frame_listas.pack(fill='both', expand=True, padx=10, pady=10)

        self.lista_ingresos = ListaRegistros(self.frame_listas, "Ingresos")
        self.lista_salidas = ListaRegistros(self.frame_listas, "Salidas")

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

    def registrar(self, tipo):
        self.registro.abrir_ventana(tipo)
