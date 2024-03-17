SPECIAL_CHARACTERS = '.,-_!'


def main():
    """Create dictionary of emails to names"""
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        choice = input(f"Is your name {name.title()}? (Y/n) ").lower()
        if choice != "y" and choice != "":
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name_from_email(email):
    """Extract name from email address"""
    name = email.split('@')[0]
    for check in range(len(SPECIAL_CHARACTERS)):
        if SPECIAL_CHARACTERS[check] in name:
            return " ".join(name.split(SPECIAL_CHARACTERS[check]))
        else:
            return name


main()
