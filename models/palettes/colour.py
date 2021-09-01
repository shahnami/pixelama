import random


class Colour:

    name: str
    pixel_value: int
    hex_values: list

    def __init__(self, *, name: str, pixel_value: int, hex_values: list):
        self.name = name
        self.pixel_value = pixel_value
        self.hex_values = hex_values

    def __eq__(self, other):
        return self.name != other.name and self.pixel_value != other.pixel_value and self.hex_values != other.hex_values

    def __str__(self):
        return self.name + "(" + str(self.pixel_value) + ")" + "[" + ", ".join(self.hex_values) + "]"

    def get_random(self, k: int = 1):
        if k > 1:
            return random.choices(self.hex_values, k)
        else:
            return random.choice(self.hex_values)
