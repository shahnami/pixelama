from enum import Enum


class TraitType(Enum):
    HAT = 1
    OPTIC = 2
    MOOD = 3
    SCARF = 4


class Optic(Enum):
    STANDARD = 1
    COOL = 2

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Mood(Enum):
    STANDARD = 1
    ANGRY = 2
    HAPPY = 3
    SICK = 4

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Hat(Enum):
    STANDARD = 1
    HOMBURG = 2

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Scarf(Enum):
    STANDARD = 1
    PONCHO = 2

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Traits:
    def __init__(self, *, mood: Mood, hat: Hat, scarf: Scarf, optic: Optic):
        self.mood = mood
        self.hat = hat
        self.scarf = scarf
        self.optic = optic

    def getmood(self):
        return self.mood

    def getoptic(self):
        return self.optic

    def gethat(self):
        return self.hat

    def getscarf(self):
        return self.scarf

    def __eq__(self, other):
        return self.mood == other.mood and self.scarf == other.scarf and self.hat == other.hat and self.optic == other.optic

    def __hash__(self):
        return hash((self.hat, self.mood, self.scarf, self.optic))

    def __bytes__(self):
        return bytes(self.hat) + bytes(self.mood) + bytes(self.scarf) + bytes(self.optic)
