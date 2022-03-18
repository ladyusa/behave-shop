from behave import *
from order import Order, OrderItem
from product import Product, ProductCatalog

@given('the store is ready to service customers')
def the_store_is_ready_to_service_customers(context):
    context.catalog = ProductCatalog()
    context.order = Order()

@given('a product {name} with price {price:f} exists')
def a_product_with_price_exists(context, name, price):
    context.catalog.add_product(name, price)

@when('I buy {name} with quantity {quantity:d}')
def i_buy_with_quantity(context, name, quantity):
    product = context.catalog.get_product(name)
    context.order.add_item(product, quantity)

@then('total should be {total:f}')
def total_should_be(context, total):
    assert context.order.get_total() == total


