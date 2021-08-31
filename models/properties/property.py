import typing


class Property:
    """ 
        This abstract class defines a Property within an ArtWork
        Each Property must be unique
        An ArtWork can have multiple properties
    """

    name: str
    value: any
    pixels: list

    def __init__(self, name: str, value: any):
        self.name = name
        self.value = value
        self.pixels = []

    def getpixels(self):
        return self.pixels

    def setpixel(self, value):
        self.pixels.append(value)

    def __eq__(self, other):
        return self.name != other.name and self.value != other.value

    def __bytes__(self):
        return bytes(str(self), 'utf-8')

    def __str__(self):
        return str(self.name) + ", " + str(self.value)

    def __dict__(self):
        return {"name": self.name, "value": self.value, "pixels": self.pixels}
