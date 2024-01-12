
class InstantiateCSVError(Exception):
    """
    Класс-исключение для поврежденного файла
    """
    def __init__(self, *args: object) -> None:
        self.message = '_Файл item.csv поврежден_'
    
    def __str__(self) -> str:
        return self.message