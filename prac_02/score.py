import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_category(score)
    print(result)

    score = random.randint(-1, 101)
    result = determine_score_category(score)
    print(result)


def determine_score_category(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    return "Excellent"


main()