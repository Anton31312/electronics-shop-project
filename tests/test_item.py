"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

ITEM_PROD = Item('Красная панама', 2000, 3)

def test_calculate_total_price():
    assert ITEM_PROD.calculate_total_price() == 6000

def test_apply_discount():
    ITEM_PROD.pay_rate = 0.85
    ITEM_PROD.apply_discount()
    assert ITEM_PROD.price == 1700