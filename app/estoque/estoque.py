from typing import List

from app.produto.produto import Produto
from app.produto.dao import DAOProduto

class Estoque:

    def __init__(self):
        self.__produto_dao = DAOProduto()

    @property
    def produtos(self) -> List[Produto]:
        return self.__produto_dao.get_all()

    def adiciona_produto(self, nome: str, codigo: str, valor: float, quantidade: int):
        """Adiciona um produto ao estoque

        Parameters
        ----------
        nome : str
            Nome do produto a adicionar
        codigo : str
            Codigo único do produto. Se o código já existir, não adiciona
        valor : float
            Valor unitário do produto
        quantidade : int
            Quantidade inicial do produto
        """
        try:
            self.__produto_dao.get(codigo)
        except:
            self.__produto_dao.add(codigo, Produto(nome, codigo, valor, quantidade))

    def retira_unidade_produto(self, codigo: str, unidades: int):
        """Retira unidades de um produto

        Parameters
        ----------
        codigo : str
            Código identificador do produto
        unidades : int
            Unidades a retirar do produto
        """
        try:
            produto = self.__produto_dao.get(codigo)
        except:
            print('Produto não encontrado!')

        if produto is not None:
            if produto.quantidade - unidades >= 0:
                produto.quantidade -= unidades
            else:
                produto.quantidade = 0
            self.__produto_dao.remove(codigo)
            self.__produto_dao.add(codigo, produto)

    def adiciona_unidade_produto(self, codigo: str, unidades: int):
        """Adiciona unidades de um produto

        Parameters
        ----------
        codigo : str
            Código identificador do produto
        unidades : int
            Unidades a adicionar do produto
        """
        try:
            produto = self.__produto_dao.get(codigo)
        except:
            print('Produto não encontrado!')
        
        if produto is not None:
            produto.quantidade += unidades
            self.__produto_dao.remove(codigo)
            self.__produto_dao.add(codigo, produto)

    def remove_produto(self, codigo: str):
        """Remove um produto do estoque
        
        Parameters
        ----------
        codigo : str
            Código do produto
        """
        self.__produto_dao.remove(codigo)
