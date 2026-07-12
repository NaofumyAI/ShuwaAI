import requests

from config import LM_STUDIO_URL
from config import MODEL_NAME

from personality.loader import crear_prompt

from memory.history import agregar
from memory.history import obtener


SYSTEM_PROMPT = crear_prompt()


def responder(mensaje):

    mensajes = [

        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }

    ]

    mensajes.extend(obtener())

    mensajes.append(
        {
            "role": "user",
            "content": mensaje
        }
    )

    datos = {

        "model": MODEL_NAME,

        "messages": mensajes,

        "temperature": 0.8

    }

    respuesta = requests.post(

        LM_STUDIO_URL,

        json=datos

    )

    respuesta.raise_for_status()

    texto = respuesta.json()["choices"][0]["message"]["content"]

    agregar("user", mensaje)

    agregar("assistant", texto)

    return texto