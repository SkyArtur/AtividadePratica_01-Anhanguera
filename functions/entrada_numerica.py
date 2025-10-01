from .decorators import *

@controle_recursivo
def entrada_numerica(_rotulo: str, _decimal: bool = False, maxx: int = None, *args, **kwargs):
    try:
        num: float = float(_rotulo)
        if maxx and num > maxx:
            raise Exception(msg_de_alerta.format(entrada_numerica.__name__, f'O valor digitado é maior que {maxx}!'))
    except (ValueError, Exception) as error:
        if isinstance(error, ValueError):
            print(msg_de_alerta.format(entrada_numerica.__name__, 'Insira apenas valores numéricos.'))
        else:
            print(error)
    else:
        return num if _decimal else int(num)