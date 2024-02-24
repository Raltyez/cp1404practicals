
MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score(score)
        elif choice == "P":
            determine_score_category(score)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


def determine_score_category(score):
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")


def get_valid_score(score):
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


main()
