"""
Pseudocode/Notes:
noun: items(multiple), price(for each Item)
verb: Enter price for each (items), calculate total price of all items,
      discount calculation
conditions: if total price > 100 then (discount calculation)
constants: 100 for condition, 0.10 for discount

get number_of_item
while number_of_item < 0
    display Invalid number of items!
    get number_of_item
for i in number_of_item
    get item_price
    total_price = total_price + item_price
if total_price > 100
    discount = total_price * 0.10
    total_price = total_price - discount
print total_price, number_of_item
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_VALUE = 0.10
total_price = 0

number_of_item = int(input("Number of items: "))
while number_of_item < 0:
    print("Invalid number of items!")
    number_of_item = int(input("Number of items: "))

for i in range(number_of_item):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price > DISCOUNT_THRESHOLD:
    discount = total_price * DISCOUNT_VALUE
    total_price -= discount

print(f"Total price for {number_of_item} items is ${total_price:.2f}")
