from app.usuario.controlador import Controlador
from app.produto.apresentacao import ApresentacaoProduto
from app.util import le_string, nao_eh_vazio

class ApresentacaoUsuario:

    def __init__(self):
        self.__controlador = Controlador()
        self.__apresentacao_produto = ApresentacaoProduto()
    
    def login(self):
        """Tela de login, realiza o login do usuário"""
        resposta = input('Você deve entrar no sistema, deseja entrar?[sim|nao]')
        if resposta == 'sim':
            nome = le_string('Nome de usuário: ', nao_eh_vazio)
            senha = le_string('Senha de usuário: ', nao_eh_vazio)
            usuario = self.__controlador.obtem_usuario(nome)
            while usuario is None or not usuario.compara_senha(senha) :
                print('Nome ou senha de usuário incorretos, tente novamente!\n')
                nome = le_string('Nome de usuário: ', nao_eh_vazio)
                senha = le_string('Senha de usuário: ', nao_eh_vazio)
                usuario = self.__controlador.obtem_usuario(nome)
            self.__apresentacao_produto.opcoes()
        else:
            return
