from sqlalchemy import create_engine, Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

Base = declarative_base()

class Aluno(Base):
    _tablename_ = 'alunos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    email = Column(String)
    _notas = Column(String)

    @hybrid_property
    def notas(self):
        return [float(nota) for nota in self._notas.split(',')]

    @notas.setter
    def notas(self, value):
        self._notas = ','.join(str(v) for v in value)

class Professor(Base):
    _tablename_ = 'professores'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    disciplina = Column(String)
    email = Column(String)

class Turma(Base):
    _tablename_ = 'turmas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    semestre = Column(Integer)
    professor_id = Column(Integer, ForeignKey('professores.id'))

class AlunoTurma(Base):
    _tablename_ = 'alunos_turmas'

    id = Column(Integer, primary_key=True)
    aluno_id = Column(Integer, ForeignKey('alunos.id'))
    turma_id = Column(Integer, ForeignKey('turmas.id'))

# Configuração do banco de dados
db = create_engine("sqlite:///escola.db")
Session = sessionmaker(bind=db)
session = Session()