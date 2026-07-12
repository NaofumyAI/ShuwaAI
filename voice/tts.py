import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate",170)

engine.setProperty("volume",1.0)


def hablar(texto):

    engine.say(texto)

    engine.runAndWait()