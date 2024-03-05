"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and print them"""
    datas = get_data()
    print_subject(datas)


def print_subject(datas):
    """Display data"""
    for data in datas:
        print(f"{data[0]} is taught by {data[1]:12} and has {data[2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_datas = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        subject_datas.append(parts)
    input_file.close()
    return subject_datas


main()
