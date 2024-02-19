LOW_THRESHOLD = 5
HIGH_THRESHOLD = 10

password = input("Enter password")
while len(password) < LOW_THRESHOLD or len(password) > HIGH_THRESHOLD:
    print("Invalid password!")
    password = input("Enter password")
print(f"{'*'} * {len(password)}")