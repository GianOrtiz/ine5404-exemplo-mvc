import json

from typing import List
from app.dao import DAO
from app.usuario.usuario import Usuario

REPOSITORIO_USUARIOS_ARQUIVO = 'usuarios.pkl'

class DAOUsuario(DAO):

    def __init__(self):
        super().__init__(REPOSITORIO_USUARIOS_ARQUIVO)

    def add(self, nome: str, usuario: Usuario):
        """Adiciona novo usuário no datasource
        
        Parameters
        ----------
        nome : str
            O nome do usuário
        usuario : Usuario
            O usuário a adicionar no datasource
        """
        super().add(nome, usuario)

    def get(self, nome: str) -> Usuario:
        """Obtem um usuário pelo seu nome

        Parameters
        ----------
        nome : str
            O nome do usuário

        Returns
        -------
        Usuario
            O usuário encontrado
        """
        return super().get(nome)

    def remove(self, nome: str):
        """Remove um usuário pelo seu nome

        Parameters
        ----------
        nome : str
            O nome do usuário
        """
        super().remove(nome)

    def get_all(self) -> List[Usuario]:
        """Obtem a lista de todos os usuários

        Parameters
        ----------
        list
            A lista de todos os usuários
        """
        return super().get_all()