from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self,departamento: str, cpf: int, dias_de_emprestimo: int = 20):
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str):
        return f'Professor do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'Professor do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
