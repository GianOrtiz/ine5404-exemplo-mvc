from app.repositorio.repositorio_arquivo import RepositorioArquivo

REPOSITORIO_USUARIO_ARQUIVO = 'usuarios.json'

class RepositorioUsuario(RepositorioArquivo):

    # Modelo de Singleton.
    __instance = None

    @staticmethod 
    def getInstance():
      if RepositorioUsuario.__instance == None:
         RepositorioUsuario()
      return RepositorioUsuario.__instance

    def __init__(self):
        if RepositorioUsuario.__instance != None:
            raise Exception('Esta classe é um Singleton!')
        else:
            super().__init__(REPOSITORIO_USUARIO_ARQUIVO)
            RepositorioUsuario.__instance = self



