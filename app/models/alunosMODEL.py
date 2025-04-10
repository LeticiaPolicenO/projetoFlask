from flask import Flask, jsonify, request
app = Flask(__name__)
class AlunoNaoEncontrado(Exception):
    pass


diciAlunos = {
    "alunos": [
        {
            "id": 1,
            "nome": "Amanda Silva",
            "idade": 19,
            "notas": [8.2, 7.5, 9.1],
            "email": "amanda.silva@email.com"
        },
        {
            "id": 2,
            "nome": "Bruno Oliveira",
            "idade": 22,
            "notas": [9.5, 8.8, 9.9],
            "email": "bruno.oliveira@email.com"
        },
        {
            "id": 3,
            "nome": "Carla Souza",
            "idade": 20,
            "notas": [7.0, 6.5, 7.8],
            "email": "carla.souza@email.com"
        },
        {
            "id": 4,
            "nome": "Daniel Pereira",
            "idade": 21,
            "notas": [8.5, 9.2, 8.0],
            "email": "daniel.pereira@email.com"
        },
        {
            "id": 5,
            "nome": "Elisa Martins",
            "idade": 23,
            "notas": [9.0, 8.7, 9.5],
            "email": "elisa.martins@email.com"
        },
        {
            "id": 6,
            "nome": "Felipe Costa",
            "idade": 18,
            "notas": [6.5, 7.0, 7.2],
            "email": "felipe.costa@email.com"
        }
    ]
}

def listar_alunos():
    return diciAlunos


def encontre_aluno_por_ID(idAluno):
    lista_alunos = diciAlunos['alunos']
    for aluno in lista_alunos:
        if aluno['id'] == idAluno:
            return aluno
    return jsonify({"erro": "Aluno não encontrado"}), 404
    

def criar_alunitos(aluno):
    diciAlunos['alunos'].append(aluno)


def atualizar_aluno(aluno, novos_dados):
    aluno = encontre_aluno_por_ID(aluno)
    aluno.update(novos_dados)

def deletar_aluno(aluno):
    achar_aluno = encontre_aluno_por_ID(aluno)
    diciAlunos['alunos'].remove(achar_aluno)
    return jsonify(listar_alunos())