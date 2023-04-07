import os
import tkinter as tk
from tkinter import filedialog, messagebox
import whisper
import warnings

warnings.filterwarnings("ignore")

class WhisperGUI:

    def __init__(self, master):
        self.master = master
        self.master.title("Transcripción de audio con Whisper")

        self.audio_file = None

        # widgets
        self.select_audio_button = tk.Button(self.master, text="Seleccionar archivo de audio",
                                             command=self.select_audio)
        self.transcribe_button = tk.Button(self.master, text="Transcribir", command=self.transcribe_audio)
        self.output_label = tk.Label(self.master,
                                     text="Seleccione un archivo de audio para comenzar la transcripción")

        self.output_dir = os.getcwd()

        # disposición de los widgets en la ventana
        self.select_audio_button.pack()
        self.transcribe_button.pack()
        self.output_label.pack()

    def select_audio(self):
        self.audio_file = filedialog.askopenfilename(
            title="Seleccionar archivo de audio",
            filetypes=[("Archivo de audio", "*.wav;*.mp3;*.ogg;*.flac;*.m4a")]
        )
        if self.audio_file:
            messagebox.showinfo(
                "Archivo seleccionado", f"Ha seleccionado el archivo de audio: {os.path.basename(self.audio_file)}")

    def transcribe_audio(self):
        if self.audio_file:
            self.output_label["text"] = "Transcribiendo..."
            self.master.update_idletasks()

            # Cargamos el modelo base de Whisper
            model = whisper.load_model("base")

            result = model.transcribe(self.audio_file)


            # Accedemos al valor de la clave 'text' para obtener la transcripción en formato de texto 
            texto_resultado = result["text"]

            with open(os.path.join(self.output_dir, "prueba.txt"), "w") as archivo_txt:
              archivo_txt.write(texto_resultado)

            self.output_label["text"] = f"Transcripción completa. Resultado almacenado en {self.output_dir}"
        else:
            messagebox.showerror("Error", "No ha seleccionado ningún archivo de audio")


if __name__ == "__main__":
    root = tk.Tk()
    gui = WhisperGUI(root)
    root.mainloop()