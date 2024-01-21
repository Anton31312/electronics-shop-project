from csv import DictReader
from src.csv_error import InstantiateCSVError

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self._name = name
        self.price = price
        self.quantity = quantity

        self.all.append(self)

    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return self.name

    def __add__(self, other):
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        raise Exception  

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self._name = name[:10]
        else:
            self._name = name

    @classmethod
    def instantiate_from_csv(cls, path):
        '''
        Класс-метод, инициализирующий экземпляры класса `Item` 
        данными из файла _src/items.csv_
        '''
        try:
            with open(path, newline='') as csvfile:
                cls.all.clear()
                reader = DictReader(csvfile)
                for row in reader:
                    if len(row) == 3:
                        __name = row['name']
                        price = row['price']
                        quantity = row['quantity']
                        item = cls(__name, price, quantity)
                        cls.all.append(item)
                    else:
                        raise(InstantiateCSVError("Файл поврежден"))    
        except InstantiateCSVError:
            return print(f"Файл поврежден -> {path}")              
        except FileNotFoundError:
            return print(f"Отсутствует файл -> {path}")
          

    @staticmethod
    def string_to_number(str_num: str) -> int:
        '''
        Статический метод. 

        :return: Число из числа-строки.
        '''
        return int(float(str_num))

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        self.all_price = self.price * self.quantity
        return self.all_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        new_price = self.pay_rate * self.price
        self.price = new_price
