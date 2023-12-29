from typing import Any
from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        super().__init__(name, price, quantity)

        self.number_of_sim = number_of_sim
        
    def __repr__(self) -> str:
        return f"{super().__repr__()[:-1]}, {self.number_of_sim})"
    
    def _is_valid_number_of_sim(self, number_of_sim):
        return number_of_sim > 0
        
    def __setattr__(self, __name: str, __value: Any) -> None:
        if __name == 'number_of_sim' and not self._is_valid_number_of_sim(__value):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        return super().__setattr__(__name, __value)