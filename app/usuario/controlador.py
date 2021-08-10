from typing import List

from app.usuario.usuario import Usuario
from app.usuario.dao import DAOUsuario

class Controlador:

    def __init__(self):
        self.__dao = DAOUsuario()

        # Se os usuários estiverem vazio, cria o usuário padrão
        usuarios = self.__dao.get_all()
        if len(usuarios) == 0:
            self.__dao.add('default', Usuario('default', 'default'))
    
    def cria_usuario(self, nome: str, senha: str) -> Usuario:
        """Cria um novo usuário no sistema

        Parameters
        ----------
        nome : str
            Nome do usuário
        senha : str
            Senha do usuário
        
        Returns
        -------
        Usuario
            Usuário criado
        """
        usuario = Usuario(nome, senha)
        self.__dao.add(nome, usuario)
        return usuario
        
    def obtem_usuario(self, nome: str) -> Usuario:
        """Retorna os usuários

        Parameters
        ----------
        nome : str
            Nome do usuário para retornar

        Returns
        -------
        Usuario
            O usuário selecionado
        """
        return self.__dao.get(nome)

    def remove_usuario(self, nome: str):
        """Remove um usuário

        Parameters
        ----------
        nome : str
            Nome do usuário para remover
        """
        self.__dao.remove(nome)

    def atualiza_usuario(self, nome: str, senha: str):
        """Atualiza as informações de um usuário
        
        Parameters
        ----------
        nome : str
            Nome do usuário para selecionar
        senha : str
            Nova senha do usuário
        """
        usuario = self.__dao.get(nome)
        if usuario is not None:
            self.__dao.remove(nome)
            usuario.senha = senha
            self.__dao.add(nome, usuario)
