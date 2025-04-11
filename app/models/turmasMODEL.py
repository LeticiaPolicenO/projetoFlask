from flask import Flask, jsonify, request
app = Flask(__name__)
class AlunoNaoEncontrado(Exception):
    pass

diciTurma = {
    "turmas": [
            {
                "id": 1,
                "nome": "Turma A",
                "semestre": 1,
                "alunos_id": [1, 2],
                "professor_id": 1
            },
            {
                "id": 2,
                "nome": "Turma B",
                "semestre": 2,
                "alunos_id": [3, 4],
                "professor_id": 2
            },
            {
                "id": 3,
                "nome": "Turma C",
                "semestre": 1,
                "alunos_id": [5, 6],
                "professor_id": 3
            },
            {
                "id": 4,
                "nome": "Turma D",
                "semestre": 2,
                "alunos_id": [1, 3, 5],
                "professor_id": 4
            },
            {
                "id": 5,
                "nome": "Turma E",
                "semestre": 1,
                "alunos_id": [2, 4, 6],
                "professor_id": 5
            }
        ]
    }

def listar_turmas():
    return diciTurma

def encontrar_turma_por_id(idTurma):
    listar_turmas()
    for turma in diciTurma['turmas']:
        if turma['id'] == idTurma:
            return turma
    return jsonify({"erro": "Turma nao encontrada"}), 404


def criar_turma(nova_turma):
    diciTurma['turmas'].append(nova_turma)


def atualizar_turma(idTurma, novos_dados):
    turma = encontrar_turma_por_id(idTurma)
    turma.update(novos_dados)

def deletar_turma(idTurma):
    turma = encontrar_turma_por_id(idTurma)
    diciTurma['turmas'].remove(turma)
    return jsonify(listar_turmas())

