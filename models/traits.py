from enum import Enum


class TraitType(Enum):
    HAT = 1
    OPTIC = 2
    MOOD = 3
    SCARF = 4
    SKIN = 5


class Skin(Enum):
    DEFAULT = "assets/skins/default.txt"
    BEIGE = "assets/skins/beige.txt"
    BLACK = "assets/skins/black.txt"

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Optic(Enum):
    DEFAULT = ""
    COOL = "assets/optics/cool.txt"

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Mood(Enum):
    DEFAULT = ""
    ANGRY = "assets/moods/angry.txt"
    BLUSH = "assets/moods/blush.txt"
    SICK = "assets/moods/sick.txt"

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Hat(Enum):
    DEFAULT = ""
    HOMBURG = "assets/hats/homburg.txt"

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Scarf(Enum):
    DEFAULT = ""
    PONCHO = "assets/scarfs/poncho.txt"
    TIE = "assets/scarfs/tie.txt"
    BOWTIE = "assets/scarfs/bowtie.txt"

    def __str__(self):
        return str(self.name)

    def __bytes__(self):
        return bytes(str(self.name), 'utf-8')


class Traits:
    def __init__(self, *, mood: Mood, hat: Hat, scarf: Scarf, optic: Optic, skin: Skin):
        self.mood = mood
        self.hat = hat
        self.scarf = scarf
        self.optic = optic
        self.skin = skin

    def getmood(self):
        return self.mood

    def getoptic(self):
        return self.optic

    def gethat(self):
        return self.hat

    def getscarf(self):
        return self.scarf

    def getskin(self):
        return self.skin

    def __eq__(self, other):
        return self.mood == other.mood and self.scarf == other.scarf and self.hat == other.hat and self.optic == other.optic and self.skin == other.skin

    def __hash__(self):
        return hash((self.hat, self.mood, self.scarf, self.optic, self.skin))

    def __bytes__(self):
        return bytes(self.hat) + bytes(self.mood) + bytes(self.scarf) + bytes(self.optic) + bytes(self.skin)
