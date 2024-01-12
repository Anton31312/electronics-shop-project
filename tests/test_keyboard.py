from src.keyboard import Keyboard

KB = Keyboard('Light A5432 KD87A', 5900, 10)
def test_init():
    assert str(KB) == "Light A5432 KD87A"

def test_change_language():
    assert str(KB.language) == "EN"

    KB.change_lang()
    assert str(KB.language) == "RU"

    KB.change_lang()
    assert str(KB.language) == "EN"