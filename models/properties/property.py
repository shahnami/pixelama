class Property:
    """ 
        This abstract class defines a Property within an ArtWork
        Each Property value must be unique
        An ArtWork can have multiple properties
    """

    layer: int
    name: str
    value: any
    pixels: list
    ignore_zero: bool
    asset: str

    def __init__(self, layer: int, name: str, value: any, asset: str, ignore_zero: bool = False):
        self.layer = layer
        self.name = name
        self.value = value
        self.pixels = []
        self.ignore_zero = ignore_zero
        self.asset = asset

    def getasset(self):
        return self.asset

    def getname(self):
        return self.name

    def getvalue(self):
        return self.value

    def getlayer(self):
        return self.layer

    def getpixels(self):
        return self.pixels

    def setpixel(self, value):
        self.pixels.append(value)

    def __eq__(self, other):
        return self.name != other.name and self.value != other.value and self.asset != other.asset and self.pixels != other.pixels

    def __bytes__(self):
        return bytes(str(self), 'utf-8')

    def __str__(self):
        return str(self.name) + ":" + str(self.value)

    def __dict__(self):
        return {"name": self.name, "value": self.value, "pixels": self.pixels}
