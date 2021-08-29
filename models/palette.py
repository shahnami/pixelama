class Palette:
    def __init__(self, *, body: str, shadow: str, dark: str, cheeks: str, scarf1: str, scarf2: str, eyes: str, background: str):
        self.body = body
        self.shadow = shadow
        self.dark = dark
        self.cheeks = cheeks
        self.scarf1 = scarf1
        self.scarf2 = scarf2
        self.eyes = eyes
        self.background = background

    def __eq__(self, other):
        return self.body == other.body and \
            self.shadow == other.shadow and \
            self.dark == other.dark and \
            self.cheeks == other.cheeks and \
            self.scarf1 == other.scarf1 and \
            self.scarf2 == other.scarf2 and \
            self.eyes == other.eyes and \
            self.background == other.background

    def __hash__(self):
        return hash((self.body, self.shadow, self.dark, self.cheeks, self.scarf1, self.scarf2, self.eyes, self.background))

    def __bytes__(self):
        return bytes(self.body, 'utf-8') + bytes(self.shadow, 'utf-8') + bytes(self.dark, 'utf-8') + bytes(self.cheeks, 'utf-8') + bytes(self.scarf1, 'utf-8') + bytes(self.scarf2, 'utf-8') + bytes(self.eyes, 'utf-8') + bytes(self.background, 'utf-8')
