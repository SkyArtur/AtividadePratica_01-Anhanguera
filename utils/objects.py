from .functions import *


class Aluno:
    def __init__(self, *args, **kwargs):
        self.matricula: str = kwargs.get('matricula')
        self.nome: str = kwargs.get('nome')
        self.notas: list[int] = kwargs.get('notas') if kwargs.get('notas') else [0]

    @property
    def media_final(self):
        return sum(self.notas) / len(self.notas)

    @property
    def situacao(self):
        return "Aprovado" if self.media_final > 7 else "Reprovado"


class BancoDeDados:
    def __init__(self, pre_dados: list[Aluno] = None):
        self.__dados = [] if not pre_dados else pre_dados

    def __incrementa_matricula(self):
        nova_matricula = int(self.__dados[-1].matricula) if len(self.__dados) > 0 else 0
        nova_matricula = nova_matricula + 1
        return f'{nova_matricula:0>9}'

    def visualizar_alunos(self):
        for aluno in self.__dados:
            print(
                dados_alunos_texto.format(
                    aluno.nome,
                    aluno.matricula,
                    aluno.notas,
                    aluno.media_final,
                    aluno.situacao
                )
            )
        input('Digite algo para continuar...')

    def adicionar_aluno(self):
        print(f'Adicionando aluno...')
        control = True
        while control:
            aluno = Aluno()
            aluno.matricula = self.__incrementa_matricula()
            aluno.nome = input('Digite o nome do aluno: ')
            aluno.notas = [int(entrada_numerica(f'Digite a nota {n} do aluno: ', maxx=10)) for n in range(4)]
            self.__dados.append(aluno)
            control = menu_numerico(menu_adicionar_aluno, [0, 1])

    @property
    def dados(self) -> list[Aluno]:
        return self.__dados

