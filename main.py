# main.py
# criado por: phmcasimiro em 05/12/2025
# Este arquivo contém a função principal da aplicação
# A função principal é usada para iniciar a aplicação
# A função principal é usada para iniciar o servidor

from FakePinterest import app # importa o app do arquivo __init__.py

# __name__ é uma variável que é definida automaticamente pelo Python. 
# Ela é usada para verificar se o arquivo está sendo executado diretamente ou se está sendo importado como um módulo.
if __name__ == '__main__':
    app.run(debug=True) # Debug=True permite que o servidor reinicie automaticamente quando houver alterações no código.


