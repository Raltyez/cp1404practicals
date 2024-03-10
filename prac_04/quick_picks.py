from random import randint
MINIMUM = 1
MAXIMUM = 45
MAX_LIST = 6

number_of_picks = int(input("How many quick picks? "))
while number_of_picks < 0:
    print("Invalid number of picks")
    number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    picks = []
    for j in range(MAX_LIST):
        number = randint(MINIMUM, MAXIMUM)
        while number in picks:
            number = randint(MINIMUM, MAXIMUM)
        picks.append(number)
    print(sorted(picks))
