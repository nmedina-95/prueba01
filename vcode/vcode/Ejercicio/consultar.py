from database import conectar


def consultar_equipos():
    conexion = conectar()

    registros = conexion.execute("""
        SELECT *
        FROM equipos
        ORDER BY id DESC
    """).fetchall()

    conexion.close()

    return registros


def buscar_equipos(texto):
    conexion = conectar()

    texto = f"%{texto}%"

    registros = conexion.execute("""
        SELECT *
        FROM equipos
        WHERE nombre LIKE ?
           OR equipo LIKE ?
           OR usuario LIKE ?
           OR numero_serie LIKE ?
           OR ficha_entrega LIKE ?
        ORDER BY id DESC
    """, (
        texto,
        texto,
        texto,
        texto,
        texto
    )).fetchall()

    conexion.close()

    return registros
