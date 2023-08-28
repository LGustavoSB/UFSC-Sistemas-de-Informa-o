from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    def __init__(self):
        self.__chamados = []
        self.__tipos_chamados = []

    def total_chamados_por_tipo(self, tipo: TipoChamado):
        count = 0
        for chamado in self.__chamados:
            if tipo.codigo == chamado.tipo.codigo:
                count += 1
        return count

    def inclui_chamado(self, data: Date, cliente: Cliente,
                       tecnico: Tecnico, titulo: str, descricao: str,
                       prioridade: int, tipo: TipoChamado):
        if (isinstance(data, Date)
            and isinstance(cliente, Cliente)
            and isinstance(tecnico, Tecnico)
            and isinstance(titulo, str)
            and isinstance(descricao, str)
            and isinstance(prioridade, int)
                and isinstance(tipo, TipoChamado)):
            chamado = Chamado(data, cliente, tecnico, titulo,
                              descricao, prioridade, tipo)
        else:
            return None
        for cmd in self.__chamados:
            if (cmd.data == chamado.data
                and cmd.cliente == chamado.cliente
                and cmd.tecnico == chamado.tecnico
                    and cmd.tipo == chamado.tipo):
                return None
        self.__chamados.append(chamado)
        return chamado

    def inclui_tipochamado(self, codigo: int, nome: str, descricao: str):
        if (isinstance(codigo, int)
            and isinstance(nome, str)
                and isinstance(descricao, str)):
            tipochamado = TipoChamado(codigo, nome, descricao)
        else:
            return None
        for _ in self.__tipos_chamados:
            if tipochamado.codigo == _.codigo:
                return None
        self.__tipos_chamados.append(tipochamado)
        return tipochamado

    @property
    def tipos_chamados(self):
        return self.__tipos_chamados
