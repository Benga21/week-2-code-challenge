# tests/test_order.py

import pytest
from lib.order import Order
from lib.coffee import Coffee
from lib.customer import Customer

def test_order_creation():
    coffee = Coffee("Espresso")
    customer = Customer("shawn")
    order = Order(customer, coffee, 3.5)
    
    #  this Check if customer matches
    if order.customer == customer:
        print("Customer matches.")
    else:
        print("Customer does not match.")

    #  this Checks if coffee matches
    if order.coffee == coffee:
        print("Coffee matches.")
    else:
        print("Coffee does not match.")

    # this Check if price matches
    if order.price == 3.5:
        print("Price matches.")
    else:
        print("Price does not match.")

