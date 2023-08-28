

class Pilha:
    def __init__(self, max):
        self.__max = max
        self.__dados = [None]*max
        self.__num_elmnts = 0
        self.__topo = None

    def push(self, val):
        if self.__num_elmnts == self.__max:
            raise Exception
        else:
            self.__dados[self.__num_elmnts] = val
            val.anterior = self.__topo
            self.__topo = val
            self.__num_elmnts += 1

    def pop(self):
        if self.__num_elmnts > 0:
            self.__topo = self.__topo.anterior
            self.__num_elmnts -= 1
            return self.__topo
        else:
            raise Exception

    @property
    def dados(self):
        return self.__dados

    @property
    def topo(self):
        return self.__topo
