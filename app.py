from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config.from_object('config.Config') #Chama a classe 'Config' no arquivo 'config'
db = SQLAlchemy(app) #Cria uma instância do SQLAlchemy e a associa ao aplicativo Flask

#Criar uma pagina de login
@app.route('/')
def home():
    return "Bem vindo"

if __name__ == '__main__':
    app.run(debug=True)
