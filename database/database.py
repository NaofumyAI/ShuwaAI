import sqlite3
from config import DATABASE


def conectar():
    return sqlite3.connect(DATABASE)


def crear_tablas():

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memoria(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT,
        clave TEXT,
        valor TEXT
    )
    """)

    conexion.commit()
    conexion.close()


def guardar(usuario, clave, valor):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO memoria(usuario, clave, valor)
        VALUES (?, ?, ?)
        """,
        (usuario, clave, valor)
    )

    conexion.commit()
    conexion.close()


def buscar(usuario, clave):

    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT valor
        FROM memoria
        WHERE usuario=? AND clave=?
        ORDER BY id DESC
        LIMIT 1
        """,
        (usuario, clave)
    )

    dato = cursor.fetchone()

    conexion.close()

    if dato:
        return dato[0]

    return None