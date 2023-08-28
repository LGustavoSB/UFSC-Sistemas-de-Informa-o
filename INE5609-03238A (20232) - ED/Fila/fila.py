

class Fila:
    def __init__(self, max):
        self.__max = max
        self.__dados = []*max
        self.__ini = None
        self.__fim = None

    def enqueue(self, val):
        self.__dados[self.__ini+1] = val

fila = Fila(5)
fila.enqueue(1)
