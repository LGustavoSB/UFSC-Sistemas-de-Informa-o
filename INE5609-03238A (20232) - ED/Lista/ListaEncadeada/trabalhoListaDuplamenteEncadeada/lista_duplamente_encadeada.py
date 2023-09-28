from elemento import Elemento


class Lista:
    def __init__(self):
        self.__inicio = None
        self.__fim = None
        self.__atual = None
        self.__numero_elementos = 0

    def primeiro_elemento(self, chave):
        novo_elemento = Elemento(chave)
        self.__inicio = novo_elemento
        self.__fim = novo_elemento
        self.__numero_elementos += 1

    def acessar_atual(self):
        if self.__atual is not None:
            return self.__atual
        else:
            raise Exception('Cursor não definido')

    # VERIFICAR SE HÁ ELEMENTOS, SE HÁ INICIO E SE HÁ FIM
    def inserir_antes_do_atual(self, novo):
        if not self.vazia():
            if self.__atual is not None:
                novo_elemento = Elemento(novo)
                novo_elemento.prox = self.__atual
                if self.__atual == self.__inicio:
                    self.__inicio = novo_elemento
                else:
                    novo_elemento.ant = self.__atual.ant
                    self.__atual.ant.prox = novo_elemento
                self.__atual.ant = novo_elemento
                self.__numero_elementos += 1
            else:
                raise Exception('Cursor não definido')
        else:
            raise Exception('Não existem elementos na lista')

    # VERIFICAR SE HÁ ELEMENTOS, SE HÁ INICIO E SE HÁ FIM
    def inserir_apos_atual(self, novo):
        if self.__atual is not None:
            novo_elemento = Elemento(novo)
            novo_elemento.ant = self.__atual
            if self.__atual == self.__fim:
                self.__fim = novo_elemento
            else:
                novo_elemento.prox = self.__atual.prox
                self.__atual.prox.ant = novo_elemento
            self.__atual.prox = novo_elemento
        else:
            raise Exception('Cursor não definido')
        self.__numero_elementos += 1

    # VERIFICAR SE HÁ ELEMENTOS, SE HÁ INICIO E SE HÁ FIM
    def inserir_como_ultimo(self, novo):
        novo_elemento = Elemento(novo)
        novo_elemento.ant = self.__fim
        self.__fim.prox = novo_elemento
        self.__fim = novo_elemento
        self.__numero_elementos += 1

    # VERIFICAR SE HÁ ELEMENTOS, SE HÁ INICIO E SE HÁ FIM
    def inserir_como_primeiro(self, novo):
        novo_elemento = Elemento(novo)
        novo_elemento.prox = self.__inicio
        self.__inicio.ant = novo_elemento
        self.__inicio = novo_elemento
        self.__numero_elementos += 1

    def inserir_na_posicao(self, k, novo):
        novo_elemento = Elemento(novo)
        # SE A POSIÇÃO É A PRIMEIRA INSERIR COMO PRIMEIRO
        if k == 1:
            self.inserir_como_primeiro(novo)
        # SE A POSIÇÃO É A ULTIMA INSERIR COMO ULTIMO
        elif k == self.__numero_elementos:
            self.inserir_como_ultimo(novo)
        else:
            # VERIFICAR SE A POSIÇÃO ESTÁ MAIS PROXIMA DO INICIO OU DO FIM
            if (self.__numero_elementos / k) <= (self.__numero_elementos / 2):
                # num_elementos = 10 e k = 4: 10/4 = 2.5 --> 2.5 <= 5
                cont = 1
                elemento_k = self.__inicio
                while cont != k:
                    # busca o proximo elemento esperando o contador alcançar k
                    elemento_k = elemento_k.prox
                    cont += 1
            else:
                cont = self.__numero_elementos
                elemento_k = self.__fim
                while cont != k:
                    # busca o elemento anterior esperando o contador alcançar k
                    elemento_k = elemento_k.ant
                    cont -= 1
            # definir cursor com o elemento da posição que queremos inserir
            self.__atual = elemento_k
            # inserir no lugar do cursor
            self.inserir_antes_do_atual(novo)

    def excluir_atual(self):
        if self.__atual == self.__inicio:
            self.excluir_primeiro()
        elif self.__atual == self.__fim:
            self.excluir_ultimo()
        else:
            atual = self.__atual
            self.__atual = atual.prox
            atual.prox.ant = atual.ant
            atual.ant.prox = atual.prox
            self.__numero_elementos -= 1

    def excluir_primeiro(self):
        if self.__inicio is not None:
            if self.__inicio == self.__atual:
                self.__atual = self.__inicio.prox
            self.__inicio.prox.ant = None
            self.__inicio = self.__inicio.prox
            self.__numero_elementos -= 1

    def excluir_ultimo(self):
        if self.__fim is not None:
            if self.__fim == self.__atual:
                self.__atual = self.__fim.ant
            self.__fim.ant.prox = None
            self.__fim = self.__fim.ant
            self.__numero_elementos -= 1

    def excluir_elemento(self, chave):
        self.buscar(chave)
        self.excluir_atual()

    def excluir_da_posicao(self, k):
        if k == 1:
            self.excluir_primeiro()
        elif k == self.__numero_elementos:
            self.excluir_ultimo()
        else:
            if self.__numero_elementos / k <= self.__numero_elementos / 2:
                cont = 1
                elemento_k = self.__inicio
                while cont != k:
                    elemento_k = elemento_k.prox
                    cont += 1
            else:
                cont = self.__numero_elementos
                elemento_k = self.__fim
                while cont != k:
                    elemento_k = elemento_k.ant
                    cont -= 1
            self.__atual = elemento_k
            self.excluir_atual()
            return elemento_k

    def buscar(self, chave):
        elemento_iter = self.__inicio
        while elemento_iter.chave != chave:
            if elemento_iter.prox is None:
                return False
            elemento_iter = elemento_iter.prox
        self.__atual = elemento_iter
        return True

    # FUNÇÕES PARA CONTROLE DE CURSOR:

    def avancar_k_posicoes(self, k):
        cont = 0
        while cont != k:
            if self.__atual.prox is None:
                raise IndexError('Posição vai além do fim')
            self.__atual = self.__atual.prox
            cont += 1

    def retroceder_k_posicoes(self, k):
        cont = 0
        while cont != k:
            if self.__atual.ant is None:
                raise IndexError('Posição vai além do inicio')
            self.__atual = self.__atual.ant
            cont += 1

    def ir_para_primeiro(self):
        self.__atual = self.__inicio

    def ir_para_ultimo(self):
        self.__atual = self.__fim

    # FUNCOES DE APOIO

    def vazia(self):
        if self.__numero_elementos == 0:
            return True
        return False

    def listar_lista(self):
        lista = []
        elemento_atual = self.__inicio
        while elemento_atual is not None:
            lista.append(elemento_atual.chave)
            elemento_atual = elemento_atual.prox
        return lista
