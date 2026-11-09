from database import conectar


def actualizar_equipo(
    id_equipo,
    nombre,
    equipo,
    usuario,
    numero_serie,
    ficha_entrega,
    consignacion
):
    conexion = conectar()

    conexion.execute("""
        UPDATE equipos
        SET
            nombre = ?,
            equipo = ?,
            usuario = ?,
            numero_serie = ?,
            ficha_entrega = ?,
            consignacion = ?
        WHERE id = ?
    """, (
        nombre,
        equipo,
        usuario,
        numero_serie,
        ficha_entrega,
        consignacion,
        id_equipo
    ))

    conexion.commit()
    conexion.close()
