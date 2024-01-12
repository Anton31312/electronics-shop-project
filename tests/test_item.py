"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from src.phone import Phone

ITEM_PROD = Item('Красная панама', 2000, 3)
ITEM_PROD_SEC = Item('Папка', 300, 100)
PHONE_PROD = Phone("iPhone 14", 120_000, 5, 2)

def test_calculate_total_price():
    assert ITEM_PROD.calculate_total_price() == 6000

def test_apply_discount():
    ITEM_PROD.pay_rate = 0.85
    ITEM_PROD.apply_discount()
    assert ITEM_PROD.price == 1700

def test_string_to_number():
    assert ITEM_PROD.string_to_number('1') == 1

def test_name():
    ITEM_PROD.name = 'Красные штаны'
    assert ITEM_PROD.name == 'Красные шт'
    assert ITEM_PROD_SEC.name == 'Папка'

def test__repr__():
    assert repr(ITEM_PROD) == "Item('Красные шт', 1700.0, 3)"

def test__str__():
    assert str(ITEM_PROD) == 'Красные шт'

def test__add__():
    assert ITEM_PROD.quantity + PHONE_PROD.quantity