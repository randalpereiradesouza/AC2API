from flask import Flask
import json

app = Flask(__name__)

estados = [
    {
        'id': 1,
        'name': "Sao Paulo",
        "description": "Estado Brasileiro regiao Sudeste"
    },
    {
        "id": 2,
        "name": "Amazonas ",
        "description": "Estado Brasileiro regiao Norte"
    },
    {
        "id": 3,
        "name": "Rio Grande Do Sul",
        "description": "Estado Brasileiro regiao Sul"
    },
    {
        "id": 4,
        "name": "Mato Grosso",
        "description": "Estado Brasileiro regiao Centro-oeste"
    },
    {
        "id": 5,
        "name": "Ceara",
        "description": "Estado Brasileiro regiao Nordeste"
    }
]

estadosJSON = json.dumps(estados)


@app.route('/')
def home():
    return "Estados Brasileiros", 200


@app.route('/api/estados', methods=["GET"])
def estados():
    return "sem retorno", 204


if __name__ == '__main__':
    app.run()
