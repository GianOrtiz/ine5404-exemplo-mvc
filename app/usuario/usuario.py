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
        self.__senha = senha

    @property
    def nome(self) -> str:
        return self.__nome

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