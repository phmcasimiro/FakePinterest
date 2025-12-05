# __init__.py
# criado por: phmcasimiro em 05/12/2025
# Este arquivo contém as classes que representam as tabelas do banco de dados
# As classes são usadas para criar as tabelas no banco de dados
# As classes herdam de database.Model e UserMixin (determina que a classe gerenciará o login)

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt


# Flask é a classe que será usada para criar a aplicação.
app = Flask(__name__)

# Define a URI do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' 

# Define a chave secreta
app.config['SECRET_KEY'] = 'f2de131c3698b1986336ad68fa26263c'


# Inicializa o banco de dados
database = SQLAlchemy(app) # Inicializa o banco de dados
bcrypt = Bcrypt(app) # Inicializa o bcrypt
login_manager = LoginManager(app) # Inicializa o login manager
login_manager.login_view = 'homepage' # Define a view/route de login

from FakePinterest import routes