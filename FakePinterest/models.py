# models.py
# criado por: phmcasimiro em 05/12/2025
# Este arquivo contém as classes que representam as tabelas do banco de dados
# As classes são usadas para criar as tabelas no banco de dados
# As classes herdam de database.Model e UserMixin (determina que a classe gerenciará o login)


from FakePinterest import database, login_manager
from datetime import datetime
from flask_login import UserMixin # UserMixin é uma classe que fornece funcionalidades de usuário e informa qual classe gerenciará o login

# Decorator que define a função que será chamada para carregar o usuário no sistema de login
@login_manager.user_loader # decorator que define a função que será chamada para carregar o usuário
def load_user(id): # load_user() é a função que será chamada para carregar o usuário
    return Usuarios.query.get(int(id)) # Usuarios.query.get(int(id)) é a função que será chamada para carregar o usuário

class Usuarios(database.Model, UserMixin): # Usuario herda de database.Model e UserMixin (determina que a classe gerenciará o login)
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
