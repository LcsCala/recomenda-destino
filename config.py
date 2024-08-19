#Configuração para conectar com postgre
#E também declarar as funções aqui
import psycopg2

coneccao = psycopg2.connect(
    database = 'country_finder',
    user = 'postgres',
    password = '99!21?80',
    host = 'localhost',
    port = '5432'
)

#Executa meus comandos dentro dentro do postgre
curs = coneccao.cursor()
#Vai conter todos os registros retornado por 'curs'
resultados = curs.fetchall()


#Confirma todas as alterações feitas na transação atual do banco de dados
commit = coneccao.commit()


#Fechar minha conecção com o banco de dados (Por uma questão de segurança)
fecha_conec = coneccao.close()
#Fecha o meu cursor
fehca_cur = curs.close()