import pickle

from typing import List, Dict, TypeVar
from abc import ABC, abstractmethod

T = TypeVar('T')

class DAO(ABC):
    """Classe de acesso aos dados, contem apenas implementação"""

    def __init__(self, datasource: str):
        """Iniciliza o DAO

        Parameters
        ----------
        datasource : str
            O datasource para utilizar, um arquivo, por exemplo
        """

        if not isinstance(datasource, str):
            raise ValueError('datasource deve ser do tipo str')
        self.__datasource = datasource
        self.__cache: Dict[str, T] = {}

        try:
            self.__load()
        except:
            self.__dump()
    
    def __dump(self):
        """Salva o cache no datasource"""
        f = open(self.__datasource, 'wb')
        pickle.dump(self.__cache, f)
        f.close()

    def __load(self):
        """Carrega os dados do arquivo datasource"""
        f = open(self.__datasource, 'rb')
        self.__cache = pickle.load(f)
        f.close()

    @abstractmethod
    def add(self, key: str, obj: T):
        """Adiciona novo objeto no datasource
        
        Parameters
        ----------
        key : str
            A chave única do objeto
        obj : T
            O objeto para salvar no datasource
        """
        self.__cache[key] = obj
        self.__dump()

    @abstractmethod
    def get(self, key: str) -> T:
        """Obtem um objeto pela sua chave

        Parameters
        ----------
        key : str
            A chave única do objeto

        Returns
        -------
        T
            O objeto obtido pela chave
        """
        return self.__cache[key]

    @abstractmethod
    def remove(self, key: str):
        """Remove um objeto pela sua chave

        Parameters
        ----------
        key : str
            A chave única do objeto
        """
        try:
            self.__cache.remove(key)
            self.__dump
        except:
            pass

    @abstractmethod
    def get_all(self) -> List[T]:
        """Obtem a lista de todos os objetos

        Parameters
        ----------
        dict
            Todos os objetos salvos
        """
        return self.__cache.values()
