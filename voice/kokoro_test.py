from kokoro import KPipeline
import soundfile as sf
import sounddevice as sd

pipeline = KPipeline(lang_code="a")

texto = "Hola Naofumy. Soy Shuwa. Esta es mi primera prueba de voz."

generator = pipeline(
    texto,
    voice="af_heart"
)

for i, (gs, ps, audio) in enumerate(generator):

    sf.write("salida.wav", audio, 24000)

    print("Audio generado.")

    sd.play(audio, 24000)
    sd.wait()