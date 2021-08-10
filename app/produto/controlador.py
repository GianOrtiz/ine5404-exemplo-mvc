from typing import List

from app.produto.produto import Produto
from app.produto.dao import DAOProduto

class Controlador:

    def __init__(self):
        self.__dao = DAOProduto()
        
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
        produto = Produto(codigo, nome, valor, quantidade)
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
