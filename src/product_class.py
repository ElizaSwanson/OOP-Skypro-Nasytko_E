from src.base_product_class import BaseProduct
from src.mixin_class import MixinPrint


class Product(BaseProduct, MixinPrint):
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_data: dict) -> "Product":
        return cls(**product_data)

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is self.__class__:
            price_1 = self.__price * self.quantity
            price_2 = other.__price * other.quantity
            return price_1 + price_2
        raise TypeError
