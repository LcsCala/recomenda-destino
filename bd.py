#Configuração para conectar com postgre
#E também declarar as variaveis aqui
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega as variáveis do .env que vai conter as informações que não desejoj que apareça

bd_senha = os.getenv("bd_senha")


def conectar():
    return psycopg2.connect(
        database = 'country_finder',
        user = 'postgres',
        password = bd_senha,
        host = 'localhost',
        port = '5432'
    )

def mostra_tabela():
    conexao = conectar()

    #Executa meus comandos dentro dentro do postgre
    curs = conexao.cursor()
    curs.execute('SELECT * FROM paises')

    #Vai conter todos os registros retornado por 'curs'
    resultados = curs.fetchall()

    #Fecha o meu cursor
    curs.close()
    #Fechar minha conexão com o banco de dados (Por uma questão de segurança)
    conexao.close()
    return resultados