from FakePinterest import app # importa o app do arquivo __init__.py

# __name__ é uma variável que é definida automaticamente pelo Python. 
# Ela é usada para verificar se o arquivo está sendo executado diretamente ou se está sendo importado como um módulo.
if __name__ == '__main__':
    app.run(debug=True) # Debug=True permite que o servidor reinicie automaticamente quando houver alterações no código.


