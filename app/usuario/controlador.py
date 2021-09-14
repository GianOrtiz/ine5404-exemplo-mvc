import PySimpleGUI as sg

from typing import List

from app.usuario.usuario import Usuario
from app.usuario.dao import DAOUsuario

class Controlador:

    def __init__(self, apresentacao):
        self.__dao = DAOUsuario()
        self.__apresentacao = apresentacao

        # Se os usuários estiverem vazio, cria o usuário padrão
        usuarios = self.__dao.get_all()
        if len(usuarios) == 0:
            self.__dao.add('default', Usuario('default', 'default'))

    def cria_usuario(self, nome: str, senha: str) -> Usuario:
        """Cria um novo usuário no sistema

        Parameters
        ----------
        nome : str
            Nome do usuário
        senha : str
            Senha do usuário
        
        Returns
        -------
        Usuario
            Usuário criado
        """
        usuario = Usuario(nome, senha)
        self.__dao.add(nome, usuario)
        return usuario
        
    def obtem_usuario(self, nome: str) -> Usuario:
        """Retorna os usuários

        Parameters
        ----------
        nome : str
            Nome do usuário para retornar

        Returns
        -------
        Usuario
            O usuário selecionado
        """
        return self.__dao.get(nome)

    def remove_usuario(self, nome: str):
        """Remove um usuário

        Parameters
        ----------
        nome : str
            Nome do usuário para remover
        """
        self.__dao.remove(nome)

    def atualiza_usuario(self, nome: str, senha: str):
        """Atualiza as informações de um usuário
        
        Parameters
        ----------
        nome : str
            Nome do usuário para selecionar
        senha : str
            Nova senha do usuário
        """
        usuario = self.__dao.get(nome)
        if usuario is not None:
            self.__dao.remove(nome)
            usuario.senha = senha
            self.__dao.add(nome, usuario)

    def login(self, nome: str, senha: str) -> str:
        """Realiza o login de um usuário"""
        if nome == '' or senha == '':
            return 'Nome e senha são obrigatórios'

        usuario = self.obtem_usuario(nome)    
        if usuario is not None:
            senha_igual = usuario.compara_senha(senha)
            if senha_igual:
                return ''
        return 'Nome ou senha incorretos'

    def le_eventos(self, tela_inicial = 'LOGIN'):
        """
        Lê os eventos da tela e reage de acordo, abrindo e usando CRUD para
        as operações.
        """
    
        if tela_inicial == 'LOGIN':
            self.__apresentacao.login()
        else:
            self.__apresentacao.cria_usuario()

        rodando = True
        resultado = ''
        while rodando:
            event, values = self.__apresentacao.window.read()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Login':
                resposta = self.login(values['nome'], values['senha'])
                if resposta == '':
                    resultado = ''
                    rodando = False
                    self.__apresentacao.window.close()
                    self.__apresentacao.apresentacao_produto.inicia()
                else:
                    resultado = resposta
            elif event == 'Criar':
                try:
                    self.cria_usuario(values['nome'], values['senha'])
                    resultado = ''
                    rodando = False
                    self.__apresentacao.window.close()
                    self.__apresentacao.apresentacao_produto.inicia()
                except:
                    resultado = 'Nome ou senha já utilizado'
            elif event == 'Cancelar':
                self.__apresentacao.window.close()
                self.__apresentacao.apresentacao_produto.inicia()

            if resultado != '':
                sg.popup('RESULTADO: ', resultado)

        self.__apresentacao.window.close()