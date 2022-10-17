from Destino import Destino
from DestinoRepository import DestinoRepository


class InterfaceUsuario:
    def __init__(self, destino: DestinoRepository) -> None:
        self.destino = DestinoRepository

    def get_user_input(self):
        result = input(
            "Informe o DDD:")
        return self.destino.obter_destino_pelo_ddd()
    
    def exibir_destino(self):
        for item in self.destino.lista_destino:
            return item

    def saida_usuario(self):
        pass