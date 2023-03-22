""" 
from alarm_clock import AlarmClock

alarm_one = AlarmClock()
alarm_two = AlarmClock()

print(f"Current time is {alarm_one.current_time}")
alarm_one.set_current_time("10:15PM")
alarm_one.toggle_alarm()
alarm_one.toggle_alarm()

print(f"Current time is {alarm_two.current_time}")
alarm_two.set_current_time("11:27PM")
alarm_two.toggle_alarm()
alarm_two.set_alarm_time("7:30PM") 
 """

from grocery.product import Product
from grocery.customer import Customer

customer_one = Customer('Bob')

apple = Product('apple', 'fruit', 2.00)
avocado = Product('banana', 'vegetable', 3.00)
chicken = Product('chicken', 'meat', 14.00)
bread = Product('bread', 'bakery', 4.00)

print(f"The first customer's name is {customer_one.name}.")

customer_one.add_item_to_cart(apple)
customer_one.add_item_to_cart(avocado)
customer_one.add_item_to_cart(chicken)
customer_one.add_item_to_cart(bread)

total = customer_one.cart.calculate_cart_total()
print(f"The total for {customer_one.name}'s cart is {total}!")

customer_one.cart.empty_products()
customer_one.see_items_in_cart()
