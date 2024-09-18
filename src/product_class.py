class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.newprice = price
        self.quantity = quantity

    @property
    def price(self):
        return self.newprice

    @price.setter
    def price(self, value: int):
        if value <= 0:
            return "Цена не может быть нулевая"
        else:
            self.newprice = value

    @classmethod
    def new_product(cls, product_data):
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")
        return cls(name, description, price, quantity)

    def __repr__(self):
        return f"Product(name='{self.name}', description='{self.description}', price={self.price}, quantity={self.quantity})"