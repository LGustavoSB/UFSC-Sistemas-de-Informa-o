from lista import Lista


class Hash:
    def __init__(self, num_grupos):
        self.hash_table = [Lista() for grupo in range(num_grupos)]
        self.__num_grupos = num_grupos

    def funcao_hash(self, value):
        return value % self.__num_grupos

    def inserir_elemento(self, id_elemento):
        grupo = self.funcao_hash(id_elemento)
        self.hash_table[grupo].inserir_no_inicio(id_elemento)

    def buscar_elemento(self, id_elemento):
        pos = self.funcao_hash(id_elemento)
        return self.hash_table[pos].buscar(id_elemento)

    def remover_elemento(self, id_elemento):
        pos = self.funcao_hash(id_elemento)
        self.hash_table[pos].remover(id_elemento)


hash_table = Hash(15)
for i in range(30):
    hash_table.inserir_elemento(i)
    print(hash_table.buscar_elemento(i).valor)

hash_table.remover_elemento(15)

print(hash_table.buscar_elemento(0).valor)
