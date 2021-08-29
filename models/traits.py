from enum import Enum


class Face(Enum):
    STANDARD = ""
    ANGRY = "assets/face/angry.txt"
    HAPPY = "assets/face/happy.txt"

    def __str__(self):
        return str(self.value)


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
    def __init__(self, *, face: Face, hat: Hat, scarf: Scarf):
        self.face = face
        self.hat = hat
        self.scarf = scarf
