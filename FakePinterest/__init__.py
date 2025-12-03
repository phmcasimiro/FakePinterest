from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask é a classe que será usada para criar a aplicação.
app = Flask(__name__)

# Inicializa o banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db' # Define a URI do banco de dados
database = SQLAlchemy(app) # Inicializa o banco de dados

from FakePinterest import routes