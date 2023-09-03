

class Elemento:
    def __init__(self, valor):
        self.__valor = valor
        self.__prox = None
        self.__ant = None

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, novo_valor):
        self.__valor = novo_valor

    @property
    def prox(self):
        if self.__prox is None:
            return "Não tem proximo"
        return self.__prox

    @prox.setter
    def prox(self, novo_prox):
        self.__prox = novo_prox

    @property
    def ant(self):
        if self.__ant is None:
            return "Nao tem anterior"
        return self.__ant

    @ant.setter
    def ant(self, novo_ant):
        self.__ant = novo_ant

class Lista:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def inserir_primeiro_elemento(self, valor):
        if self.__inicio is None and self.__fim is None:
            primeiro_elemento = Elemento(valor)
            self.__inicio = primeiro_elemento
            self.__fim = primeiro_elemento

    def inserir_no_inicio(self, valor):
        novo_inicio = Elemento(valor)
        if self.__inicio is None:
            self.inserir_primeiro_elemento(valor)
            return
        novo_inicio.prox = self.__inicio
        self.__inicio.ant = novo_inicio
        self.__inicio = novo_inicio

    def inserir_no_fim(self, valor):
        novo_fim = Elemento(valor)
        if self.__fim is None:
            self.inserir_primeiro_elemento(valor)
        novo_fim.ant = self.__fim
        self.__fim.prox = novo_fim
        self.__fim = novo_fim

    def remover_inicio(self):
        novo_inicio = self.__inicio.prox

    def buscar(self, valor_buscado):
        elemento_atual = self.__inicio #1
        while elemento_atual.valor != valor_buscado: #1 5 3
            elemento_atual = elemento_atual.prox
        return elemento_atual

    def inserir_depois_de(self, prox, valor):
        i = self.buscar(prox)
        novo_elemento = Elemento(valor) #5
        novo_elemento.prox = i.prox #5prox = 3
        i.prox.ant = novo_elemento #3ant = 5
        novo_elemento.ant = i #5ant = 1
        i.prox = novo_elemento #1prox = 5

    def inserir_antes_de(self, ant, valor):
        i = self.buscar(ant) #1 3
        novo_elemento = Elemento(valor) #5
        novo_elemento.prox = i.prox #5prox = 3
        i.prox.ant = novo_elemento #3ant = 5
        novo_elemento.ant = i #5ant = 1
        i.prox = novo_elemento #1prox = 5

    def remover_elemento(self, valor_removido):
        if self.__inicio == valor_removido:
            self.__inicio = self.__inicio
            self.__inicio.ant = None

        elif self.__fim == valor_removido:
            self.__fim = self.__fim.ant
            self.__fim.prox = None

        else:
            elemento_atual = self.__inicio #1
            while elemento_atual:
                proximo_elemento = elemento_atual.prox #2
                if proximo_elemento.valor == valor_removido:
                    elemento_atual.prox = proximo_elemento.prox #1prox = 3
                    proximo_elemento.prox.ant = proximo_elemento.ant #3ant = 1
                    elemento_atual = None # = None
                else:
                    elemento_atual = proximo_elemento

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim


lista = Lista()
lista.inserir_no_inicio("2") #2
lista.inserir_no_fim("3") #2 3
lista.inserir_no_inicio("1") #1 2 3
lista.remover_elemento("2")# 1 3
lista.inserir_depois_de("1", "5")
print(lista.inicio.prox.valor, lista.fim.ant.valor)#3 1
print(lista.inicio.valor, lista.fim.valor) #1 3
print(lista.inicio.prox.valor, lista.fim.ant.valor)#5 5
lista.inserir_no_inicio("2") #2 1 3
print(lista.inicio.prox.valor, lista.fim.ant.valor) #1 1
print(lista.inicio.valor, lista.fim.valor) #2 3
