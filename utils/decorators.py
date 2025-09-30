from .variables import *

def controle_recursivo(fn: Callable) -> Callable:
    """
    Implementa comportamento de chamadas recursivas para controle da entrada do usuário.
    Quebra a execução do programa se o número máximo prédefinido (5) for atingido.
    :param fn: Função aprimorada.
    :return: Callable.
    """
    def envolucro(rotulo: str = '\n=>', chamadas: int = 5, *args, **kwargs):
        entrada = fn(input(rotulo), *args, **kwargs)
        if entrada is None:
            if chamadas > 0:
                return  envolucro(rotulo, chamadas - 1, *args, **kwargs)
            else:
                raise RuntimeError(msg_de_erro.format(fn.__name__, 'Limite de chamadas recursivas atingido.'))
        return entrada
    return envolucro