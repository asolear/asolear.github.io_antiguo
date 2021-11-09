
Plantilla web,
para meter los datos en 
'datos.csv
'

libreoffice --calc datos.csv

- en contenidos.PY ajustar las secciones y contenidos
- Se crean por separado los tags de Index.html y los del navbar, por lo que hay que sincronizarlos

  
- crear el venv y ejecutar con
``` bash

    deactivate;
    python3 -m venv ./.venv;
    source ./.venv/bin/activate;
    pip install -r requirements.txt;
    python app.py

```
y por ultimo guardar y deplegar en gh-pages con

```
app.py

...
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
            from elsa import cli
            cli(app, base_url=https://asolear.es)
    else:
        app.run(debug=True, host='0.0.0.0', port=8888)
';
    echo python app.py serve;
    python app.py freeze;
    python app.py deploy
}

```

