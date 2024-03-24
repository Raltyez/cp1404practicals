CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Guitar:
    """Represents the guitar object"""

    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Displays the guitar name, and it's year built and price"""
        return f"{self.name} ({self.year}) : ${self.cost:.2f}"

    def __lt__(self, other):
        """Compares the year for the guitar object"""
        return self.year < other.year

    def get_age(self):
        """Get the age of the """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """determines whether the guitar is vintage or not"""
        return self.get_age() >= VINTAGE_AGE
