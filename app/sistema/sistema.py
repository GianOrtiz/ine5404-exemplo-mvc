from typing import List, Callable

from app.usuario.usuario import Usuario
from app.estoque.estoque import Estoque
from app.util import nao_eh_vazio

class Sistema:
    
    def __init__(self):
        self.__estoque = Estoque()
        self.__usuarios: List[Usuario] = [
            Usuario('default', 'default'),
        ]
        self.__autenticado = False

    @property
    def autenticado(self) -> bool:
        return self.__autenticado

    def login_usuario(self):
        """Realiza o login de um usuário"""
        nome = self.__le_string('Nome do usuário:\n', nao_eh_vazio)
        senha = self.__le_string('Senha do usuário:\n', nao_eh_vazio)
        for usuario in self.__usuarios:
            if usuario.nome == nome:
                if usuario.compara_senha(senha):
                    self.__autenticado = True
                    return
        print('Nome ou senha incorretos!\n')
                    
    def consulta_produto(self):
        """Consulta um produto se houver no estoque"""
        codigo = self.__le_string('Código do produto:\n', nao_eh_vazio)
        for produto in self.__estoque.produtos:
            if produto.codigo == codigo:
                print('Produto encontrado:\n')
                print(produto)
                return
        print('Produto não encontrado!\n')

    def cria_produto(self):
        """Cria um novo produto"""
        codigo_produto = self.__le_string('Código do produto:\n', nao_eh_vazio)

        def codigo_existente(codigo: str) -> bool:
            for produto in self.__estoque.produtos:
                if produto.codigo == codigo:
                    return True
            return False

        while codigo_existente(codigo_produto):
            codigo_produto = self.__le_string('Código já utilizado, tente outro:\n', nao_eh_vazio)
        
        nome_produto = self.__le_string('Nome do produto:\n', nao_eh_vazio)
        valor_produto = self.__le_float('Valor do produto:\n')
        quantidade_produto = self.__le_int('Quantidade inicial do produto:\n')
        self.__estoque.adiciona_produto(
            nome_produto, codigo_produto, valor_produto, quantidade_produto)

    def remove_unidade_produto(self):
        """Remove unidades de um produto"""
        codigo_produto = self.__le_string('Código do produto:\n', nao_eh_vazio)
        unidades = self.__le_int('Unidades para retirar:\n')
        self.__estoque.retira_unidade_produto(codigo_produto, unidades)

    def adiciona_unidade_produto(self):
        """Adiciona unidades de um produto"""
        codigo_produto = self.__le_string('Código do produto:\n', nao_eh_vazio)
        unidades = self.__le_int('Unidades para adicionar:\n')
        self.__estoque.adiciona_unidade_produto(codigo_produto, unidades)

    def remove_produto(self):
        """Remove um produto pelo seu código"""
        codigo_produto = self.__le_string('Código do produto:\n', nao_eh_vazio)
        self.__estoque.remove_produto(codigo_produto)

    def cria_usuario(self):
        """Cria um novo usuário"""
        def usuario_existe(nome: str) -> bool:
            for usuario in self.__usuarios:
                if usuario.nome == nome:
                    return True
            return False

        nome = self.__le_string('Nome do usuário:\n', nao_eh_vazio)
        while usuario_existe(nome):
            nome = self.__le_string('Usuário já existe, tente outro nome:\n', nao_eh_vazio)

        senha = self.__le_string('Senha do usuário:\n', nao_eh_vazio)
        self.__usuarios.append(Usuario(nome, senha))

    def __le_string(self, descricao: str, validacao: Callable[[str], bool]) -> str:
        """Le uma string por input validando a entrada

        Parameters
        ----------
        descricao : str
            Descrição do valor que será recebido
        validacao : (valor: str) -> bool
            Função de validação do valor recebido
        
        Returns
        -------
        str
            Retorna a string se ela passar pela validação
        """
        while True:
            valor = input(descricao)
            if validacao(valor):
                return valor
            else:
                print('Input recebido não é válido, tente novamente!')

    def __le_float(self, descricao: str) -> float:
        """Le um float pela linha de comando
        
        Parameters
        ----------
        descricao : str
            Descrição do valor que será recebido

        Returns
        -------
        float
            O valor do float lido
        """
        while True:
            valor = input(descricao)
            try:
                valor = float(valor)
                return valor
            except:
                print('Valor deve ser do tipo float')

    def __le_int(self, descricao: str) -> int:
        """Le um int pela linha de comando
        
        Parameters
        ----------
        descricao : str
            Descrição do valor que será recebido

        Returns
        -------
        int
            O valor do int lido
        """
        while True:
            valor = input(descricao)
            try:
                valor = int(valor)
                return valor
            except:
                print('Valor deve ser do tipo int')

