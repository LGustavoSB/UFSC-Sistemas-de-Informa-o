from pilha import Pilha


class Elemento:
    def __init__(self, time):
        self.__time = time
        self.__anterior = None

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time):
        self.__time = time

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

p1 = Pilha(5)
x = Elemento('Avaí')
y = Elemento('Gremio')

p1.push(x)
print(p1.topo.anterior)
p1.push(y)
print(p1.topo.anterior.time)
p1.push(Elemento('Fig'))
print(p1.topo.anterior.time)
p1.pop()
print(p1.topo.anterior.time)
