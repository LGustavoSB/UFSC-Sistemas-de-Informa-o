

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


class Lista:
    def __init__(self, valor = None):
        self.__inicio = Elemento(valor)

    def inserir_elemento(self, valor):
        novo_elemento = Elemento(valor)
        novo_elemento.prox = self.__inicio
        self.__inicio = novo_elemento

    def remover_elemento(self, valor_removido):
        elemento_atual = self.__inicio
        if elemento_atual.valor == valor_removido:
            self.__inicio = elemento_atual.prox
        else:
            while elemento_atual:
                proximo_elemento = elemento_atual.prox
                if proximo_elemento.valor == valor_removido:
                    elemento_atual.prox = proximo_elemento.prox
                    elemento_atual = None
                else:
                    elemento_atual = proximo_elemento

    @property
    def inicio(self):
        return self.__inicio


lista = Lista("11")
print(lista.inicio.valor)
lista.inserir_elemento("33")
print(lista.inicio.valor)
lista.remover_elemento("33")
print(lista.inicio.valor)
