from flask import Flask, jsonify, request

dici = {
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
    ],
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
    ],
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

app = Flask(__name__)

# -------------------- ALUNOS --------------------

@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify(dici['alunos'])

@app.route("/alunos/<int:idAluno>", methods=['GET'])
def get_aluno_by_id(idAluno):
    aluno = next((a for a in dici['alunos'] if a['id'] == idAluno), None)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos", methods=['POST'])
def create_aluno():
    novo_aluno = request.json
    dici['alunos'].append(novo_aluno)
    return jsonify(novo_aluno), 201

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def update_aluno(idAluno):
    aluno = next((a for a in dici['alunos'] if a['id'] == idAluno), None)
    if aluno:
        dados = request.json
        aluno.update(dados)
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos/<int:idAluno>", methods=['DELETE'])
def delete_aluno(idAluno):
    aluno = next((a for a in dici['alunos'] if a['id'] == idAluno), None)
    if aluno:
        dici['alunos'].remove(aluno)
        return jsonify({"mensagem": f"Aluno com ID {idAluno} removido com sucesso"})
    return jsonify({"erro": "Aluno não encontrado"}), 404

# -------------------- PROFESSORES --------------------

@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(dici['professores'])

@app.route("/professores/<int:idProfessor>", methods=['GET'])
def get_professor_by_id(idProfessor):
    professor = next((p for p in dici['professores'] if p['id'] == idProfessor), None)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route("/professores", methods=['POST'])
def create_professor():
    novo_professor = request.json
    dici['professores'].append(novo_professor)
    return jsonify(novo_professor), 201

@app.route("/professores/<int:idProfessor>", methods=['PUT'])
def update_professor(idProfessor):
    professor = next((p for p in dici['professores'] if p['id'] == idProfessor), None)
    if professor:
        dados = request.json
        professor.update(dados)
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route("/professores/<int:idProfessor>", methods=['DELETE'])
def delete_professor(idProfessor):
    professor = next((p for p in dici['professores'] if p['id'] == idProfessor), None)
    if professor:
        dici['professores'].remove(professor)
        return jsonify({"mensagem": f"Professor com ID {idProfessor} removido com sucesso"})
    return jsonify({"erro": "Professor não encontrado"}), 404

# -------------------- TURMAS --------------------

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify(dici['turmas'])

@app.route("/turmas/<int:idTurma>", methods=['GET'])
def get_turma_by_id(idTurma):
    turma = next((t for t in dici['turmas'] if t['id'] == idTurma), None)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route("/turmas", methods=['POST'])
def create_turma():
    nova_turma = request.json
    dici['turmas'].append(nova_turma)
    return jsonify(nova_turma), 201

@app.route("/turmas/<int:idTurma>", methods=['PUT'])
def update_turma(idTurma):
    turma = next((t for t in dici['turmas'] if t['id'] == idTurma), None)
    if turma:
        dados = request.json
        turma.update(dados)
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route("/turmas/<int:idTurma>", methods=['DELETE'])
def delete_turma(idTurma):
    turma = next((t for t in dici['turmas'] if t['id'] == idTurma), None)
    if turma:
        dici['turmas'].remove(turma)
        return jsonify({"mensagem": f"Turma com ID {idTurma} removida com sucesso"})
    return jsonify({"erro": "Turma não encontrada"}), 404

if __name__ == "__main__":
    app.run(debug=True)
