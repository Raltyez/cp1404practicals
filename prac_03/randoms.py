import random
print(dir(random))
help(random.randint)
help(random.randrange)
help(random.uniform)

"""
Questions:
What did you see on line 1?
What was the smallest number you could have seen, what was the largest?
The smallest number i could have seen is 5 while the largest would be 20.

What did you see on line 2?
What was the smallest number you could have seen, what was the largest?
Could line 2 have produced a 4?
The smallest number i could have seen is 3, while the largest is 9
Line 2 could not produce a 4 due to the increment of 2 from the starting value 3

What did you see on line 3?
What was the smallest number you could have seen, what was the largest?
The smallest number i could have seen is 2.5 while the largest is 5.5
"""

print(random.randint(1, 100))
