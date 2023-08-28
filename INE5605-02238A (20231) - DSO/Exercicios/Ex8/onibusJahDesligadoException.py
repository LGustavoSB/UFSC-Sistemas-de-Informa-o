class OnibusJahDesligadoException(Exception):
    def __init__(self):
        super().__init__("Onibus jah esta desligado")
