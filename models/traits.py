from enum import Enum


class Category(Enum):
    STANDARD = 1
    ZOMBIE = 2
    ALIEN = 3


class Traits:
    def __init__(self, *, category: Category):
        self.category = category
