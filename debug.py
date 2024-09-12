# debug.py
#  importing customer and coffe data 
from  lib.customer import Customer
from  lib.coffee import Coffee

customer = Customer("shawn")
coffee = Coffee(" Espresso")
order = customer.create_order(coffee, 6.0)
print(customer.orders())
print(coffee.orders())
print(coffee.num_orders())
print(coffee.average_price())
