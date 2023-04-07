import os
import time
import tkinter as tk
import pydub
from tkinter import filedialog, messagebox
from pydub import AudioSegment
import whisper


class WhisperGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Transcripción de audio con Whisper")

        self.audio_file = None
        self.progress_canvas = None
        self.max_time = None  # Duración máxima del archivo de audio

        # widgets
        self.select_audio_button = tk.Button(self.master, text="Seleccionar archivo de audio", command=self.select_audio)
        self.transcribe_button = tk.Button(self.master, text="Transcribir", command=self.transcribe_audio)
        self.output_label = tk.Label(self.master, text="Seleccione un archivo de audio y modelo para comenzar la transcripción")

        self.model_var = tk.StringVar(self.master)
        self.model_var.set("base")  # Valor predeterminado
        self.model_menu = tk.OptionMenu(self.master, self.model_var, "base", "small", "medium", "large")

        self.output_dir = os.getcwd()

        # Disposición de los widgets en la ventana
        self.select_audio_button.pack()
        self.model_menu.pack()
        self.transcribe_button.pack()
        self.output_label.pack()

        # Crear el Canvas de la barra de progreso
        self.progress_canvas = tk.Canvas(self.master, width=200, height=10, borderwidth=1, relief="solid")
        self.progress_canvas.pack()

        # Crear un rectángulo para mostrar el progreso actual
        self.progress_rect = self.progress_canvas.create_rectangle(0, 0, 0, 10, fill="blue", width=0)

    def select_audio(self):
        self.audio_file = filedialog.askopenfilename(
            title="Seleccionar archivo de audio",
            filetypes=[("Archivo de audio", "*.wav;*.mp3;*.ogg;*.flac;*.m4a")]
        )
        if self.audio_file:
            # Obtener la duración del archivo de audio
            audio = AudioSegment.from_file(self.audio_file)
            self.max_time = audio.duration_seconds

            messagebox.showinfo(
                "Archivo seleccionado", f"Ha seleccionado el archivo de audio: {os.path.basename(self.audio_file)}")

    def transcribe_audio(self):
        if self.audio_file:
            self.output_label["text"] = "Transcribiendo..."
            self.master.update_idletasks()

            # Cargamos el modelo seleccionado de Whisper
            model_name = self.model_var.get()
            model = whisper.load_model(model_name)

            # Actualizamos la barra de progreso cada segundo
            time_elapsed = 0
            while time_elapsed <= self.max_time:
                time.sleep(1)
                time_elapsed += 1
                progress = int(100 * time_elapsed / self.max_time)
                self.update_progressbar(progress)

            result = model.transcribe(self.audio_file)

            # Accedemos al valor de la clave 'text' para obtener la transcripción en formato de texto
            texto_resultado = result["text"]

            with open(os.path.join(self.output_dir, "prueba.txt"), "w") as archivo_txt:
              archivo_txt.write(texto_resultado)

            self.output_label["text"] = f"Transcripción completa. Resultado almacenado en {self.output_dir}"
        else:
            messagebox.showerror("Error", "No ha seleccionado ningún archivo de audio")

    def update_progressbar(self, progress):
        # Actualización de la barra de progreso
        canvas_width = 200
        progress_fraction = progress / 100
        progress_width = int(canvas_width * progress_fraction)
        self.progress_canvas.coords(self.progress_rect, 0, 0, progress_width, 10)

        # Actualización de la etiqueta de progreso
        self.output_label["text"] = f"Transcribiendo... {progress}% completado"
        self.master.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    whisper_gui = WhisperGUI(root)
    root.mainloop()