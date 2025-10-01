

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
