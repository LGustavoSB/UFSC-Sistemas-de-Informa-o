from funcionario import Funcionario


class Administrativo(Funcionario):
    def __init__(self,departamento: str, cpf: int, dias_de_emprestimo: int = 10):
        super().__init__(departamento, cpf, dias_de_emprestimo)

    def emprestar(self, titulo_livro: str):
        return f'Funcionario administrativo do departamento "{self.departamento}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'Funcionario administrativo do departamento "{self.departamento}" devolveu o livro: {titulo_livro}'
