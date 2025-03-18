import unittest
import json
from app import app  # Certifique-se de que a importação está correta

class TestAPI(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        cls.client.testing = True

    # ===================== Testes CRUD para Alunos =====================

    def test_create_aluno(self):
        try:
            novo_aluno = {
                "id": 7,
                "nome": "Lucas Lima",
                "idade": 21,
                "notas": [8.5, 7.3, 9.2],
                "email": "lucas.lima@email.com"
            }
            response = self.client.post('/alunos', json=novo_aluno)
            self.assertEqual(response.status_code, 201)
            self.assertEqual(json.loads(response.data)["nome"], novo_aluno["nome"])
        except Exception as e:
            self.fail(f"Erro no teste test_create_aluno: {e}")

    def test_get_alunos(self):
        try:
            response = self.client.get('/alunos')
            self.assertEqual(response.status_code, 200)
            self.assertIn('alunos', json.loads(response.data).keys())
        except Exception as e:
            self.fail(f"Erro no teste test_get_alunos: {e}")

    def test_get_aluno_by_id(self):
        try:
            response = self.client.get('/alunos/1')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["nome"], "Amanda Silva")
        except Exception as e:
            self.fail(f"Erro no teste test_get_aluno_by_id: {e}")

    def test_update_aluno(self):
        try:
            aluno_atualizado = {
                "nome": "Amanda Souza",
                "idade": 20,
                "notas": [8.5, 7.5, 9.0],
                "email": "amanda.souza@email.com"
            }
            response = self.client.put('/alunos/1', json=aluno_atualizado)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["nome"], aluno_atualizado["nome"])
        except Exception as e:
            self.fail(f"Erro no teste test_update_aluno: {e}")

    def test_delete_aluno(self):
        try:
            response = self.client.delete('/alunos/1')
            self.assertEqual(response.status_code, 200)
            self.assertIn('Aluno com ID 1 removido com sucesso', json.loads(response.data)["mensagem"])
        except Exception as e:
            self.fail(f"Erro no teste test_delete_aluno: {e}")

    # ===================== Testes CRUD para Alunos com falha =====================

    def test_create_aluno_sem_nome(self):
        try:
            novo_aluno = {
                "id": 8,
                "idade": 22,
                "notas": [7.5, 6.2, 8.9],
                "email": "sem.nome@email.com"
            }
            response = self.client.post('/alunos', json=novo_aluno)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Nome é obrigatório", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_create_aluno_sem_nome: {e}")

    def test_get_aluno_inexistente(self):
        try:
            response = self.client.get('/alunos/999')  # ID inexistente
            self.assertEqual(response.status_code, 404)
            self.assertIn("Aluno não encontrado", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_get_aluno_inexistente: {e}")

    def test_update_aluno_inexistente(self):
        try:
            aluno_atualizado = {
                "nome": "João Silva",
                "idade": 23,
                "notas": [9.5, 8.0, 9.8],
                "email": "joao.silva@email.com"
            }
            response = self.client.put('/alunos/999', json=aluno_atualizado)  # ID inexistente
            self.assertEqual(response.status_code, 404)
            self.assertIn("Aluno não encontrado", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_update_aluno_inexistente: {e}")

    def test_delete_aluno_inexistente(self):
        try:
            response = self.client.delete('/alunos/999')  # ID inexistente
            self.assertEqual(response.status_code, 404)
            self.assertIn("Aluno não encontrado", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_delete_aluno_inexistente: {e}")

    # ===================== Testes adicionais de falhas e limites de dados =====================

    def test_create_aluno_com_id_duplicado(self):
        try:
            aluno_com_id_duplicado = {
                "id": 1,
                "nome": "Carlos Oliveira",
                "idade": 19,
                "notas": [8.0, 7.0, 6.5],
                "email": "carlos.oliveira@email.com"
            }
            response = self.client.post('/alunos', json=aluno_com_id_duplicado)
            self.assertEqual(response.status_code, 400)
            self.assertIn("ID já existe", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_create_aluno_com_id_duplicado: {e}")

    def test_update_aluno_com_email_invalido(self):
        try:
            aluno_atualizado = {
                "nome": "Maria Oliveira",
                "idade": 22,
                "notas": [9.5, 8.5, 7.0],
                "email": "emailinvalido"
            }
            response = self.client.put('/alunos/1', json=aluno_atualizado)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Email inválido", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_update_aluno_com_email_invalido: {e}")

    def test_create_aluno_com_notas_invalidas(self):
        try:
            aluno_com_notas_invalidas = {
                "id": 9,
                "nome": "Ricardo Lima",
                "idade": 20,
                "notas": [12.5, -1.0, 7.5],  # Notas inválidas
                "email": "ricardo.lima@email.com"
            }
            response = self.client.post('/alunos', json=aluno_com_notas_invalidas)
            self.assertEqual(response.status_code, 400)
            self.assertIn("Notas inválidas", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_create_aluno_com_notas_invalidas: {e}")

    def test_delete_aluno_sem_autorizacao(self):
        try:
            # Tentando deletar sem permissão (supondo que precise de autenticação)
            response = self.client.delete('/alunos/1')
            self.assertEqual(response.status_code, 401)
            self.assertIn("Autenticação necessária", json.loads(response.data)["erro"])
        except Exception as e:
            self.fail(f"Erro no teste test_delete_aluno_sem_autorizacao: {e}")

    def test_get_alunos_vazio(self):
        try:
            response = self.client.get('/alunos')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.data)["alunos"], [])
        except Exception as e:
            self.fail(f"Erro no teste test_get_alunos_vazio: {e}")

if __name__ == "__main__":
    unittest.main()
