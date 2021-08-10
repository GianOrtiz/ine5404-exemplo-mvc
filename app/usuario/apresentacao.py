import PySimpleGUI as sg

from app.usuario.controlador import Controlador
from app.produto.apresentacao import ApresentacaoProduto

class ApresentacaoUsuario:

    def __init__(self):
        self.__controlador = Controlador()
        self.__apresentacao_produto = ApresentacaoProduto()
        self.__container = []
        self.__window = sg.Window('Autenticação', self.__container, font=('Arial', 12))
    
    def inicia(self):
        """Inicia a apresentação de login."""
        self.login()

        rodando = True
        resultado = ''
        while rodando:
            event, values = self.le_eventos()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif event == 'Login':
                resposta = self.__controlador.login(values['nome'], values['senha'])
                if resposta == '':
                    resultado = ''
                    rodando = False
                    self.__window.close()
                    self.__apresentacao_produto.inicia()
                else:
                    resultado = resposta

            if resultado != '':
                sg.popup('RESULTADO: ', resultado)

        self.__window.close()
    
    def login(self):
        """Tela de login, realiza o login do usuário"""
        linha0 = [sg.Text('LOGIN')]
        linha1 = [sg.Text('Nome:'), sg.InputText('', key='nome')]
        linha2 = [sg.Text('Senha:'), sg.InputText('', key='senha', password_char='*')]
        linha3 = [sg.Button('Login')]
        
        self.__container = [linha0, linha1, linha2, linha3]
        self.__window = sg.Window('Autenticação', self.__container, font=('Arial', 12))

    def le_eventos(self):
        """Lê os eventos da tela de autenticação"""
        return self.__window.read()
