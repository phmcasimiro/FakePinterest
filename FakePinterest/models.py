# models.py

from FakePinterest import database
from datetime import datetime

class Usuarios(database.Model): # Usuario herda de database.Model
    #__tablename__ = 'usuarios' # nome da tabela no banco de dados
    id = database.Column(database.Integer, primary_key=True) # id é a chave primária
    username = database.Column(database.String(100), nullable=False) # nome é obrigatório
    email = database.Column(database.String(100), nullable=False, unique=True) # email é obrigatório
    senha = database.Column(database.String(100), nullable=False) # senha é obrigatória
    fotos = database.relationship('Fotos', backref='usuario', lazy=True) # relacionamento com a tabela de fotos
    pass

class Fotos(database.Model):
    #__tablename__ = 'fotos' # nome da tabela no banco de dados
    id = database.Column(database.Integer, primary_key=True) # id é a chave primária
    imagem = database.Column(database.String(200), default='default.png') # imagem é obrigatória
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow()) # data de criação é obrigatória
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False) # usuario_id é obrigatório
