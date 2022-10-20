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
        lista_destinos = self.destino.lista_destino
        formatText = "{0:<10} {1:<20}\n"
        destinos = formatText.format("DDD", "destino")

        for item in lista_destinos:
            destinos += formatText.format(item.DDD, item.destino,)

        return destinos


    def saida_usuario(self):
        pass