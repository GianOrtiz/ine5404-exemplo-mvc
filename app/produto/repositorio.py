from app.repositorio.repositorio_arquivo import RepositorioArquivo
REPOSITORIO_USUARIO_PRODUTO = 'produtos.json'

class RepositorioProduto(RepositorioArquivo):

    # Modelo de Singleton.
    __instance = None

    @staticmethod 
    def getInstance():
      if RepositorioProduto.__instance == None:
         RepositorioProduto()
      return RepositorioProduto.__instance

    def __init__(self):
        if RepositorioProduto.__instance != None:
            raise Exception('Esta classe é um Singleton!')
        else:
            super().__init__(REPOSITORIO_USUARIO_PRODUTO)
            RepositorioProduto.__instance = self



