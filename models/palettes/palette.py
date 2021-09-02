import random

from models.palettes.colour import Colour
from models.properties.properties import Properties
from models.properties.property import Property


class Palette:

    colours: dict
    background: str
    primary: str
    secondary: str

    def __init__(self, *, properties: Properties, configuration: dict):
        self.primary = random.choice(configuration["primary"])
        self.secondary = random.choice(configuration["secondary"])
        self.background = random.choice(configuration["background"])

        self.colours = {}

        for _, (_, prop) in enumerate(properties.items()):
            self.colours.update({prop.getname(): {prop.getvalue(): []}})
            for _, (_, cvalue) in enumerate(configuration["properties"][prop.getname()][prop.getvalue()]["palette"].items()):
                self.colours[prop.getname()][prop.getvalue()].append(Colour(
                    name=prop.getname(), pixel_value=cvalue["pixel"], hex_value=random.choice(cvalue["hex"])))

    def __bytes__(self):
        bytes_string = bytes(self.primary, "utf-8") + bytes(self.secondary,
                                                            "utf-8") + bytes(self.background, "utf-8")
        for _, (name, colour) in enumerate(self.colours.items()):
            bytes_string += bytes(name, 'utf-8') + \
                bytes(list(colour.keys())[0], 'utf-8')
        return bytes_string

    def get_colour(self, *, prop: Property, pixel_value: int):
        name = prop.getname()
        value = prop.getvalue()

        for colour in self.colours[name][value]:
            if colour.pixel_value == pixel_value:
                return colour.getcolour()
