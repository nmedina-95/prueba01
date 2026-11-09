import sqlite3

NOMBRE_BD = "equipos.db"


def conectar():
    conexion = sqlite3.connect(NOMBRE_BD)
    conexion.row_factory = sqlite3.Row
    return conexion
