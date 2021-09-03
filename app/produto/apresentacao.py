import PySimpleGUI as sg

from app.produto.controlador import Controlador
from app.util import le_float, le_string, le_int, nao_eh_vazio

PRODUTOS_POR_LINHA = 4

class ApresentacaoProduto:

    def __init__(self):
        self.__controlador = Controlador(self)
        self.__container = []
        self.__window = sg.Window('Estoque', self.__container, font=('Arial', 12))

    @property
    def window(self) -> sg.Window:
        return self.__window

    def inicia(self):
        """Inicia a apresentação dos produtos como um estoque"""
        self.__controlador.le_eventos()

    def tela_produtos(self):
        """Tela principal dos produtos, mostra todos os produtos"""
        produtos = self.__controlador.produtos()
        produtos_frames = []
        linha = []
        for produto in produtos:
            if len(linha) == PRODUTOS_POR_LINHA:
                produtos_frames.append(linha)
                linha = []
            linha.append(
                sg.Frame(
                    produto.nome,
                    [
                        [sg.Text('Código'), sg.Text(produto.codigo)],
                        [sg.Text('Valor(R$)'), sg.Text(str(produto.valor))],
                        [sg.Text('Quantidade'), sg.Text(str(produto.quantidade))],
                        [sg.Button('Editar', key='edit-{0}'.format(produto.codigo))],
                        [sg.Button('Remover', key='remove-{0}'.format(produto.codigo))],
                    ],
                    key=produto.codigo,
                ),
            )
        produtos_frames.append(linha)

        self.__window.close()
        self.__container = [[sg.Button('Adicionar Produto', key='add')], produtos_frames]
        new_window = sg.Window('Produtos', self.__container, font=('Arial', 12), size=(800, 600))
        self.__window = new_window

    def tela_edicao(self, codigo: str):
        """Permite que o usuário edite um produto"""
        produto = self.__controlador.obtem_produto(codigo)
        linha0 = [sg.Text('Código'), sg.Text(produto.codigo)]
        linha1 = [sg.Text('Nome'), sg.InputText(produto.nome, key='nome')]
        linha2 = [sg.Text('Valor(R$)'), sg.InputText(produto.valor, key='valor')]
        linha3 = [sg.Text('Quantidade'), sg.InputText(produto.quantidade, key='quantidade')]
        linha4 = [sg.Button('Cancelar', key='cancel'), sg.Button('Salvar', key='save-{0}'.format(produto.codigo))]
        self.__container = [
            linha0,
            linha1,
            linha2,
            linha3,
            linha4,
        ]
        self.__window = sg.Window('Edição {0}'.format(codigo), self.__container, font=('Arial', 12))

    def tela_adicionar(self):
        """Tela para adicionar novo produto"""
        linha0 = [sg.Text('Código'), sg.InputText('', key='codigo')]
        linha1 = [sg.Text('Nome'), sg.InputText('', key='nome')]
        linha2 = [sg.Text('Valor(R$)'), sg.InputText('', key='valor')]
        linha3 = [sg.Text('Quantidade'), sg.InputText('', key='quantidade')]
        linha4 = [sg.Button('Cancelar', key='cancel'), sg.Button('Criar', key='create')]
        self.__container = [
            linha0,
            linha1,
            linha2,
            linha3,
            linha4,
        ]
        self.__window = sg.Window('Adicionar produto', self.__container, font=('Arial', 12))
