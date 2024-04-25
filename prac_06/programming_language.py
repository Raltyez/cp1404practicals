
class ProgrammingLanguage:
    """Represents the programming language object"""

    def __init__(self, language="", typing="", reflection=False, year=int()):
        """Initial programming language instance"""
        self.language = language
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Method to check language type is dynamic"""
        if self.typing == "Dynamic":
            return True
        else:
            return False

    def __str__(self):
        """Returns a string for all attributes to the class"""
        return f"{self.language}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
