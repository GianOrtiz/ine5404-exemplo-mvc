from abc import ABC, abstractmethod
from typing import List

from app.modelo import Modelo


class Repositorio(ABC):

    @abstractmethod
    def cria(self, objeto: Modelo):
        """Cria um novo objeto no repositório

        Parameters
        ----------
        objeto : Modelo
            O objeto a ser criado
        """
        pass

    @abstractmethod
    def obtem(self, to: Modelo) -> List[Modelo]:
        """Obtem todos os objetos do repositório
        
        Parameters
        ----------
        to : Modelo
            Modelo que será transformado o JSON

        Returns
        -------
        list
            Lista de todos os objetos
        """
        pass

    @abstractmethod
    def remove(self, identificador: str): 
        """Remove um objeto do repositório pelo identificador

        Parameters
        ----------
        identificador : str
            Identificador único do objeto
        """
        pass

    @abstractmethod
    def atualiza(self, objeto: Modelo):
        """Atualiza o valor de um objeto do repositório

        Parameters
        ----------
        objeto : Modelo
            O objeto para atualizar
        """
        pass

    @abstractmethod
    def obtem_um(self, identificador: str, to: Modelo) -> Modelo:
        """Obtem apenas um objeto pelo identificador

        Parameters
        ----------
        identificador : str
            Identificador único do objeto
        to : Modelo
            Modelo que será transformado o JSON

        Returns
        -------
        Modelo
            O objeto encontrado
        """
        pass
