from flask import Flask, jsonify
from alunosbp import database_alunos, alunos_app
from professoresbp import database_professores

app = Flask(__name__)
database = dict()


@app.route('/')
def all():
    return jsonify(database)


@app.route('/professores')
def professores():
    return jsonify(database['PROFESSOR'])


def initialize():
    database['ALUNO'] = database_alunos
    database['PROFESSOR'] = database_professores
    app.register_blueprint(alunos_app)

    app.run()

initialize()
