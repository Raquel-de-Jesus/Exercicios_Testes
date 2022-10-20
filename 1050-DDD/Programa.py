from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()
destino_repository.adicionar_destino(Destino(75, "Feira de Santana"))
destino_repository.adicionar_destino(Destino(71, "Salvador"))
destino_repository.adicionar_destino(Destino(55, "São Paulo"))

print(destino_repository.__str__())

