from .entrada_numerica import *


def menu_numerico(rotulo: str, opcoes: list[int], fn_clear: Callable = None, *args, **kwargs):
    msg = f'Opção invalida! Apenas números entre {min(opcoes)} e {max(opcoes)}.'
    while True:
        opcao = entrada_numerica(rotulo)
        if opcao in opcoes:
            return opcao
        else:
            fn_clear()
            print(msg_de_alerta.format(menu_numerico.__name__, msg))
