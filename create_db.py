# create_db.py
# Script para criação de banco de dados
# Pode ser executado uma vez para criar o banco de dados e depois excluído
# Criado por PHMCasimiro em 03/12/2025

from FakePinterest import database, app
from FakePinterest.models import Usuarios, Fotos

with app.app_context(): # Cria o contexto da aplicação
    database.create_all() # Cria o banco de dados

print("Banco de dados criado com sucesso!")
