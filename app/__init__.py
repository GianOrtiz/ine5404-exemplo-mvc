from app.sistema.sistema import Sistema

def main():
    sistema = Sistema()

    opcoes = ['1', '2', '3', '4', '5']
    switcher = {
        opcoes[0]: sistema.consulta_produto,
        opcoes[1]: sistema.cria_produto,
        opcoes[2]: sistema.remove_unidade_produto,
        opcoes[3]: sistema.adiciona_unidade_produto,
        opcoes[4]: sistema.cria_usuario,
    }

    print('Sistema de Estoque')
    print('------------------\n')
    while True:
        if sistema.autenticado:
            resposta = input(
                '''
                Escolha uma das opções:

                0 - Sair
                1 - Consultar produto por código
                2 - Criar um novo produto
                3 - Remove unidades de produto
                4 - Adicionar unidades de produto
                5 - Criar um novo usuário
                '''
            )
            if resposta == '0':
                break
            elif resposta in opcoes:
                # Chama a função correspondente a resposta dada.
                switcher[resposta]()
            else:
                print('Opção escolhida não existente, tente novamente!') 
        else:
            # Autentica um usuário caso ele não esteja autenticado.
            resposta = input('Você não está autenticado, deseja autenticar?[sim|nao]:\n')
            if resposta == 'sim':
                sistema.login_usuario()
            else:
                break 
