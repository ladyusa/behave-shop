class OrderItem:

    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.product = product
        self.quantity = quantity

    def get_subtotal(self):
        return self.product.price * self.quantity

class Order:

    def __init__(self, id = 0):
        self.id = id
        self.items = []

    def add_item(self, product, quantity):
        self.items.append(OrderItem(product, quantity))

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.get_subtotal()
        return total

