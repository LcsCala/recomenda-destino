from flask import Flask, request, jsonify
import bd

app = Flask(__name__)

#Criar uma pagina de login
@app.route('/')
def home():
    return "Bem vindo"

#Pagina que mostra a tabela
@app.route('/consulta', methods = ['GET'])
def tabela ():
    resultados = bd.mostra_tabela()
    colunas = [
        'coluna1', 
        'coluna2',
        'coluna3',
        'coluna4',
        'coluna5',
        'coluna6',
        'coluna7',
        'coluna8',
        'coluna9',
        'coluna10',
        'coluna11',
        'coluna12',
        'coluna13',
        ]
    resultados_formatados = [dict(zip(colunas, linha)) for linha in resultados]
    return jsonify(resultados_formatados)

if __name__ == '__main__':
    app.run(debug=True)
