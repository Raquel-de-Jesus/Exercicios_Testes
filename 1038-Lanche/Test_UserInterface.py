from unittest import result
from Menu import Menu
from MenuRepository import MenuRepository
from Order import Order
from UserInterface import UserInterface
import pytest
import builtins
import unittest.mock as mock

def test_get_total_price():
    #Arrange
    menu_repository = MenuRepository()
    menu1 = Menu(1, "Teste0", 5)
    order = Order(1,3)
    user_interface = UserInterface(menu_repository)

    #Act
    menu_repository.set_menu_item(menu1)

    #Assert
    assert user_interface.get_total_price(order)

def test_get_user_input(monkeypatch):
    #Arrange
    menu_repository = MenuRepository()
    menu2 = Menu(2, "Teste0", 10)
    user_interface = UserInterface(menu_repository)

    #Act
    menu_repository.set_menu_item(menu2)
    monkeypatch.setattr('builtins.input', lambda _:"1 9")
    resultado = user_interface.get_user_input() 

    #Assert
    assert resultado