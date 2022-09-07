from flask import Flask, request
from flask_json import FlaskJSON

app = Flask(__name__)
json = FlaskJSON(app)

# Decorador de python
# este método funciona a través de la ruta por medio de post
# estas dos lineas deben de estar siempre jutans (el decorador y la función)
@app.route("/agentpy_json", methods=['POST'])
def agentpy_senddata():
    data = request.get_json(force=True)
    print(data)
    return "Posted"

# app es el servidor, pero se necesita correr para que esté escuchando

if __name__ == '__main__':
    app.run()

# cuando se corra este programa, se tendrá un servidor que va leer los datos del json y los va a imprimir