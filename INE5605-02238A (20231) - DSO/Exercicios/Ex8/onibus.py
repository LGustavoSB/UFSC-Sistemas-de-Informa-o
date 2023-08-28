from abstractOnibus import AbstractOnibus
from onibusJahCheioException import OnibusJahCheioException
from onibusJahVazioException import OnibusJahVazioException
from onibusJahLigadoException import OnibusJahLigadoException
from onibusJahDesligadoException import OnibusJahDesligadoException


class Onibus(AbstractOnibus):
    def __init__(self, capacidade: int, total_passageiros: int, ligado: bool):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade
        if isinstance(total_passageiros, int):
            self.__total_passageiros = total_passageiros
        if isinstance(ligado, bool):
            self.__ligado = ligado

    @property
    def capacidade(self):
        return self.__capacidade

    @capacidade.setter
    def capacidade(self, capacidade: int):
        if isinstance(capacidade, int):
            self.__capacidade = capacidade

    @property
    def total_passageiros(self):
        return self.__total_passageiros

    @total_passageiros.setter
    def total_passageiros(self, total_passageiros: int):
        if isinstance(total_passageiros, int):
            self.__total_passageiros = total_passageiros

    @property
    def ligado(self):
        return self.__ligado

    def embarca_pessoa(self):
        if self.__total_passageiros >= self.__capacidade:
            raise OnibusJahCheioException()
        else:
            self.__total_passageiros += 1
            return "Passageiro embarcou"

    def desembarca_pessoa(self):
        if self.__total_passageiros == 0:
            raise OnibusJahVazioException()
        else:
            self.__total_passageiros -= 1
            return "Passageiro desembarcou"

    def ligar(self):
        if self.__ligado:
            raise OnibusJahLigadoException()
        else:
            self.__ligado = True
            return "Ônibus ligado"

    def desligar(self):
        if not self.__ligado:
            raise OnibusJahDesligadoException()
        else:
            self.__ligado = False
            return "Desligou onibus"
