

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
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__num_elementos = 0
        #self.__max = max_elements
        self.__cursor = None

    def inserir_primeiro_elemento(self, valor):
        if self.__inicio is None and self.__fim is None:
            primeiro_elemento = Elemento(valor)
            self.__inicio = primeiro_elemento
            self.__fim = primeiro_elemento
            self.__num_elementos += 1

    def inserir_no_inicio(self, valor):
        #if self.__num_elementos >= self.__max:
        #    raise Exception("Numero maximo de valores atingido")
        novo_inicio = Elemento(valor)
        if self.__inicio is None:
            self.inserir_primeiro_elemento(valor)
            return
        novo_inicio.prox = self.__inicio
        self.__inicio = novo_inicio
        self.__num_elementos += 1

    def inserir_no_fim(self, valor):
        #if self.__num_elementos >= self.__max:
        #    raise Exception("Numero maximo de valores atingido")
        novo_fim = Elemento(valor)
        if self.__fim is None:
            self.inserir_primeiro_elemento(valor)
        self.__fim.prox = novo_fim
        self.__fim = novo_fim
        self.__num_elementos += 1

    def inserir_na_posicao(self, pos, valor):
        pass

    def inserir_depois_de(self, ref, valor):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        else:
            if ref == self.__fim.valor:
                self.inserir_no_fim(valor)
            elemento_buscado = self.buscar(ref)
            novo_elemento = Elemento(valor)
            novo_elemento.prox = elemento_buscado.prox
            elemento_buscado.prox = novo_elemento

    def inserir_antes_de(self, ref, valor):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        else:
            if ref == self.__inicio.valor:
                self.inserir_no_inicio(valor)
            else:
                elemento_buscado = self.buscar(ref)
                novo_elemento = Elemento(valor)
                novo_elemento.prox = elemento_buscado
                elemento_buscado.prox = novo_elemento

    def remover_primeiro_elemento(self):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        self.__inicio = self.inicio.prox
        self.__num_elementos -= 1

    def remover_ultimo_elemento(self):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        penultimo = self.__inicio
        while penultimo.prox != self.__fim:
            penultimo = penultimo.prox
        self.__fim = penultimo
        self.__num_elementos -= 1

    def remover_da_posicao(self, pos):
        pass

    def remover(self, ref):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        else:
            if ref == self.__inicio.valor:
                self.remover_primeiro_elemento()
            elif ref == self.__fim.valor:
                self.remover_ultimo_elemento()
            else:
                elemento_atual = self.__inicio
                while elemento_atual:
                    proximo_elemento = elemento_atual.prox
                    if proximo_elemento.valor == ref:
                        elemento_atual.prox = proximo_elemento.prox
                        elemento_atual = None
                    else:
                        elemento_atual = proximo_elemento

    def acessa_primeiro(self):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        return self.__inicio

    def acessa_ultimo(self):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        return self.__fim

    def acessa_da_posicao(self):
        pass

    def buscar(self, valor_buscado):
        if self.__num_elementos == 0:
            raise Exception("Não há elementos na lista")
        elemento_atual = self.__inicio
        print(elemento_atual.valor)
        while elemento_atual.valor != valor_buscado:
            try:
                elemento_atual = elemento_atual.prox
            except Exception:
                raise Exception('Valor não encontrado na lista')
        return elemento_atual

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim

