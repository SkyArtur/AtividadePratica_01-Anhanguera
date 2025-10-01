import os
from functions import *
from utils import *
from .aluno import Aluno



class Aplicacao:

    def __init__(self, pre_dados: list[Aluno] = None):
        self.__dados = [] if not pre_dados else pre_dados
        self.__aluno = None

    @property
    def dados(self) -> list[Aluno]:
        return self.__dados

    @staticmethod
    def limpar_display():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __incrementa_matricula(self):
        nova_matricula = int(self.__dados[-1].matricula) if len(self.__dados) > 0 else 0
        nova_matricula = nova_matricula + 1
        return f'{nova_matricula:0>9}'

    def limpar_ciclo_de_execucao(self):
        self.__aluno = None

    def __exibir_aluno(self):
        print(
            dados_alunos_texto.format(
                self.__aluno.nome,
                self.__aluno.matricula,
                self.__aluno.notas,
                self.__aluno.media_final,
                self.__aluno.situacao
            )
        )

    def visualizar_alunos(self):
        self.limpar_display()
        print('Alunos Cadastrados...')
        for aluno in self.__dados:
            self.__aluno = aluno
            self.__exibir_aluno()
        input('Digite algo para continuar...')

    def adicionar_aluno(self):
        control = True
        while control:
            self.limpar_display()
            print(f'Adicionando novo aluno...')
            self.__aluno = Aluno()
            self.__aluno.matricula = self.__incrementa_matricula()
            self.__aluno.nome = input('Digite o nome do aluno: ')
            self.__aluno.notas = [int(entrada_numerica(f'Digite a {n + 1}\u00AA nota: ', maxx=10)) for n in range(4)]
            self.__dados.append(self.__aluno)
            self.__exibir_aluno()
            control = menu_numerico(menu_adicionar_aluno, [0, 1], fn_clear=self.limpar_display)

    def buscar_aluno_por_matricula(self) -> Aluno | None:
        self.limpar_display()
        print(f'Buscando aluno por matrícula...')
        matricula = entrada_numerica(f'Digite a matricula do aluno: ')
        for registro in self.__dados:
            if registro.matricula == f'{matricula:0>9}':
                self.__aluno = registro
                self.__exibir_aluno()
        if self.__aluno is None:
            print(msg_de_alerta.format(self.buscar_aluno_por_matricula.__name__, 'Aluno não encontrado!'))
        input('Digite algo para continuar...')
        return self.__aluno

    def atualizar_notas(self):
        self.__aluno = self.buscar_aluno_por_matricula()
        self.limpar_display()
        print(f'Atualizando notas do aluno {self.__aluno.nome}, matricula {self.__aluno.matricula}...')
        nova_nota = menu_numerico(
            menu_atualizar_notas.format(
                self.__aluno.notas[0],
                self.__aluno.notas[1],
                self.__aluno.notas[2],
                self.__aluno.notas[3],
            ),
            [1, 2, 3, 4],
            fn_clear=self.limpar_display
        )
        self.__aluno.notas[nova_nota - 1] = entrada_numerica('Digite a nota do aluno: ', maxx=10)
        self.__exibir_aluno()
        input('Digite algo para continuar...')
