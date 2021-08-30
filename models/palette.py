class Palette:
    def __init__(self, *, skin: str, shadow: str, dark: str, cheeks: str, scarf1: str, scarf2: str, eyes: str, hat: str, background: str):
        self.skin = skin
        self.shadow = shadow
        self.dark = dark
        self.cheeks = cheeks
        self.scarf1 = scarf1
        self.scarf2 = scarf2
        self.eyes = eyes
        self.background = background
        self.hat = hat

    def __eq__(self, other):
        return self.skin == other.skin and \
            self.shadow == other.shadow and \
            self.dark == other.dark and \
            self.cheeks == other.cheeks and \
            self.scarf1 == other.scarf1 and \
            self.scarf2 == other.scarf2 and \
            self.eyes == other.eyes and \
            self.background == other.background and \
            self.hat == other.hat

    def __hash__(self):
        return hash((self.skin, self.shadow, self.dark, self.cheeks, self.scarf1, self.scarf2, self.eyes, self.hat, self.background))

    def __bytes__(self):
        return bytes(self.skin, 'utf-8') + bytes(self.shadow, 'utf-8') + bytes(self.dark, 'utf-8') + bytes(self.cheeks, 'utf-8') + bytes(self.scarf1, 'utf-8') + bytes(self.scarf2, 'utf-8') + bytes(self.eyes, 'utf-8') + bytes(self.hat, 'utf-8') + bytes(self.background, 'utf-8')
