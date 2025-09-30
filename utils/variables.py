from typing import Callable

msg_de_erro: str = "\u274C Erro função <{}>: {}"
msg_de_alerta: str = "\u26D4 Atenção <{}>: {}"

dados_alunos_texto = """=> {}
Matrícula: {}
Notas: {}
Média Final: {:.2f}
Situação: {}
"""

menu_inicial_texto = """
  - Controle de notas de Alunos - 
=> Escolha o que deseja fazer a seguir:

[1] Acessar Sistema de Alunos;
[0] Sair;
?: """

menu_operacoes_sistema = """
=> Operações do Sistema:

[1] Visualizar Todos os Alunos;
[2] Adicionar Novo Aluno;
?: """

menu_adicionar_aluno = """
=> Deseja adicionar outro aluno?

[1] Sim;
[0] Retornar;
?: """
