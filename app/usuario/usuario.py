from hashlib import blake2b

import os

HASH_KEY = os.environ['HASH_KEY']

class Usuario:

    def __init__(self, nome: str, senha: str):
        """
        Parameters
        ----------
        nome : str
            Nome único do usuário.
        senha : str
            Senha do usuário.
        """

        if not isinstance(nome, str):
            raise ValueError('nome deve ser do tipo str')

        if not isinstance(senha, str):
            raise ValueError('senha deve ser do tipo str')

        self.__nome = nome
        self.__senha = blake2b(
            bytes(senha, 'utf-8'), key=bytes(HASH_KEY, 'utf-8')).hexdigest()

    @property
    def nome(self) -> str:
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise ValueError('nome deve ser do tipo str')
        self.__nome = nome
    
    @property
    def senha(self) -> str:
        return self.__senha

    @senha.setter
    def senha(self, senha: str):
        if not isinstance(senha, str):
            raise ValueError('senha deve ser do tipo str')
        self.__senha = senha

    def compara_senha(self, senha: str) -> bool:
        """Compara a senha dada com a senha do usuário.

        Parameters
        ----------
        senha : str
            Senha para comparar com a senha do usuário
        
        Returns
        -------
        bool
            Retorna True se senhas são iguais ou False caso contrário
        """
        return self.__senha == blake2b(
            bytes(senha, 'utf-8'), key=bytes(HASH_KEY, 'utf-8')).hexdigest()

    def __str__(self) -> str:
        return 'Usuário - {0}'.format(self.__nome)

    def __repr__(self) -> str:
        return self.__str__()
