FILE_NAME = "name.txt"
NUMBER_FILE_NAME = "numbers.txt"

# 1
name = input("Enter your name: ")
out_file = open(FILE_NAME, 'w')
out_file.write(name)
out_file.close()

# 2
in_file = open(FILE_NAME, 'r')
print(f"Your name is {out_file.read()}")
in_file.close()

# 3
in_file = open(NUMBER_FILE_NAME, 'r')
number_1 = in_file.readline().strip()
number_2 = in_file.readline().strip()
total_number = int(number_1) + int(number_2)
print(total_number)
in_file.close()

# 4
total_numbers = 0
in_file = open("more_numbers.txt", 'r')
for line in in_file:
    value = in_file.read().strip()
    total_numbers += int(value)
print(total_numbers)
in_file.close()
