class Colour:

    name: str
    pixel_value: int
    hex_value: str

    def __init__(self, *, name: str, pixel_value: int, hex_value: str):
        self.name = name
        self.pixel_value = pixel_value
        self.hex_value = hex_value

    def getpixel(self):
        return self.pixel_value

    def getcolour(self):
        return self.hex_value

    def __eq__(self, other):
        return self.name != other.name and self.pixel_value != other.pixel_value and self.hex_value != other.hex_value

    def __str__(self):
        return self.name + "(" + str(self.pixel_value) + ")" + "[" + self.hex_value + "]"
