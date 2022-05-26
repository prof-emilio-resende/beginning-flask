from flask import Blueprint, jsonify, request
from .db import database_alunos as database
from .helper import buscar_aluno

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
    resposta = buscar_aluno(id_aluno, database)
    if len(resposta) == 0:
        return 'Not Found', 404
    
    return jsonify(resposta)

# curl -X DELETE http://localhost:5000/alunos/1
@alunos_app.route('/<int:id_aluno>', methods=['DELETE'])
def remove_aluno(id_aluno):
    resposta = buscar_aluno(id_aluno, database)
    if len(resposta) == 0:
        return 'Not Found', 404

    i = 0
    resposta = None
    for al in database:
        if al['id'] == id_aluno:
            resposta = database[i]
            del database[i]
            break
        i = i + 1
    
    return jsonify(resposta)


# curl -X PUT -H "Content-Type: application/json" -d '{"id": 1, "name": "emilio"}' http://localhost:5000/alunos/1
@alunos_app.route('/<int:id_aluno>', methods=['PUT'])
def atualiza_aluno(id_aluno):
    novo_aluno = request.get_json()
    resposta = buscar_aluno(id_aluno, database)
    if len(resposta) == 0:
        return 'Not Found', 404

    i = 0
    resposta = None
    for al in database:
        if al['id'] == id_aluno:
            resposta = database[i]
            del database[i]
            database.append(novo_aluno)
            break
        i = i + 1
    
    return jsonify(resposta)