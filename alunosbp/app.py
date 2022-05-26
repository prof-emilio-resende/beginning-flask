from flask import Blueprint, jsonify, request
from .db import database_alunos as database

alunos_app = Blueprint('alunos_app', __name__)

@alunos_app.route('/')
def alunos():
    return jsonify(database)

# curl -X POST -H "Content-Type: application/json" -d '{"id": 1, "name": "emilio"}' http://localhost:5000/alunos
@alunos_app.route('/', methods=['POST'])
def novo_aluno():
    novo_aluno = request.get_json()
    database.append(novo_aluno)
    return jsonify(database), 201


# curl -X GET http://localhost:5000/alunos/1
@alunos_app.route('/<int:id_aluno>', methods=['GET'])
def localiza_aluno(id_aluno):
    for aluno in database:
        if aluno['id'] == id_aluno:
            return jsonify(aluno)
    return '', 404