

class Elemento:
    def __init__(self, chave):
        self.__chave = chave
        self.__prox = None
        self.__ant = None

    @property
    def chave(self):
        return self.__chave

    @property
    def prox(self):
        return self.__prox

    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

    @property
    def ant(self):
        return self.__ant

    @ant.setter
    def ant(self, novo_ant):
        self.__ant = novo_ant
