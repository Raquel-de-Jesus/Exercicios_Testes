from Destino import Destino
from DestinoRepository import DestinoRepository

def test_exibir_destino():
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