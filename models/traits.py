from enum import Enum


class Category(Enum):
    STANDARD = 1
    ZOMBIE = 2
    ALIEN = 3


class Hat(Enum):
    STANDARD = ""
    HOMBURG = "assets/hats/homburg.txt"

    def __str__(self):
        return str(self.value)


class Scarf(Enum):
    STANDARD = ""
    PONCHO = "assets/scarfs/poncho.txt"

    def __str__(self):
        return str(self.value)


class Traits:
    def __init__(self, *, category: Category, hat: Hat, scarf: Scarf):
        self.category = category
        self.hat = hat
        self.scarf = scarf
