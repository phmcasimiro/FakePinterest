# routes.py
# criado por: phmcasimiro em 05/12/2025
# Este arquivo contém as rotas da aplicação
# As rotas são usadas para mapear URLs para funções
# As rotas são usadas para renderizar templates HTML

from flask import render_template, url_for, redirect, flash
from FakePinterest import app, database, bcrypt
from FakePinterest.models import Usuarios, Fotos
from flask_login import login_required, login_user, logout_user, current_user
from FakePinterest.forms import FormLogin, FormCriarConta

# '/' rota raiz da aplicação.
@app.route('/', methods=['GET', 'POST'])
def homepage(): # homepage() é a função que será chamada quando a rota '/' for acessada.
    form_login = FormLogin() # form_login é a instância do formulário de login
    if form_login.validate_on_submit(): # validate_on_submit() é uma função que valida o formulário
        usuario = Usuarios.query.filter_by(email=form_login.email.data).first() # usuario é a instância do modelo Usuarios
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data): # check_password_hash() é uma função que verifica se a senha é correta
            login_user(usuario, remember=True) # login_user() é uma função que loga o usuário # remember é um booleano que define se o usuário deve ser lembrado
            return redirect(url_for('perfil', usuario=usuario.id_usuario)) # redirect() é uma função que redireciona para a rota raiz
    return render_template('homepage.html', form=form_login)# render_template() é uma função que renderiza um template HTML.

# '/criarconta' rota para a página de criar conta.
# criarconta() é a função que será chamada quando a rota '/criarconta' for acessada.
@app.route('/criarconta', methods=['GET', 'POST'])
def criarconta():
    form_criarconta = FormCriarConta() # form_criarconta é a instância do formulário de criar conta
    if form_criarconta.validate_on_submit(): # validate_on_submit() é uma função que valida o formulário
        senha_criptografada = bcrypt.generate_password_hash(form_criarconta.senha.data).decode('utf-8') # senha_criptografada é a senha criptografada
        usuario = Usuarios(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_criptografada) # usuario é a instância do modelo Usuarios
        database.session.add(usuario) # add() é uma função que adiciona o usuário ao banco de dados
        database.session.commit() # commit() é uma função que salva as alterações no banco de dados
        flash('Conta criada com sucesso!', 'sucesso') # flash() é uma função que exibe uma mensagem na tela
        login_user(usuario, remember=True) # login_user() é uma função que loga o usuário
        return redirect(url_for('perfil', usuario=usuario.id_usuario)) # redirect() é uma função que redireciona para a rota raiz
    return render_template('criarconta.html', form=form_criarconta) # render_template() é uma função que renderiza um template HTML.

# '/perfil/<usuario>' rota para a página do perfil.
# <usuario> é um parâmetro da rota.
@app.route("/perfil/<id_usuario>")
@login_required
def perfil(id_usuario): # perfil() é a função que será chamada quando a rota '/perfil/<usuario>' for acessada.
    if int(id_usuario) == int(current_user.id): # Usuário visitando seu próprio perfil
        return render_template('perfil.html',usuario=current_user) # render_template() é uma função que renderiza um template HTML.
    else:
        usuario = Usuarios.query.get(id_usuario) # usuario é a instância do modelo Usuarios # usuario recebe o id do usuario
        return render_template('perfil.html',usuario=usuario) # render_template() é uma função que renderiza um template HTML.

@app.route("/logout") # logout() é a função que será chamada quando a rota '/logout' for acessada.
@login_required # @login_required é um decorator que garante que o usuário esteja logado para acessar a rota
def logout(): # logout() é a função que será chamada quando a rota '/logout' for acessada.
    logout_user() # logout_user() é uma função que desloga o usuário
    return redirect(url_for('homepage')) # redirect() é uma função que redireciona para a rota raiz