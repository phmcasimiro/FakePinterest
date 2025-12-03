from flask import render_template, url_for
from FakePinterest import app

# '/' rota raiz da aplicação.
@app.route('/')
def homepage(): # homepage() é a função que será chamada quando a rota '/' for acessada.
    return render_template('homepage.html') # render_template() é uma função que renderiza um template HTML.

# '/perfil/<usuario>' rota para a página do perfil.
# <usuario> é um parâmetro da rota.
@app.route("/perfil/<usuario>")
def perfil(usuario): # perfil() é a função que será chamada quando a rota '/perfil/<usuario>' for acessada.
    return render_template('perfil.html',usuario=usuario) # render_template() é uma função que renderiza um template HTML.