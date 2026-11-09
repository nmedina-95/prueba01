from database import conectar


def eliminar_equipo(id_equipo):
    conexion = conectar()

    conexion.execute("""
        DELETE FROM equipos
        WHERE id = ?
    """, (id_equipo,))

    conexion.commit()
    conexion.close()
