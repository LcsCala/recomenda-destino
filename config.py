#Configuração para conectar com postgre
import psycopg2

coneccao = psycopg2.connect(
    database = '',
    user = '',
    password = '',
    host = '',
    port = ''
)

#Executa meus comandos dentro dentro do postgre
curs = coneccao.cursor()

#Confirma todas as alterações feitas na transação atual do banco de dados
coneccao.commit()