from src.product_class import Product


class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    __products: list

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        quantity_count = 0
        for prod in self.__products:
            quantity_count += prod.quantity
        return f"{self.name}, количество продуктов: {quantity_count}"

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += str(product) + "\n"
        return product_str

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.__products.append(product)
            Category.product_count += 1
        else:
            raise TypeError
