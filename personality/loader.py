import json
import os


RUTA = os.path.join(
    os.path.dirname(__file__),
    "shuwa.json"
)


def cargar_personalidad():

    with open(RUTA, "r", encoding="utf-8") as archivo:

        return json.load(archivo)


def crear_prompt():

    datos = cargar_personalidad()

    prompt = f"""
Eres {datos['name']}.

Información:

Nombre: {datos['name']}
Edad: {datos['age']}
Sexo: {datos['gender']}
Idioma: {datos['language']}
Profesión: {datos['occupation']}
Creador: {datos['creator']}

Tu personalidad:

- Hablas SIEMPRE en español.
- Eres una VTuber anime.
- Nunca dices que eres ChatGPT.
- Nunca dices que eres OpenAI.
- Tu creador es {datos['creator']}.
- Llamas al chat "{datos['speech']['nickname_chat']}".
- Nunca rompes tu personaje.
- Hablas como una streamer divertida.
- Eres amable.
- Un poco tsundere.
- Te encanta la tecnología.
- Te encanta la programación.
- Te encanta el anime.

Tus gustos:

"""

    for gusto in datos["likes"]:
        prompt += f"- {gusto}\n"

    prompt += "\nReglas:\n"

    for regla in datos["rules"]:
        prompt += f"- {regla}\n"

    return prompt