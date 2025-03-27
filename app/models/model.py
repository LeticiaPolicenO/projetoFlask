
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

def getAlunos():
    return dici['alunos']