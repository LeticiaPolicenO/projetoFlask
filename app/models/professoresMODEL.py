from flask import Flask, jsonify, request
app = Flask(__name__)
class AlunoNaoEncontrado(Exception):
    pass

diciProfessor = {
    "professores": [
            {
                "id": 1,
                "nome": "Rafael Almeida",
                "disciplina": "Matemática",
                "email": "rafael.almeida@email.com"
            },
            {
                "id": 2,
                "nome": "Juliana Silva",
                "disciplina": "Física",
                "email": "juliana.silva@email.com"
            },
            {
                "id": 3,
                "nome": "Carlos Roberto",
                "disciplina": "Química",
                "email": "carlos.roberto@email.com"
            },
            {
                "id": 4,
                "nome": "Patrícia Oliveira",
                "disciplina": "Biologia",
                "email": "patricia.oliveira@email.com"
            },
            {
                "id": 5,
                "nome": "Gustavo Mendes",
                "disciplina": "História",
                "email": "gustavo.mendes@email.com"
            }
        ]
}

def listar_professores():
    return diciProfessor

def encontre_professor_por_id(idProfessor):
    listar_professores()
    for professor in diciProfessor['professores']:
        if professor['id'] == idProfessor:
            return professor
        return jsonify({"erro": "Professor não encontrado"}), 404

def criar_professor(novo_professor):
    diciProfessor['professores'].append(novo_professor)


def atualizar_professor(idProfessor, novos_dados):
    professor = encontre_professor_por_id(idProfessor)
    professor.update(novos_dados)

def deletar_professor(idProfessor):
    achar_professor = encontre_professor_por_id(idProfessor)
    diciProfessor['professores'].remove(achar_professor)
    return jsonify(listar_professores())