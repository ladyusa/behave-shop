class Product:

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def cut_stock(self, quantity):
        self.stock = self.stock - quantity

class ProductCatalog:

    def __init__(self):
        self.products = dict()

    def add_product(self, name, price, stock):
        self.products[name] = Product(name, price, stock)

    def get_product(self, name):
        return self.products[name]
