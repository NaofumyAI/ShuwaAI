from kokoro import KPipeline
import sounddevice as sd
import threading

pipeline = KPipeline(lang_code="a")

# Evita que dos voces hablen al mismo tiempo
hablando = False


def _hablar(texto):
    global hablando

    hablando = True

    try:
        generator = pipeline(
            texto,
            voice="af_heart"
        )

        for _, _, audio in generator:
            sd.stop()
            sd.play(audio, 24000)
            sd.wait()

    finally:
        hablando = False


def hablar(texto):
    global hablando

    # Si ya estaba hablando, detenemos el audio
    if hablando:
        sd.stop()

    threading.Thread(
        target=_hablar,
        args=(texto,),
        daemon=True
    ).start()