from usuario_bu import UsuarioBU
from abc import ABC
from abc import abstractmethod


class Aluno(UsuarioBU, ABC):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def emprestar(self, titulo_livro: str):
        return f'de matricula "{self.matricula}" pegou emprestado o livro: {titulo_livro} com {self.dias_de_emprestimo} dias de prazo'

    def devolver(self, titulo_livro: str):
        return f'Aluno de matricula "{self.matricula}" devolveu o livro: {titulo_livro}'