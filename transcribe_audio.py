import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import *
from tkinter.ttk import *
from whisper import Whisper

class Interface:

    def __init__(self, master):
        self.master = master
        self.master.title("Transcripción de Audio")
        
        self.model = None
        self.audio_file = None

        # widgets
        self.select_model_label = tk.Label(self.master, text="Seleccionar modelo:")
        self.model_options = ["base", "small", "medium", "large"]
        self.model_var = tk.StringVar(value=self.model_options[0])
        self.model_dropdown = tk.ttk.Combobox(self.master, textvariable=self.model_var, values=self.model_options)
        self.model_dropdown.bind("<<ComboboxSelected>>", lambda event: self.select_model())
        self.select_audio_button = tk.Button(self.master, text="Seleccionar archivo de audio", command=self.select_audio)
        self.transcribe_button = tk.Button(self.master, text="Transcribir", command=self.transcribe_audio)
        self.output_label = tk.Label(self.master, text="Seleccione un modelo y un archivo de audio para comenzar la transcripción")
        self.output_dir = os.getcwd()

        # disposición de los widgets en la ventana
        self.select_model_label.pack()
        self.model_dropdown.pack()
        self.select_audio_button.pack()
        self.transcribe_button.pack()
        self.output_label.pack()
    
    def select_model(self):
        model_size = self.model_var.get()
        self.model = Whisper("es", model_size)
        messagebox.showinfo("Modelo seleccionado", f"Ha seleccionado el modelo de transcripción de audio {model_size}")
    
    def select_audio(self):
        self.audio_file = filedialog.askopenfilename(
                    title="Seleccionar archivo de audio",
                    filetypes=[("Archivo de audio", "*.wav;*.mp3;*.ogg;*.flac;*.m4a")]
                )
        if self.audio_file:
            messagebox.showinfo("Archivo seleccionado", f"Ha seleccionado el archivo de audio: {os.path.basename(self.audio_file)}")
    
    def transcribe_audio(self):
        if self.model is None:
            messagebox.showerror("Error", "Debe seleccionar un modelo antes de comenzar la transcripción")
            return
        elif self.audio_file is None:
            messagebox.showerror("Error", "Debe seleccionar un archivo de audio antes de comenzar la transcripción")
            return

        try:
            self.output_label.config(text=f"Transcribiendo {os.path.basename(self.audio_file)}")
            self.master.update_idletasks()

            with open(self.audio_file, "rb") as audio_file:
                audio_data = audio_file.read()

            result = self.model.transcribe(audio_data)

        except Exception as e:
            self.output_label.config(text=f"Error al transcribir el archivo: {str(e)}")

        else:
            texto_resultado = result["text"]
            with open(os.path.join(self.output_dir, "transcripcion.txt"), "w") as archivo_txt:
                archivo_txt.write(texto_resultado)

            self.output_label.config(text=f"Transcripción completa. Resultado almacenado en {os.path.join(self.output_dir, 'transcripcion.txt')}")

if __name__ == "__main__":
    ventana = tk.Tk()
    gui = Interface(ventana)
    ventana.mainloop()