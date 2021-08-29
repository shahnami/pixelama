from enum import Enum


class Mood(Enum):
    STANDARD = ""
    ANGRY = "assets/mood/angry.txt"
    HAPPY = "assets/mood/happy.txt"

    def __str__(self):
        return str(self.value)

    def __bytes__(self):
        return bytes(self.value, 'utf-8')


class Hat(Enum):
    STANDARD = ""
    HOMBURG = "assets/hats/homburg.txt"

    def __str__(self):
        return str(self.value)

    def __bytes__(self):
        return bytes(self.value, 'utf-8')


class Scarf(Enum):
    STANDARD = ""
    PONCHO = "assets/scarfs/poncho.txt"

    def __str__(self):
        return str(self.value)

    def __bytes__(self):
        return bytes(self.value, 'utf-8')


class Traits:
    def __init__(self, *, mood: Mood, hat: Hat, scarf: Scarf):
        self.mood = mood
        self.hat = hat
        self.scarf = scarf

    def __eq__(self, other):
        return self.mood == other.mood and self.scarf == other.scarf and self.hat == other.hat

    def __hash__(self):
        return hash((self.hat, self.mood, self.scarf))

    def __bytes__(self):
        return bytes(self.hat) + bytes(self.mood) + bytes(self.scarf)
