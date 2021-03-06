import PySimpleGUI as sg

from app.usuario.controlador import Controlador
from app.produto.apresentacao import ApresentacaoProduto

class ApresentacaoUsuario:

    def __init__(self):
        self.__controlador = Controlador(self)
        self.__apresentacao_produto = ApresentacaoProduto(self)
        self.__container = []
        self.__window = sg.Window(
            'Autenticação', self.__container, font=('Arial', 12))
    
    @property
    def window(self) -> sg.Window:
        return self.__window
    
    @property
    def apresentacao_produto(self) -> ApresentacaoProduto:
        return self.__apresentacao_produto

    def inicia(self, tela_incial = 'LOGIN'):
        """Inicia a apresentação de login."""
        self.__controlador.le_eventos(tela_incial)
    
    def login(self):
        """Tela de login, realiza o login do usuário"""
        linha0 = [sg.Text('LOGIN')]
        linha1 = [sg.Text('Nome:'), sg.InputText('', key='nome')]
        linha2 = [
            sg.Text('Senha:'), sg.InputText('', key='senha', password_char='*')]
        linha3 = [sg.Button('Login')]
        
        self.__container = [linha0, linha1, linha2, linha3]
        self.__window = sg.Window(
            'Autenticação', self.__container, font=('Arial', 12))

    def cria_usuario(self):
        """Tela para criação do usuário."""
        linha0 = [sg.Text('Nome:'), sg.InputText('', key='nome')]
        linha1 = [
            sg.Text('Senha:'), sg.InputText('', key='senha', password_char='*')]
        linha2 = [sg.Button('Criar'), sg.Button('Cancelar')]

        self.__container = [linha0, linha1, linha2]
        self.__window = sg.Window(
            'Criar Usuário', self.__container, font=('Arial', 12))
