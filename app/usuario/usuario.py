from app.modelo import Modelo
from app.usuario.repositorio import RepositorioUsuario

class Usuario(Modelo):

    # Repositório estático da classe.
    __repositorio: RepositorioUsuario = RepositorioUsuario.getInstance()

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
        self.__senha = senha

    @property
    def identificador(self) -> str:
        return self.__nome

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
        return self.__senha == senha

    def to_json(self):
        json = {
            'nome': self.__nome,
            'senha': self.__senha,
        }
        return json

    @staticmethod
    def from_json(json: dict):
        return Usuario(
            json['nome'],
            json['senha'],
        )

    @staticmethod
    def cria_usuario(nome: str, senha: str):
        """Cria um novo usuário

        Parameters
        ----------
        nome : str
            Nome do usuário
        senha : str
            Senha do usuário

        Returns
        -------
        Usuario
            O novo usuário criado        
        """
        usuario = Usuario(nome, senha)
        Usuario.__repositorio.cria(usuario)
        return usuario

    @staticmethod
    def obtem_usuarios():
        """Obtem todos os usuarios

        Returns
        -------
        list
            Lista de todos os usuários
        """
        return Usuario.__repositorio.obtem(Usuario)

    def remove_usuario(self):
        """Remove este usuário"""
        Usuario.__repositorio.remove(self, Usuario)
    
    def atualiza_usuario(self):
        """Atualiza as informações deste usuário"""
        Usuario.__repositorio.atualiza(self)


