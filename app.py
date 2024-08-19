from flask import Flask, request, jsonify
import config

app = Flask(__name__)

#Criar uma pagina de login
@app.route('/')
def home():
    return "Bem vindo"

if __name__ == '__main__':
    app.run(debug=True)
