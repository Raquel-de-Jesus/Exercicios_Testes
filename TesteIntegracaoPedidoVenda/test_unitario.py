from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository

def test_baixar_estoque():
    # Arrange
    produto = Produto(1, "Café", 4, 10)

    # Act
    produto.baixar_estoque(3)
    # Assert
    assert produto.estoque == 7