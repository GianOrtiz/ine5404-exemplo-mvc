from typing import TypeVar
from abc import ABC, abstractmethod, abstractproperty

T = TypeVar('T')

class Modelo(ABC):

    @abstractproperty
    def identificador(self) -> str:
        pass

    @abstractmethod
    def to_json(self) -> dict[str, T]:
        """Converte o objeto modelo em JSON

        Returns
        -------
        dict[str, T]
            O objeto convertido em JSON
        """
        pass
    
    @staticmethod
    def from_json(json: dict[str, T]) -> object:
        """Converte o JSON em objeto.

        Parameters
        ----------
        json : dict[str, T]
            O JSON para converter em objeto

        Returns
        -------
        object
            O objeto convertido
        """
        pass
