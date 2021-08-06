from typing import List

from app.produto.produto import Produto

class Controlador:

    def __init__(self):
        self.__produtos: List[Produto] = Produto.obtem_produtos()
        
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
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        produto = Produto.cria_produto(codigo, nome, valor, quantidade)
        self.__produtos.append(produto)
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
        for produto in self.__produtos:
            if produto.codigo == codigo:
                return produto
        return None
    
    def remove_produto(self, codigo: str):
        """Remove um produto

        Parameters
        ----------
        codigo : str
            Código do produto
        """
        for produto in self.__produtos:
            if produto.codigo == codigo:
                produto.remove_produto()
                self.__produtos.remove(produto)
                return

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
        for produto in self.__produtos:
            if produto.codigo == codigo:
                if nome is not None:
                    produto.nome = nome
                if valor is not None:
                    produto.valor = valor
                if quantidade is not None:
                    produto.quantidade = quantidade
                produto.atualiza_produto()
