from typing import Callable

nao_eh_vazio = lambda x: len(x) > 0

def le_string(descricao: str, validacao: Callable[[str], bool]) -> str:
    """Le uma string por input validando a entrada

    Parameters
    ----------
    descricao : str
        Descrição do valor que será recebido
    validacao : (valor: str) -> bool
        Função de validação do valor recebido
    
    Returns
    -------
    str
        Retorna a string se ela passar pela validação
    """
    while True:
        valor = input(descricao)
        if validacao(valor):
            return valor
        else:
            print('Input recebido não é válido, tente novamente!')

def le_float(descricao: str) -> float:
    """Le um float pela linha de comando
    
    Parameters
    ----------
    descricao : str
        Descrição do valor que será recebido

    Returns
    -------
    float
        O valor do float lido
    """
    while True:
        valor = input(descricao)
        try:
            valor = float(valor)
            return valor
        except:
            print('Valor deve ser do tipo float')

def le_int(descricao: str) -> int:
    """Le um int pela linha de comando
    
    Parameters
    ----------
    descricao : str
        Descrição do valor que será recebido

    Returns
    -------
    int
        O valor do int lido
    """
    while True:
        valor = input(descricao)
        try:
            valor = int(valor)
            return valor
        except:
            print('Valor deve ser do tipo int')
