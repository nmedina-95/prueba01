from flask import Flask, render_template, request, redirect, url_for

from crear_tabla import crear_tabla
from insertar import insertar_equipo
from consultar import consultar_equipos, buscar_equipos
from actualizar import actualizar_equipo
from eliminar import eliminar_equipo


app = Flask(__name__)


# Crear la tabla al iniciar
crear_tabla()


# ==========================================================
# PÁGINA PRINCIPAL
# ==========================================================

@app.route("/")
def inicio():

    texto = request.args.get("buscar", "")

    if texto:
        equipos = buscar_equipos(texto)
    else:
        equipos = consultar_equipos()

    return render_template(
        "index.html",
        equipos=equipos,
        buscar=texto
    )


# ==========================================================
# GUARDAR
# ==========================================================

@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    equipo = request.form["equipo"]
    usuario = request.form["usuario"]
    numero_serie = request.form["numero_serie"]
    ficha_entrega = request.form["ficha_entrega"]
    consignacion = request.form["consignacion"]

    insertar_equipo(
        nombre,
        equipo,
        usuario,
        numero_serie,
        ficha_entrega,
        consignacion
    )

    return redirect(url_for("inicio"))


# ==========================================================
# EDITAR
# ==========================================================

@app.route("/editar/<int:id_equipo>", methods=["POST"])
def editar(id_equipo):

    nombre = request.form["nombre"]
    equipo = request.form["equipo"]
    usuario = request.form["usuario"]
    numero_serie = request.form["numero_serie"]
    ficha_entrega = request.form["ficha_entrega"]
    consignacion = request.form["consignacion"]

    actualizar_equipo(
        id_equipo,
        nombre,
        equipo,
        usuario,
        numero_serie,
        ficha_entrega,
        consignacion
    )

    return redirect(url_for("inicio"))


# ==========================================================
# ELIMINAR
# ==========================================================

@app.route("/eliminar/<int:id_equipo>", methods=["POST"])
def eliminar(id_equipo):

    eliminar_equipo(id_equipo)

    return redirect(url_for("inicio"))


# ==========================================================
# EJECUTAR SERVIDOR
# ==========================================================

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
