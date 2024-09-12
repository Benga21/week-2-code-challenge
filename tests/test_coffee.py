# tests/test_coffee.py

import pytest
from lib.coffee import Coffee
from lib.customer import Customer

def test_coffee_creation():
    coffee = Coffee("Espresso")
    customer = Customer("Shawn")
    
    print("Espresso")  
    print("Shawn")    
    
    print(f"Created coffee: {coffee.name}")
    
    if coffee.name == "Espresso":
        print("Coffee name matches.")
    else:
        print("Coffee name does not match.")

def test_num_orders():
    coffee = Coffee("Espresso")
    customer = Customer("Shawn")
    customer.create_order(coffee, 4.0)
    
    num_orders = coffee.num_orders()
    print(f"Number of orders for {coffee.name}: {num_orders}")
    
    if num_orders == 1:
        print("Number of orders matches.")
    else:
        print("Number of orders does not match.")

def test_average_price():
    coffee = Coffee("Espresso")
    customer = Customer("Shawn")
    customer.create_order(coffee, 4.0)
    customer.create_order(coffee, 6.0)
    
    average_price = coffee.average_price()
    print(f"Average price for {coffee.name}: {average_price}")
    
    if average_price == 5.0:
        print("Average price matches.")
    else:
        print("Average price does not match.")
