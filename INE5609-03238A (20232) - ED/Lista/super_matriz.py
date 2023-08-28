from super_array import SuperArray


class SuperMatriz:
    def __init__(self, n_rows, n_cols):
        if n_rows > 0 and n_rows > 0:
            self.__n_rows = n_rows
            self.__n_cols = n_cols
            self.__mat = SuperArray(0, ((n_rows * n_cols) - 1))
        else:
            raise Exception("Numero de colunas e linhas precisa ser maior que zero!")

    def atribuir(self, row, col, val):
        if row < 0 or row > self.__n_rows or col < 0 or col > self.__n_cols:
            raise IndexError
        else:
            pos = (col-1) + self.__n_cols * (row-1)
            self.__mat.dados[pos] = val

    def acessar(self, row, col):
        if row < 0 or row > self.__n_rows or col < 0 or col > self.__n_cols:
            raise IndexError
        else:
            pos = (col-1) + self.__n_cols * (row-1)
            return self.__mat.dados[pos]
    