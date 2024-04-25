"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

verb: calculate based on sales(noun)
noun: sales
output: display bonus from (verb)
"""

BONUS_THRESHOLD = 1000
DENOMINATOR = 100
sales = float(input("Enter sales: $"))
if sales < BONUS_THRESHOLD:
    bonus = 0.10
else:
    bonus = 0.15
total_bonus = sales * bonus
print(f"Your bonus is ${total_bonus:.2f}")
