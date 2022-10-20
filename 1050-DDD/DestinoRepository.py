from Destino import Destino

class DestinoRepository:
    lista_destino : Destino = []

    def __init__(self) -> None:
        pass

    def adicionar_destino(self, destino : Destino):
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd : int) -> bool:
        for item in self.lista_destino:
            if (ddd.code == item.code):
                return True
        return False

    def obter_destino_pelo_ddd(self,ddd:int):
        for item in self.lista_destino:
            if (ddd.code == item.code):
                return self.lista_destino[item][1]
            else:
                return "DDD não cadastrado"