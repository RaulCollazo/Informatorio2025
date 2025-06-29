<<<<<<< HEAD
# Reloj digital Gian

import tkinter as tk
import time
from datetime import date
from time import strftime
import calendar

def hora():
    tiempo = time.strftime('%H:%M:%S %p')  
    hora_Actual.config(text=tiempo)
    reloj.after(1000, hora) 

def fecha():
    hoy = date.today()
    fecha_formateada = hoy.strftime("%d/%m/%Y")  
    
    dia = strftime('%A')  
    dias_espanol = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    
    dia_espanol = dias_espanol.get(dia, dia)  
    
    fecha_Actual.config(text=f"{dia_espanol}, {fecha_formateada}")
    
    mes_actual = hoy.month
    año_actual = hoy.year
    calendario_mensual = calendar.TextCalendar(calendar.SUNDAY).formatmonth(año_actual, mes_actual)
    

    dias_ingles = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    dias_espanol = ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa']
    for i in range(len(dias_ingles)):
        calendario_mensual = calendario_mensual.replace(dias_ingles[i], dias_espanol[i])
    
  
    meses_ingles = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    meses_espanol = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    mes_ingles = calendar.month_name[mes_actual]
    mes_espanol = dict(zip(meses_ingles, meses_espanol)).get(mes_ingles, mes_ingles)
    calendario_mensual = calendario_mensual.replace(mes_ingles, mes_espanol)
    
    calendario_Actual.config(text=calendario_mensual)
    
    boton_fecha.pack_forget()  
    fecha_Actual.pack(anchor='center', pady=10) 
    calendario_Actual.pack(anchor='center', pady=10)  

reloj = tk.Tk()  
reloj.title('Reloj')
reloj.geometry('400x300')

reloj.configure(background='black')

hora_Actual = tk.Label(reloj, font=('Digital-7', 40, 'bold'), background='black', foreground='cyan')
hora_Actual.pack(anchor='center', pady=10)


boton_fecha = tk.Button(reloj, text='Ver Fecha', command=fecha, font=('Arial', 12, 'bold'), background='black', foreground='grey')
boton_fecha.pack(pady=10)


fecha_Actual = tk.Label(reloj, font=('Arial', 20, 'bold'), background='black', foreground='cyan')
fecha_Actual.pack_forget()  

calendario_Actual = tk.Label(reloj, font=('Courier New', 10), background='black', foreground='white')
calendario_Actual.pack_forget()  

hora()

reloj.mainloop()
=======
# Reloj digital Gian

import tkinter as tk
import time
from datetime import date
from time import strftime
import calendar

def hora():
    tiempo = time.strftime('%H:%M:%S %p')  
    hora_Actual.config(text=tiempo)
    reloj.after(1000, hora) 

def fecha():
    hoy = date.today()
    fecha_formateada = hoy.strftime("%d/%m/%Y")  
    
    dia = strftime('%A')  
    dias_espanol = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    
    dia_espanol = dias_espanol.get(dia, dia)  
    
    fecha_Actual.config(text=f"{dia_espanol}, {fecha_formateada}")
    
    mes_actual = hoy.month
    año_actual = hoy.year
    calendario_mensual = calendar.TextCalendar(calendar.SUNDAY).formatmonth(año_actual, mes_actual)
    

    dias_ingles = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']
    dias_espanol = ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa']
    for i in range(len(dias_ingles)):
        calendario_mensual = calendario_mensual.replace(dias_ingles[i], dias_espanol[i])
    
  
    meses_ingles = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    meses_espanol = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    mes_ingles = calendar.month_name[mes_actual]
    mes_espanol = dict(zip(meses_ingles, meses_espanol)).get(mes_ingles, mes_ingles)
    calendario_mensual = calendario_mensual.replace(mes_ingles, mes_espanol)
    
    calendario_Actual.config(text=calendario_mensual)
    
    boton_fecha.pack_forget()  
    fecha_Actual.pack(anchor='center', pady=10) 
    calendario_Actual.pack(anchor='center', pady=10)  

reloj = tk.Tk()  
reloj.title('Reloj')
reloj.geometry('400x300')

reloj.configure(background='black')

hora_Actual = tk.Label(reloj, font=('Digital-7', 40, 'bold'), background='black', foreground='cyan')
hora_Actual.pack(anchor='center', pady=10)


boton_fecha = tk.Button(reloj, text='Ver Fecha', command=fecha, font=('Arial', 12, 'bold'), background='black', foreground='grey')
boton_fecha.pack(pady=10)


fecha_Actual = tk.Label(reloj, font=('Arial', 20, 'bold'), background='black', foreground='cyan')
fecha_Actual.pack_forget()  

calendario_Actual = tk.Label(reloj, font=('Courier New', 10), background='black', foreground='white')
calendario_Actual.pack_forget()  

hora()

reloj.mainloop()
>>>>>>> 0425495 (último commit)
