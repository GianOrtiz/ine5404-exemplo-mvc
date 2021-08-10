import json

from typing import List
from app.dao import DAO
from app.produto.produto import Produto

REPOSITORIO_PRODUTOS_ARQUIVO = 'produtos.pkl'

class DAOProduto(DAO):

    def __init__(self):
        super().__init__(REPOSITORIO_PRODUTOS_ARQUIVO)

    def add(self, codigo: str, produto: Produto):
        """Adiciona novo produto no datasource
        
        Parameters
        ----------
        codigo : str
            O código único do produto
        produto : Produto
            O produto a adicionar no datasource
        """
        super().add(codigo, produto)

    def get(self, codigo: str) -> Produto:
        """Obtem um produto pelo seu código

        Parameters
        ----------
        codigo : str
            O código único do produto

        Returns
        -------
        Produto
            O produto encontrado
        """
        return super().get(codigo)

    def remove(self, codigo: str):
        """Remove um produto pelo seu código

        Parameters
        ----------
        codigo : str
            O código único do produto
        """
        super().remove(codigo)

    def get_all(self) -> List[Produto]:
        """Obtem a lista de todos os produtos

        Parameters
        ----------
        list
            A lista de todos os produtos
        """
        return super().get_all()
