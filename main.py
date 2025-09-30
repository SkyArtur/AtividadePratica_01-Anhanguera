from utils import *


if __name__ == '__main__':
    db = BancoDeDados(
        [
            Aluno(matricula='000000001', nome='Aline Ramos', notas=[10, 7.5, 8, 6]),
            Aluno(matricula='000000002', nome='Maria Almeida', notas=[8, 7.5, 7, 6]),
            Aluno(matricula='000000003', nome='João Ribeiro', notas=[10, 5, 9, 9])
        ]
    )
    while True:
        executar = menu_numerico(menu_inicial_texto, [0, 1])
        if executar == 1:
            operacao_aluno = menu_numerico(menu_operacoes_sistema, [1, 2])
            if operacao_aluno == 1:
                db.visualizar_alunos()
            elif operacao_aluno == 2:
                db.adicionar_aluno()
        else:
            break
