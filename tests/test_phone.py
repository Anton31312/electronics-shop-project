from src.phone import Phone

PHONE_PROD = Phone("iPhone 14", 120_000, 5, 2)

def test__str__phone():
    assert str(PHONE_PROD) == 'iPhone 14'

def test__repr__phone():
    assert repr(PHONE_PROD) == "Phone('iPhone 14', 120000, 5, 2)"

def test__init__phone():    
    assert PHONE_PROD.number_of_sim == 2
