

class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__prox = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

