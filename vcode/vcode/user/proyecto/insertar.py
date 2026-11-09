from database import conectar


def insertar_equipo(
    nombre,
    equipo,
    usuario,
    numero_serie,
    ficha_entrega,
    consignacion
):
    conexion = conectar()

    conexion.execute("""
        INSERT INTO equipos (
            nombre,
            equipo,
            usuario,
            numero_serie,
            ficha_entrega,
            consignacion
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        nombre,
        equipo,
        usuario,
        numero_serie,
        ficha_entrega,
        consignacion
    ))

    conexion.commit()
    conexion.close()
