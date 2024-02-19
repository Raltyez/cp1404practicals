LOW_THRESHOLD = 5
HIGH_THRESHOLD = 10


def main():
    password = get_password()
    method_name(password)


def method_name(password):
    print(f"{'*'} * {len(password)}")


def get_password():
    password = input("Enter password: ")
    while len(password) < LOW_THRESHOLD or len(password) > HIGH_THRESHOLD:
        print("Invalid password!")
        password = input("Enter password: ")
    return password


main()
