# tests/test_customer.py

import pytest
from lib.customer import Customer
from lib.coffee import Coffee
from lib.order import Order

def test_customer_creation():
    customer = Customer("Shawn")
    if customer.name == "Shawn":
        print("Customer name matches.")
    else:
        print("Customer name does not match.")

def test_create_order():
    customer = Customer("Shawn")
    coffee = Coffee("Espresso")
    order = customer.create_order(coffee, 5.0)
    
    if order.customer == customer:
        print("Order customer matches.")
    else:
        print("Order customer does not match.")
    
    if order.coffee == coffee:
        print("Order coffee matches.")
    else:
        print("Order coffee does not match.")
    
    if order.price == 5.0:
        print("Order price matches.")
    else:
        print("Order price does not match.")
    
    if customer.orders() == [order]:
        print("Customer orders match.")
    else:
        print("Customer orders do not match.")
    
    if coffee.orders() == [order]:
        print("Coffee orders match.")
    else:
        print("Coffee orders do not match.")

def test_most_aficionado():
    coffee = Coffee("Espresso")
    customer1 = Customer("Shawn")
    customer2 = Customer("David")
    customer1.create_order(coffee, 4.0)
    customer2.create_order(coffee, 7.0)
    
    most_aficionado = Customer.most_aficionado(coffee)
    
    if most_aficionado == customer2:
        print("Most aficionado matches.")
    else:
        print("Most aficionado does not match.")
