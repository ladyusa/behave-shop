class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class ProductCatalog:

    DEFAULT_QUANTITY = 10

    def __init__(self):
        self.products = dict()

    def add_product(self, name, price, quantity = DEFAULT_QUANTITY):
        self.products[name] = Product(name, price, quantity)

    def get_product(self, name):
        return self.products[name]
