from elsa import cli
from flask import flash, Flask, jsonify, request, render_template, redirect, url_for
import csv

app = Flask(__name__)




# ===============================================================


@app.route("/")
def main():
    datos = read_csv_file('datos.csv')

    return render_template('index.html',
        title     = "Planets",
        datos   = datos,
    )

def read_csv_file(filename):
    datos = []
    with open(filename) as fh:
        rd = csv.DictReader(fh, delimiter=',')
        for row in rd:
            datos.append(row)
    return datos


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        cli(app, base_url="https://ivehiculoelectrico.com")
    else:
        app.run(debug=True, host="0.0.0.0", port=5500)
