from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):
    def __init__(self, personagem: Personagem):
        self.__personagem = personagem

    def valor_total_carta(self):
        energia = self.personagem.energia
        habilidade = self.personagem.habilidade
        velocidade = self.personagem.velocidade
        resistencia = self.personagem.resistencia
        valor_total_carta = energia + habilidade + velocidade + resistencia
        return valor_total_carta

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
