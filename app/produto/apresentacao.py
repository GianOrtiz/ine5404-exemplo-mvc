from app.produto.controlador import Controlador
from app.util import le_float, le_string, le_int, nao_eh_vazio

class ApresentacaoProduto:

    OPCOES = {
        '0': 'Sair',
        '1': 'Consultar produto por código',
        '2': 'Criar um novo produto',
        '3': 'Remove unidades de produto',
        '4': 'Adicionar unidades de produto',
    }

    def __init__(self):
        self.__controlador = Controlador()

    def opcoes(self):
        while True:
            print('Escolha uma das opções:\n')
            for key, item in ApresentacaoProduto.OPCOES.items():
                print('{0} - {1}'.format(key, item))    

            opcao = input()
            if opcao in ['0', '1', '2', '3', '4']:
                if opcao == '0':
                    break
                elif opcao == '1':
                    codigo = le_string('Código do produto: ', nao_eh_vazio)
                    produto = self.__controlador.obtem_produto(codigo)
                    if produto is None:
                        print('Produto não encontrado!')
                    print('Produto encontrado.')
                    print(produto)
                elif opcao == '2':
                    codigo = le_string('Código do produto: ', nao_eh_vazio)
                    nome = le_string('Nome do produto: ', nao_eh_vazio)
                    valor = le_float('Valor do produto: ')
                    quantidade = le_int('Quantidade inicial do produto: ')
                    produto = self.__controlador.cria_produto(codigo, nome, valor, quantidade)
                    print(produto)
                elif opcao == '3':
                    codigo = le_string('Código do produto: ', nao_eh_vazio)
                    produto = self.__controlador.obtem_produto(codigo)
                    if produto is None:
                        print('Produto não encontrado!')
                    else:
                        unidades = le_int('Unidades para remover: ')
                        nova_quantidade = produto.quantidade - unidades
                        if nova_quantidade < 0:
                            nova_quantidade = 0
                        self.__controlador.atualiza_produto(codigo, quantidade=nova_quantidade)
                elif opcao == '4':
                    codigo = le_string('Código do produto: ', nao_eh_vazio)
                    produto = self.__controlador.obtem_produto(codigo)
                    if produto is None:
                        print('Produto não encontrado!')
                    else:
                        unidades = le_int('Unidades para adicionar: ')
                        nova_quantidade = produto.quantidade + unidades
                        self.__controlador.atualiza_produto(codigo, quantidade=nova_quantidade)
            else:
                print('Opção não identificada, tente de novo.\n\n')
