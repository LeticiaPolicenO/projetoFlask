from flask import Flask, jsonify, request
from models.alunosMODEL import diciAlunos
from models import *
from models.alunosMODEL import encontre_aluno_por_ID
from models.alunosMODEL import criar_alunitos
from models.alunosMODEL import atualizar_aluno
from models.alunosMODEL import deletar_aluno


app = Flask(__name__)

class AlunoNaoEncontrado(Exception):
    pass


@app.route("/alunos", methods=['GET'])
def get_alunos():
    return jsonify(diciAlunos['alunos'])

@app.route("/alunos/<int:idAluno>", methods=['GET'])
def get_aluno_by_id(idAluno):
    aluno = encontre_aluno_por_ID(idAluno)
    if aluno:
        return jsonify(aluno)
    return jsonify({"erro": "Aluno não encontrado"}), 404

@app.route("/alunos", methods=['POST'])
def create_aluno():
    novo_aluno = request.json
    try:
        criar_alunitos(novo_aluno)
        return jsonify(novo_aluno), 201
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Aluno não criado"}), 404

@app.route("/alunos/<int:idAluno>", methods=['PUT'])
def update_aluno(idAluno):
    data = request.json
    try:
        atualizar_aluno(idAluno, data)
        return jsonify(encontre_aluno_por_ID(idAluno))
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Aluno não atualizado"}), 404
    
@app.route("/alunos/<int:idAluno>", methods=['DELETE'])
def delete_aluno(idAluno):
    try: 
        deletar_aluno(idAluno)
        return '',204
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Aluno não deletado"}), 404
