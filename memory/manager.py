import re

from database.database import guardar
from database.database import buscar


def aprender(usuario, mensaje):

    patrones = [

        ("juego favorito", r"mi juego favorito es (.+)"),

        ("color favorito", r"mi color favorito es (.+)"),

        ("comida favorita", r"mi comida favorita es (.+)"),

        ("anime favorito", r"mi anime favorito es (.+)"),

        ("pokemon favorito", r"mi pokemon favorito es (.+)")
    ]

    texto = mensaje.lower()

    for clave, patron in patrones:

        resultado = re.search(patron, texto)

        if resultado:

            valor = resultado.group(1).strip()

            guardar(usuario, clave, valor)

            return f"Entendido 😊 Recordaré que tu {clave} es {valor}."

    return None


def recordar(usuario, mensaje):

    preguntas = {

        "¿cuál es mi juego favorito?": "juego favorito",

        "cual es mi juego favorito": "juego favorito",

        "¿cuál es mi color favorito?": "color favorito",

        "cual es mi color favorito": "color favorito",

        "¿cuál es mi comida favorita?": "comida favorita",

        "cual es mi comida favorita": "comida favorita",

        "¿cuál es mi anime favorito?": "anime favorito",

        "cual es mi anime favorito": "anime favorito"

    }

    texto = mensaje.lower()

    if texto in preguntas:

        clave = preguntas[texto]

        dato = buscar(usuario, clave)

        if dato:

            return f"Tu {clave} es {dato}. 😊"

        return "Todavía no me has dicho eso."

    return None