from src.product_class import Product

class Category:
    category_count = 0
    product_count = 0

    name: str
    description: str
    products: str

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products if products else []

        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str


