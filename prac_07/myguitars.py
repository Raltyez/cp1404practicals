from prac_07.guitar import Guitar
FILENAME = "guitars.csv"


def main():
    """Guitar program using Guitar class"""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            guitar = Guitar(line[0], line[1], line[2])
            guitars.append(guitar)
    guitars.sort()
    print(guitars)


if __name__ == '__main__':
    main()
