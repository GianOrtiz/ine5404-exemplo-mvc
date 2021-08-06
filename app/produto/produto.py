from app.produto.repositorio import RepositorioProduto
from app.modelo import Modelo

class Produto(Modelo):

    # Referência estática do repositório.
    __repositorio: RepositorioProduto = RepositorioProduto()

    def __init__(self, nome: str, codigo: str, valor: float, quantidade: int):
        """
        Parameters
        ----------
        nome : str
            Nome do produto
        codigo : str
            Código único do produto para facilitar acesso
        valor : float
            Valor unitário do produto
        quantidade : int
            Quantidades existentes do produto
        """

        if not isinstance(nome, str):
            raise ValueError('nome deve ser do tipo str')

        if not isinstance(codigo, str):
            raise ValueError('codigo deve ser do tipo str')
    
        if not isinstance(valor, float):
            raise ValueError('valor deve ser do tipo float')

        if not isinstance(quantidade, int):
            raise ValueError('quantidade deve ser do tipo int')

        self.__nome = nome
        self.__codigo = codigo
        self.__valor = valor
        self.__quantidade = quantidade

    @property
    def identificador(self) -> str:
        return self.__codigo

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, nome: str) -> str:
        if not isinstance(nome, str):
            raise ValueError('nome deve ser do tipo str')
        self.__nome = nome

    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @property
    def valor(self) -> float:
        return self.__valor
    
    @valor.setter
    def valor(self, valor: float):
        if not isinstance(valor, float):
            raise ValueError('valor deve ser do tipo float')
        self.__valor = valor
    
    @property
    def quantidade(self) -> int:
        return self.__quantidade
    
    @quantidade.setter
    def quantidade(self, quantidade: int):
        if not isinstance(quantidade, int):
            raise ValueError('quantidade deve ser do tipo int')
        self.__quantidade = quantidade

    def to_json(self):
        json = {
            'codigo': self.__codigo,
            'nome': self.__nome,
            'valor': self.__valor,
            'quantidade': self.__quantidade,
        }
        return json

    @staticmethod
    def from_json(json: dict):
        return Produto(
            codigo=json['codigo'],
            nome=json['nome'],
            valor=float(json['valor']),
            quantidade=int(json['quantidade']),
        )

    
    @staticmethod
    def cria_produto(codigo: str, nome: str, valor: float, quantidade: int):
        """Cria um novo produto

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
            O novo produto criado        
        """
        produto = Produto(codigo=codigo, nome=nome, valor=valor, quantidade=quantidade)
        Produto.__repositorio.cria(produto)
        return produto

    @staticmethod
    def obtem_produtos():
        """Obtem todos os produtos

        Returns
        -------
        list
            Lista de todos os produtos
        """
        return Produto.__repositorio.obtem(Produto)

    def remove_produto(self):
        """Remove este produto"""
        Produto.__repositorio.remove(self, Produto)
    
    def atualiza_produto(self):
        """Atualiza as informações deste produto"""
        Produto.__repositorio.atualiza(self)

    def __str__(self):
        return '{0} - {1} | R$ {2} | Quantidade: {3}'.format(
            self.__codigo, self.__nome, self.__valor, self.__quantidade)
    
    def __repr__(self):
        return self.__str__()
