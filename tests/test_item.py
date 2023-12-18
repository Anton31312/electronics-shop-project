"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item

ITEM_PROD = src.item.Item('Красная панама', 2000, 3)

def test_calculate_total_price():
    assert ITEM_PROD.calculate_total_price() == 6000

def test_apply_discount():
    assert ITEM_PROD.apply_discount(0.15) == 1700