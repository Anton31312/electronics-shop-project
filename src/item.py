from csv import DictReader


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
        with open(path, newline='') as csvfile:
            cls.all.clear()
            reader = DictReader(csvfile)
            for row in reader:
                item = row
                cls.all.append(item)

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
