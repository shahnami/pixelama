from models.palettes.colour import Colour
from models.properties.properties import Properties
import random


class Palette:

    palette: list
    background: str
    primary: str
    secondary: str

    def __init__(self, *, properties: Properties, configuration: dict):
        self.primary = random.choice(configuration["primary"])
        self.secondary = random.choice(configuration["secondary"])
        self.background = random.choice(configuration["background"])

        self.palette = []

        for prop in properties:
            for i, (k, v) in enumerate(configuration["properties"][prop.getname()][prop.getvalue()]["palette"].items()):
                obj = {
                    prop.getname(): {
                        prop.getvalue(): Colour(
                            name=k, pixel_value=v["pixel"], hex_values=v["hex"])
                    }
                }
                self.palette.append(obj)

    def __bytes__(self):
        bytes_string = ''
        for colour in self.palette:
            bytes_string += bytes(colour.hex, 'utf-8')
        return bytes_string

    def get_random_colour(self, *, name: str, value: str, k: int = 1):
        for colour in self.palette:
            print(colour, name, value)
            if colour[name] == name.lower():
                return colour[name][value].get_random(k)
