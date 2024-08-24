#Código configurando o flask_login pra desenvolver o sistema no projeto
from flask_login import LoginManager,UserMixin, login_user, login_required, logout_user, current_user
import bd
import app


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#Criando a classe 'usuário'
class Usuario (UserMixin):
    def __init__(self, id, nickname, senha):
        self.id = id
        self.nickname = nickname
        self.senha = senha

#Função para conseguir os dados de um usuário
#Se o usuário existir vai permitir que ele logue no site
def get_usuario_nome(nickname):
    conexao = bd.conectar()
    curs = conexao.cursor()

    curs.execute('SELECT * FROM usuario WHERE nickname =%s', (nickname,))
    user = curs.fetchone() #Vai retornar toda linha do 'nickname'

    curs.close()
    conexao.close()

    if user:
        return Usuario(id=user[0], nickname=user[1], senha=user[2])
    return None