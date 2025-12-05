# forms.py
# criado por: phmcasimiro em 05/12/2025
# Este arquivo contém as classes que representam os formulários da aplicação
# As classes são usadas para criar os formulários da aplicação
# As classes herdam de Form

# FlaskForm é a classe que será usada para criar os formulários
from flask_wtf import FlaskForm 
# StringField é o campo de texto, PasswordField é o campo de senha, SubmitField é o botão de submit
from wtforms import StringField, PasswordField, SubmitField, DateField
# DataRequired é o validador de dados, Email é o validador de email, EqualTo é o validador de igualdade, Length é o validador de comprimento
from wtforms.validators import DataRequired, Email, EqualTo, Length, ValidationError
# Importa a classe Usuarios do arquivo models.py para ser usada na validação do email
from FakePinterest.models import Usuarios

class FormLogin(FlaskForm):
    # email é obrigatório e deve ser um email
    email = StringField('E-mail', validators=[DataRequired(), Email()]) 
    # senha é obrigatória
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    # submit é o botão de confirmação
    submit = SubmitField('Fazer Login')

class FormCriarConta(FlaskForm): # Formulário de Criação de Conta com os campos e respectivas validações
    # DEFINIR CAMPO email
    email = StringField('E-mail', validators=[DataRequired(), Email()]) 
    
    # DEFINIR FUNÇÃO DE VALIDAÇÃO
    # Esta função será executada AUTOMATICAMENTE pelo WTForms antes de form_criarconta.validate_on_submit()
    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first() 
        if usuario:
            # Se o usuário existir, o WTForms capta esta exceção e a exibe no formulário
            raise ValidationError('Este e-mail já está em uso. Cadastre-se com outro e-mail ou faça login.')

    # username é obrigatório
    username = StringField('Username', validators=[DataRequired()])
    
    # nome é obrigatório
    nome = StringField('Nome', validators=[DataRequired()])
    
    # senha é obrigatória e deve ter entre 6 e 20 caracteres
    senha = PasswordField('Senha', validators=[DataRequired(), Length(min=6, max=20)])
    
    # confirmar senha é obrigatória e deve ser igual a senha, deve ter entre 6 e 20 caracteres e deve ser igual a senha
    confirmar_senha = PasswordField('Confirmar Senha', validators=[DataRequired(), Length(min=6, max=20), EqualTo('senha')]) 
    
    # submit é o botão de confirmação
    submit = SubmitField('Fazer Login') 


