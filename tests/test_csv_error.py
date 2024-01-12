import pytest

from src.csv_error import InstantiateCSVError
from src.item import Item


def test_broken_file():
    with pytest.raises(InstantiateCSVError):
        path = 'src\items_test.csv'
        Item.instantiate_from_csv(path)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        path = 'src/item.csv'
        Item.instantiate_from_csv(path)