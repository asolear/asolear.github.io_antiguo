from elsa import cli
from flask import flash, Flask, jsonify, request, render_template, redirect, url_for
from contenido import * 

app = Flask(__name__)




# ===============================================================



@app.route("/", methods=["GET", "POST"])
def recarga():

    return render_template(
        "index.html",

        pag=pag,
        ddindividual=ddindividual,
        ddcolectivo=ddcolectivo,
        ddmarketing=ddmarketing,
        ddcontrol=ddcontrol,
        ddmovesiii=ddmovesIII,
        menu=menu,
        menu_headline=menu_headline,
        parent_list=parent_list
    )


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cli(app, base_url="https://ivehiculoelectrico.com")
    else:
        app.run(debug=True, host="0.0.0.0", port=5500)
