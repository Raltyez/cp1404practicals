from prac_07.guitar import Guitar
FILENAME = "guitars.csv"


def main():
    """Guitar program using Guitar class"""
    guitars = []
    read_guitar_file(guitars)
    # print(guitars)  #  Debugger

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")

    guitars.sort()

    for i in guitars:   #  Debugger
        print(i)

    write_guitar_file(guitars)


def write_guitar_file(guitars):
    with open(FILENAME, 'w') as out_file:
        for line in guitars:
            out_file.write(f"{str(line)}\n")


def read_guitar_file(guitars):
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)


if __name__ == '__main__':
    main()
