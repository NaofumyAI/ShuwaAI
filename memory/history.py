HISTORIAL = []

LIMITE = 10


def agregar(role, mensaje):

    HISTORIAL.append(
        {
            "role": role,
            "content": mensaje
        }
    )

    if len(HISTORIAL) > LIMITE:
        HISTORIAL.pop(0)


def obtener():

    return HISTORIAL.copy()


def limpiar():

    HISTORIAL.clear()