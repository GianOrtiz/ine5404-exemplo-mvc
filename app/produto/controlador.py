import PySimpleGUI as sg

from typing import List

from app.produto.produto import Produto
from app.produto.dao import DAOProduto

class Controlador:

    def __init__(self, apresentacao):
        self.__dao = DAOProduto()
        self.__apresentacao = apresentacao
        
    def cria_produto(self, codigo: str, nome: str, valor: float, quantidade: int) -> Produto:
        """Cria um novo produto no sistema. Se o código já existir, não cria

        Parameters
        ----------
        codigo : str
            Código único do produto
        nome : str
            Nome do produto
        valor : float
            Valor unitário do produto
        quantidade : int
            Quantidade inicial do produto
        
        Returns
        -------
        Produto
            Produto criado
        """
        produto = Produto(codigo=codigo, nome=nome, valor=valor, quantidade=quantidade)
        self.__dao.add(codigo, produto)
        return produto

    def obtem_produto(self, codigo: str) -> Produto:
        """Retorna os produto

        Parameters
        ----------
        codigo : str
            Código do produto

        Returns
        -------
        Produto
            O produto selecionado
        """
        return self.__dao.get(codigo)
    
    def remove_produto(self, codigo: str):
        """Remove um produto

        Parameters
        ----------
        codigo : str
            Código do produto
        """
        return self.__dao.remove(codigo)

    def atualiza_produto(self, codigo: str, nome: str=None, valor: float=None, quantidade: int=None):
        """Atualiza as informações de um produto
        
        Parameters
        ----------
        codigo : str
            Código do produto para atualizar
        nome : str
            Nova nome do produto
        valor : float
            Novo valor unitário do produto
        quantidade : int
            Nova quantidade do produto
        """
        produto = self.__dao.get(codigo)
        if produto is None:
            return
    
        if nome is not None:
            produto.nome = nome
        if valor is not None:
            produto.valor = valor
        if quantidade is not None:
            produto.quantidade = quantidade
        self.__dao.remove(codigo)
        self.__dao.add(codigo, produto)

    def produtos(self) -> List[Produto]:
        """Obtem todos os produtos
        
        Returns
        -------
        list
            A lista de produtos
        """
        produtos = self.__dao.get_all()
        return produtos

    def le_eventos(self):
        """
        Lê os eventos da tela e reage de acordo, abrindo e usando CRUD para
        as operações.
        """

        self.__apresentacao.tela_produtos()

        rodando = True
        while rodando:
            event, values = self.__apresentacao.window.read()
            if event == sg.WIN_CLOSED:
                rodando = False
            elif isinstance(event, str):
                event_values = event.split('-')
                tipo_evento = event_values[0]
                if len(event_values) > 1:
                    codigo_produto = event_values[1]

                if tipo_evento == 'edit':
                    # Inicia a edição de um produto.
                    self.__apresentacao.window.close()
                    self.__apresentacao.tela_edicao(codigo_produto)

                elif tipo_evento == 'remove':
                    # Remove um produto do estoque.
                    self.remove_produto(codigo_produto)
                    self.__apresentacao.tela_produtos()

                elif tipo_evento == 'save':
                    # Salva os novos valores de um produto.
                    self.atualiza_produto(
                        codigo=codigo_produto,
                        nome=values['nome'],
                        valor=float(values['valor']),
                        quantidade=int(values['quantidade']))
                    self.__apresentacao.window.close()
                    self.__apresentacao.tela_produtos()

                elif tipo_evento == 'cancel':
                    # Cancela a ação que estava sendo feita.
                    self.__apresentacao.window.close()
                    self.__apresentacao.tela_produtos()

                elif tipo_evento == 'add':
                    # Inicia a adição de um produto.
                    self.__apresentacao.window.close()
                    self.__apresentacao.tela_adicionar()

                elif tipo_evento == 'create':
                    # Cria um novo produto.
                    self.cria_produto(
                        codigo=values['codigo'],
                        nome=values['nome'],
                        valor=float(values['valor']),
                        quantidade=int(values['quantidade']),
                    )
                    self.__apresentacao.window.close()
                    self.__apresentacao.tela_produtos()

        self.__apresentacao.window.close()
