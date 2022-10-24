from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.ProdutoRepository import ProdutoRepository


def test_processar_pedido():
    # Arrange
    cliente = Cliente(1, "Maria")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    produto1 = Produto(1, "Macarrão", 3.5, 10)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(produto1)

    pedido = Pedido(1, cliente, datetime.today)
    pedidoProduto = PedidoProduto()
    pedidoProduto.adicionar_produto(produto1, 5)
    pedido.adicionar_produto_pedido(pedidoProduto)

    # Act
    pedidoProduto.processar_pedido(produto1, 5)

    # Assert
    assert pedidoProduto.valor_item == 17.5


def test_baixar_estoque():
    # Arrange
    cliente = Cliente(1, "Lara")
    cliente_repository = ClienteRepository()
    cliente_repository.adicionar_cliente(cliente)

    produto = Produto(1, "Leite", 7, 8)
    produto_repository = ProdutoRepository()
    produto_repository.adicionar_produto(produto)

    pedido = Pedido(1, cliente, datetime.today)
    pedido_produto = PedidoProduto()

    # Act
    pedido_produto.adicionar_produto(produto, 4)
    pedido.adicionar_produto_pedido(pedido_produto)

    # Assert
    assert produto.estoque == 4
