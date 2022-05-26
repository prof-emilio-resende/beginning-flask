def buscar_aluno(id, db):
    return [aluno for aluno in db if aluno['id'] == id]