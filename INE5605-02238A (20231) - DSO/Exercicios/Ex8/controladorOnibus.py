from abstractControladorOnibus import AbstractControladorOnibus
from comandoInvalidoException import ComandoInvalidoException
from onibus import Onibus


class ControladorOnibus(AbstractControladorOnibus):
    def __init__(self):
        self.__onibus = None

    def ligar(self):
        a = self.__onibus.ligar()
        return a

    def desligar(self):
        a = self.__onibus.desligar()
        return a

    def embarca_pessoa(self):
        a = self.__onibus.embarca_pessoa()
        return a

    def desembarca_pessoa(self):
        a = self.__onibus.desembarca_pessoa()
        return a

    @property
    def onibus(self):
        return self.__onibus

    def inicializar_onibus(self, capacidade: int,
                           total_passageiros: int, ligado: bool):
        if (ligado is True and isinstance(capacidade, int)
            and isinstance(total_passageiros, int)
            and isinstance(ligado, bool) and
            capacidade >= total_passageiros
                and total_passageiros >= 0 and capacidade >= 0):
            self.__onibus = Onibus(capacidade, total_passageiros, ligado)
        else:
            raise ComandoInvalidoException()
