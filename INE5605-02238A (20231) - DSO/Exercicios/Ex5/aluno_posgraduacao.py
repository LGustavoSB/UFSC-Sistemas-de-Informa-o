from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo, matricula)
        self.__elaborando_tese = False

    def emprestar(self, titulo_livro: str):
        return f'Aluno de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'Aluno de matricula "{self.matricula}" devolveu o livro: {titulo_livro}'

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese
        if elaborando_tese is True:
            self.dias_de_emprestimo = self.dias_de_emprestimo * 2
