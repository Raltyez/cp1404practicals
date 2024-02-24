
MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = int(input("Enter score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Enter score: "))
        elif choice == "P":
            if score < 50:
                print("Bad")
            elif score < 90:
                print("Passable")
            else:
                print("Excellent")
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice!")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")



main()
