from typing import List

from app.produto.produto import Produto

class Estoque:

    def __init__(self):
        self.__produtos: List[Produto] = []

    @property
    def produtos(self) -> List[Produto]:
        return self.__produtos

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
        for produto in self.produtos:
            if produto.codigo == codigo:
                return
        self.__produtos.append(Produto(nome, codigo, valor, quantidade))

    def retira_unidade_produto(self, codigo: str, unidades: int):
        """Retira unidades de um produto

        Parameters
        ----------
        codigo : str
            Código identificador do produto
        unidades : int
            Unidades a retirar do produto
        """
        for produto in self.__produtos:
            if produto.codigo == codigo:
                if produto.quantidade - unidades >= 0:
                    produto.quantidade -= unidades
                else:
                    produto.quantidade = 0
                break

    def adiciona_unidade_produto(self, codigo: str, unidades: int):
        """Adiciona unidades de um produto

        Parameters
        ----------
        codigo : str
            Código identificador do produto
        unidades : int
            Unidades a adicionar do produto
        """
        for produto in self.__produtos:
            if produto.codigo == codigo:
                produto.quantidade += unidades
                break
    
    def remove_produto(self, codigo: str):
        """Remove um produto do estoque
        
        Parameters
        ----------
        codigo : str
            Código do produto
        """
        for produto in self.__produtos:
            if produto.codigo == codigo:
                self.__produtos.remove(produto)
                break
