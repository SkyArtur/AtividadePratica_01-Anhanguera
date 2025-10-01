from utils import *
from objects import *
from functions import *


def executar(dados_para_teste: list = None):
    app = Aplicacao(dados_para_teste)
    while True:
        app.limpar_display()
        print('  - Controle de notas de Alunos - '.upper())
        operacao_aluno = menu_numerico(menu_operacoes_sistema, [0, 1, 2, 3, 4], fn_clear=app.limpar_display)
        if operacao_aluno == 1: # Visualizar todos
            app.visualizar_alunos()
        elif operacao_aluno == 2: # Visualizar por matrícula
            app.buscar_aluno_por_matricula()
        elif operacao_aluno == 3: # Adicionar Novo
            app.adicionar_aluno()
        elif operacao_aluno == 4: # Atualizar Nota
            app.atualizar_notas()
        elif operacao_aluno == 0: # Sair
            break
        app.limpar_ciclo_de_execucao()



if __name__ == '__main__':

    executar(
        [
            Aluno(matricula='000000001', nome='Aline Ramos', notas=[10, 7.5, 8, 6]),
            Aluno(matricula='000000002', nome='Maria Almeida', notas=[8, 7.5, 7, 6]),
            Aluno(matricula='000000003', nome='João Ribeiro', notas=[10, 5, 9, 9])
        ]
    )