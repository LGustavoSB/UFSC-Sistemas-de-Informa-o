from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []

    @property
    def clientes(self):
        return self.__clientes

    @property
    def tecnicos(self):
        return self.__tecnicos

    def inclui_cliente(self, codigo: int, nome: str):
        if isinstance(nome, str) and isinstance(codigo, int):
            novo_cliente = Cliente(nome, codigo)
        else:
            return None
        for cl in self.__clientes:
            if novo_cliente.codigo == cl.codigo:
                return None
        self.__clientes.append(novo_cliente)
        return novo_cliente

    def inclui_tecnico(self, codigo: int, nome: str):
        if isinstance(nome, str) and isinstance(codigo, int):
            tecnico = Tecnico(nome, codigo)
        else:
            return None
        for tec in self.__tecnicos:
            if tecnico.codigo == tec.codigo:
                return None
        self.__tecnicos.append(tecnico)
        return tecnico
