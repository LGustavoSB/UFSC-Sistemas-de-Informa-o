from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia


class Imovel:
    def __init__(self, codigo: int, descricao: str,
                 valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__locatarios = []
        self.__mobilias = []

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor: float):
        self.__valor = valor

    @property
    def locador(self):
        return self.__locador

    @locador.setter
    def locador(self, locador: Locador):
        self.__locador = locador

    @property
    def locatarios(self):
        return self.__locatarios

    def incluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario) and (locatario is not None):
            if locatario not in self.__locatarios:
                self.__locatarios.append(locatario)

    def excluir_locatario(self, codigo_locatario: int):
        for loc in self.__locatarios:
            if loc.codigo == codigo_locatario:
                self.__locatarios.remove(loc)

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        aux = False
        mobilia = Mobilia(codigo_mobilia, descricao_mobilia)
        if (isinstance(mobilia, Mobilia)) and (mobilia is not None):
            for mob in self.__mobilias:
                if mob.codigo == codigo_mobilia:
                    aux = True
            if aux is False:
                self.__mobilias.append(mobilia)

    def excluir_mobilia(self, codigo_mobilia: int):
        for mob in self.__mobilias:
            if mob.codigo == codigo_mobilia and isinstance(mob, Mobilia):
                self.__mobilias.remove(mob)

    def find_locatario_by_codigo(self, codigo_locatario: int):
        for loc in self.__locatarios:
            if loc.codigo == codigo_locatario:
                return loc
