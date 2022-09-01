from flask import Flask, request
from flask_json import FlaskJSON

app = Flask(__name__)
json = FlaskJSON(app)

# Decorador de python
@app.route("/agentpy_json", methods=['POST'])

# este método funciona a través de la ruta por medio de post
def agentpy_senddata():
    data = request.get_json(force=True)
    print(data)
    return "<p>hello world!</p>"

# app es el servidor, pero se necesita correr para que esté escuchando

if __name__ == '__main__':
    app.run()