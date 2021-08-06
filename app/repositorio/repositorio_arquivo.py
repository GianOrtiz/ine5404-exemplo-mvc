import json

from os.path import exists
from typing import List

from app.modelo import Modelo
from app.repositorio.repositorio import Repositorio

class RepositorioArquivo(Repositorio):

    def __init__(self, nome_arquivo: str):
        """
        Parameters
        ----------
        nome_arquivo : str
            Nome do arquivo para ser utilizado como armazenamento
        """
        super().__init__()
        
        if not isinstance(nome_arquivo, str):
            raise ValueError('nome_arquivo deve ser do tipo str')
        self.__nome_arquivo = nome_arquivo

        if not exists(self.__nome_arquivo):
            # Cria arquivo se não existir.
            f = open(self.__nome_arquivo, 'w')
            f.write('[]')
            f.close() 
    
    @property
    def nome_arquivo(self) -> str:
        return self.__nome_arquivo

    def cria(self, objeto: Modelo):
        """Cria um novo objeto no repositório

        Parameters
        ----------
        objeto : Modelo
            O objeto a ser criado
        """
        objetos = self.obtem(objeto)
        objetos.append(objeto)
        f = open(self.__nome_arquivo, 'w')
        dicts = []
        for o in objetos:
            dicts.append(o.to_json())
        json.dump(dicts, f)

    def obtem(self, to: Modelo) -> List[Modelo]:
        """Obtem todos os objetos do repositório
        
        Returns
        -------
        list
            Lista de todos os objetos
        to : Modelo
            Modelo em que será transformado o JSON
        """
        f = open(self.__nome_arquivo, 'r')
        objetos = json.load(f)
        modelos: List[Modelo] = []
        for o in objetos:
            modelos.append(to.from_json(o))
        return modelos
        
    def remove(self, identificador: str, to: Modelo): 
        """Remove um objeto do repositório pelo identificador

        Parameters
        ----------
        identificador : str
            Identificador único do objeto
        to : Modelo
            Modelo em que será transformado o JSON
        """
        objetos = self.obtem(to)
        for o in objetos:
            if o.identificador == identificador:
                objetos.remove(o)
                break
        
        f = open(self.__nome_arquivo, 'w')
        dicts = []
        for o in objetos:
            dicts.append(o.to_json())
        json.dump(dicts, f)
            

    def atualiza(self, objeto: Modelo):
        """Atualiza o valor de um objeto do repositório

        Parameters
        ----------
        objeto : Modelo
            O objeto para atualizar
        """
        self.remove(objeto.identificador, objeto)
        self.cria(objeto)

    def obtem_um(self, identificador: str, to: Modelo) -> Modelo:
        """Obtem apenas um objeto pelo identificador

        Parameters
        ----------
        identificador : str
            Identificador único do objeto
        to : Modelo
            Modelo em que será transformado o JSON
        """
        objetos = self.obtem(to)
        for o in objetos:
            if o.identificador == identificador:
                return o
        return None
