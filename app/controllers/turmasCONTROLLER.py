from flask import Flask, jsonify, request
from models import *
from models.turmasMODEL import diciTurma
from models.turmasMODEL import encontrar_turma_por_id
from models.turmasMODEL import criar_turma
from models.turmasMODEL import atualizar_turma
from models.turmasMODEL import deletar_turma
app = Flask(__name__)
class AlunoNaoEncontrado(Exception):
    pass

@app.route("/turmas", methods=['GET'])
def get_turmas():
    return jsonify(diciTurma['turmas'])

@app.route("/turmas/<int:idTurma>", methods=['GET'])
def get_turma_by_id(idTurma):
    turma = encontrar_turma_por_id(idTurma)
    if turma:
        return jsonify(turma)
    return jsonify({"erro": "Turma não encontrada"}), 404

@app.route("/turmas", methods=['POST'])
def create_turma():
    try:
        nova_turma = request.json
        criar_turma(nova_turma)
        return jsonify(nova_turma), 201
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Turma não criada"}), 404
    
@app.route("/turmas/<int:idTurma>", methods=['PUT'])
def update_turma(idTurma):
    dados = request.json
    try:
        atualizar_turma(idTurma, dados)
        return jsonify(encontrar_turma_por_id(idTurma))
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Turma não atualizada"}), 404
    
@app.route("/turmas/<int:idTurma>", methods=['DELETE'])
def delete_turma(idTurma):
    try:
        deletar_turma(idTurma)
        return jsonify({"mensagem": f"Turma com ID {idTurma} removida com sucesso"})
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Turma não deletado"}), 404
