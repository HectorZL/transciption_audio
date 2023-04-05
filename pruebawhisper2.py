import whisper
import warnings
import os

warnings.filterwarnings("ignore", message="FP16 is not supported on CPU; using FP32 instead")

# Ahora puedes utilizar la función load_model del módulo whisper
model = whisper.load_model("medium")

# Ejecuta la transcripción y almacena el resultado en un diccionario
result = model.transcribe("/home/mrblue/Documentos/PruebaW/pw.m4a")

output_dir = "/home/mrblue/Documentos/PruebaW"

# Accedemos al valor de la clave 'text' para obtener la transcripción en formato de texto 
texto_resultado = result["text"]

# Creamos el archivo de texto y escribimos el resultado de la transcripción
with open(os.path.join(output_dir, "prueba.txt"), "w") as archivo_txt:
    archivo_txt.write(texto_resultado)