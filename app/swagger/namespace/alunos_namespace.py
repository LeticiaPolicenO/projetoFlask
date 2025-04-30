from flask_restx import Namespace, Resource, fields
from models.alunosMODEL import listar_alunos, criar_alunitos, encontre_aluno_por_ID, atualizar_aluno, deletar_aluno

alunos_ns = Namespace("alunos", description="Operações relacionadas aos alunos.")

aluno_model = alunos_ns.model("Aluno", {
    "nome": fields.String(required=True, description="Nome do aluno"),
    "idade": fields.Integer(required=True, description="Idade do aluno"),
    "email": fields.String(required=True, description="Email do aluno"),
    "notas": fields.List(fields.Float, required=True, description="Notas"),
})

aluno_output_model = alunos_ns.model("AlunoOutput", {
    "id": fields.Integer(description="ID do aluno"),
    "nome": fields.String(description="Nome do aluno"),
    "idade": fields.Integer(description="Idade do aluno"),
    "email": fields.String(description="Email do aluno"),
    "notas": fields.List(fields.Float, description="Notas do aluno"),
})

@alunos_ns.route("/")
class AlunosResource(Resource):
    @alunos_ns.marshal_list_with(aluno_output_model)
    def get(self):
        return listar_alunos()

    @alunos_ns.expect(aluno_model)
    def post(self):
        data = alunos_ns.payload
        response, status_code = criar_alunitos(data)
        return response, status_code

@alunos_ns.route("/<int:id_aluno>")
class AlunoIdResource(Resource):
    @alunos_ns.marshal_with(aluno_output_model)
    def get(self, id_aluno):
        return encontre_aluno_por_ID(id_aluno)

    @alunos_ns.expect(aluno_model)
    def put(self, id_aluno):
        data = alunos_ns.payload
        atualizar_aluno(id_aluno, data)
        return data, 200

    def delete(self, id_aluno):
        deletar_aluno(id_aluno)
        return {"message": "Aluno excluído com sucesso"}, 200
