from elemento import Elemento


class Lista:
    def __init__(self):
        self.__inicio = None
        self.__num_elementos = 0

    def inserir_no_inicio(self, id_elemento):
        novo_elemento = Elemento(id_elemento)
        if self.__inicio is not None:
            novo_elemento.prox = self.__inicio
        self.__inicio = novo_elemento
        self.__num_elementos += 1

    def remover(self, id_elemento):
        if self.__num_elementos == 0:
            raise Exception('Não existem elementos na lista')
        else:
            if id_elemento == self.__inicio.valor:
                self.__inicio = self.__inicio.prox
            else:
                elemento_atual = self.__inicio
                while elemento_atual:
                    proximo_elemento = elemento_atual.prox
                    if proximo_elemento.valor == id_elemento:
                        elemento_atual.prox = proximo_elemento.prox
                        elemento_atual = None
                    else:
                        elemento_atual = proximo_elemento
        self.__num_elementos -= 1

    def buscar(self, id_elemento):
        elemento_atual = self.__inicio
        while elemento_atual.valor != id_elemento:
            elemento_atual = elemento_atual.prox
            if elemento_atual is None:
                raise Exception('Valor não encontrado na lista')
        return elemento_atual

