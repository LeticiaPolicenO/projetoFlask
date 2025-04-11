from flask import Flask, jsonify, request
from models import *
from models.professoresMODEL import diciProfessor
from models.professoresMODEL import encontre_professor_por_id
from models.professoresMODEL import criar_professor
from models.professoresMODEL import atualizar_professor
from models.professoresMODEL import deletar_professor
app = Flask(__name__)
class AlunoNaoEncontrado(Exception):
    pass

@app.route("/professores", methods=['GET'])
def get_professores():
    return jsonify(diciProfessor['professores'])

@app.route("/professores/<int:idProfessor>", methods=['GET'])
def get_professor_by_id(idProfessor):
    professor = encontre_professor_por_id(idProfessor)
    if professor:
        return jsonify(professor)
    return jsonify({"erro": "Professor não encontrado"}), 404

@app.route("/professores", methods=['POST'])
def create_professor():
    novo_professor = request.json
    criar_professor(novo_professor)
    return jsonify(novo_professor), 201

@app.route("/professores/<int:idProfessor>", methods=['PUT'])
def update_professor(idProfessor):
    dados = request.json
    try:
        atualizar_professor(idProfessor, dados)
        return jsonify(encontre_professor_por_id(idProfessor))
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Professor não atualizado"}), 404
    
@app.route("/professores/<int:idProfessor>", methods=['DELETE'])
def delete_professor(idProfessor):
    try:
        deletar_professor(idProfessor)
        return '',204
    except AlunoNaoEncontrado:
        return jsonify({"erro": "Professor não deletado"}), 404

