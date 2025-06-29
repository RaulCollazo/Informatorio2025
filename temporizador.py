import tkinter as tk

class TemporizadorPomodoro:
    instancia = None  # Singleton

    def __init__(self, root, on_close_callback=None):
        if TemporizadorPomodoro.instancia is not None:
            try:
                TemporizadorPomodoro.instancia.root.lift()
                TemporizadorPomodoro.instancia.root.focus_force()
            except:
                pass
            return

        self.root = tk.Toplevel(root)
        self.root.title("Temporizador Pomodoro")
        ancho_ventana = 350
        alto_ventana = 240
        x = self.root.winfo_screenwidth() - ancho_ventana
        y = 0
        self.root.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.root.config(bg="#f5f5f5")
        self.root.protocol("WM_DELETE_WINDOW", self.cerrar_ventana)
        self.on_close_callback = on_close_callback

        self.modo = tk.StringVar(value='25')
        self.trabajando = True
        self.tiempo_restante = 25 * 60
        self.temporizador_activo = False
        self.after_id = None

        # Opciones de Pomodoro
        frame_opciones = tk.Frame(self.root, bg="#f5f5f5")
        frame_opciones.pack(pady=10)
        tk.Label(frame_opciones, text="Duración Pomodoro:", bg="#f5f5f5").pack(side=tk.LEFT)
        tk.Radiobutton(frame_opciones, text="25 min", variable=self.modo, value='25', command=self.cambiar_modo, bg="#f5f5f5").pack(side=tk.LEFT)
        tk.Radiobutton(frame_opciones, text="50 min", variable=self.modo, value='50', command=self.cambiar_modo, bg="#f5f5f5").pack(side=tk.LEFT)

        # Etiqueta de estado
        self.label_estado = tk.Label(self.root, text="Tiempo de Trabajo", bg="#f5f5f5", font=("Arial", 12))
        self.label_estado.pack(pady=5)

        # Etiqueta de tiempo
        self.label_tiempo = tk.Label(self.root, text=self.formatear_tiempo(self.tiempo_restante), font=("Arial", 40), bg="#f5f5f5")
        self.label_tiempo.pack(pady=10)

        # Botones de control
        frame_botones = tk.Frame(self.root, bg="#f5f5f5")
        frame_botones.pack(pady=10)
        self.boton_inicio = tk.Button(frame_botones, text="Iniciar", command=self.iniciar)
        self.boton_inicio.pack(side=tk.LEFT, padx=5)
        self.boton_pausa = tk.Button(frame_botones, text="Pausar", command=self.pausar, state="disabled")
        self.boton_pausa.pack(side=tk.LEFT, padx=5)
        self.boton_reiniciar = tk.Button(frame_botones, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack(side=tk.LEFT, padx=5)

        TemporizadorPomodoro.instancia = self

    def cambiar_modo(self):
        self.pausar()
        self.trabajando = True
        if self.modo.get() == '25':
            self.tiempo_restante = 25 * 60
        else:
            self.tiempo_restante = 50 * 60
        self.label_estado.config(text="Tiempo de Trabajo")
        self.label_tiempo.config(text=self.formatear_tiempo(self.tiempo_restante))

    def iniciar(self):
        if not self.temporizador_activo:
            self.temporizador_activo = True
            self.boton_inicio.config(state="disabled")
            self.boton_pausa.config(state="normal")
            self.actualizar_tiempo()

    def pausar(self):
        if self.temporizador_activo:
            self.temporizador_activo = False
            self.boton_inicio.config(state="normal")
            self.boton_pausa.config(state="disabled")
            if self.after_id:
                self.root.after_cancel(self.after_id)
                self.after_id = None

    def reiniciar(self):
        self.pausar()
        self.trabajando = True
        if self.modo.get() == '25':
            self.tiempo_restante = 25 * 60
        else:
            self.tiempo_restante = 50 * 60
        self.label_estado.config(text="Tiempo de Trabajo")
        self.label_tiempo.config(text=self.formatear_tiempo(self.tiempo_restante))

    def actualizar_tiempo(self):
        self.label_tiempo.config(text=self.formatear_tiempo(self.tiempo_restante))
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.after_id = self.root.after(1000, self.actualizar_tiempo)
        else:
            if self.trabajando:
                self.trabajando = False
                self.tiempo_restante = 5 * 60
                self.label_estado.config(text="¡Descanso!")
                self.label_tiempo.config(text=self.formatear_tiempo(self.tiempo_restante))
                self.actualizar_tiempo()
            else:
                self.trabajando = True
                if self.modo.get() == '25':
                    self.tiempo_restante = 25 * 60
                else:
                    self.tiempo_restante = 50 * 60
                self.label_estado.config(text="Tiempo de Trabajo")
                self.label_tiempo.config(text=self.formatear_tiempo(self.tiempo_restante))
                self.actualizar_tiempo()

    def formatear_tiempo(self, segundos):
        minutos = segundos // 60
        segundos = segundos % 60
        return f"{minutos:02}:{segundos:02}"

    def cerrar_ventana(self):
        self.pausar()
        TemporizadorPomodoro.instancia = None
        if self.on_close_callback:
            self.on_close_callback()
        self.root.destroy()

def temporizador(root, on_close_callback=None):
    TemporizadorPomodoro(root, on_close_callback)