

class HorarioJaReservado(Exception):
    def __init__(self, mensagem):
        self.__mensagem = mensagem
        super().__init__(self.__mensagem)
