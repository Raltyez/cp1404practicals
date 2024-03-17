
COLOR_TO_HEX = {"Bole": "#b5a642", "acid green": "#b0bf1a", "amaranth": "#e52b50", "amethyst": "#9966cc",
                "apricot": "#fbceb1", "Bright Green": "#66ff00", "Bright Maroon": "#c32148", "Burgundy": "#800020",
                "Burnt Orange": "#cc5500", "Charcoal": "#36454f"}

is_true = False
while not is_true:
    try:
        color = input("Enter color: ").title()
        while color != "":
            if color in COLOR_TO_HEX:
                print(f"{color} code is {COLOR_TO_HEX[color]}")
            else:
                raise KeyError  # call exception when condition is false
            color = input("Enter color: ").title()
        is_true = True
    except KeyError:
        print("Invalid color")
