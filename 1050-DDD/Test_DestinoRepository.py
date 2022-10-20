from InterfaceUsuario import InterfaceUsuario
from Destino import Destino
from DestinoRepository import DestinoRepository


def test_adicionar_destino():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    ddd1 = Destino(75, "Feira de Santana")
    ddd2 = Destino(71, "Salvador")
    ddd3 = Destino(55, "São Paulo")

    # Act
    destino_repository.adicionar_destino(ddd1)
    destino_repository.adicionar_destino(ddd2)
    destino_repository.adicionar_destino(ddd3)

    # Assert
    assert len(destino_repository.lista_destino) == 3

def test_checa_se_destino_exite():
    # Arrange
    destino_repository = DestinoRepository()
    destino_repository.lista_destino = []
    ddd1 = Destino(75, "Feira de Santana")
    ddd2 = Destino(71, "Salvador")
    ddd3 = Destino(55, "São Paulo")

    # Act
    destino_repository.adicionar_destino(ddd1)
    destino_repository.adicionar_destino(ddd2)
    destino_repository.adicionar_destino(ddd3)
    ddd = 75

    # Assert
    assert destino_repository.checa_se_destino_existe(ddd) == True