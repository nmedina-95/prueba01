from database import conectar


def crear_tabla():
    conexion = conectar()

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS equipos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            equipo TEXT NOT NULL,
            usuario TEXT NOT NULL,
            numero_serie TEXT NOT NULL,
            ficha_entrega TEXT NOT NULL,
            consignacion TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()
