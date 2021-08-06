from typing import List

from app.usuario.usuario import Usuario

class Controlador:

    def __init__(self):
        self.__usuarios: List[Usuario] = Usuario.obtem_usuarios()
        # Se os usuários estiverem vazio, cria o usuário padrão
        if len(self.__usuarios) == 0:
            self.__usuarios.append(Usuario.cria_usuario('default', 'default'))
    
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
        usuario = Usuario.cria_usuario(nome, senha)
        self.__usuarios.append(usuario)
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
        for usuario in self.__usuarios:
            if usuario.nome == nome:
                return usuario
        return None        
    
    def remove_usuario(self, nome: str):
        """Remove um usuário

        Parameters
        ----------
        nome : str
            Nome do usuário para remover
        """
        for usuario in self.__usuarios:
            if usuario.nome == nome:
                usuario.remove_usuario()
                self.__usuarios.remove(usuario)
                return

    def atualiza_usuario(self, nome: str, senha: str):
        """Atualiza as informações de um usuário
        
        Parameters
        ----------
        nome : str
            Nome do usuário para selecionar
        senha : str
            Nova senha do usuário
        """
        for usuario in self.__usuarios:
            if usuario.nome == nome:
                usuario.senha = senha
                usuario.atualiza_usuario()
