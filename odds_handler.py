import random
from models.traits import Hat, Mood, Optic, Scarf, Skin, TraitType, Traits


class OddsHandler:

    hats: list = []
    skins: list = []
    scarfs: list = []
    moods: list = []
    optics: list = []

    def __init__(self, obj: dict):
        self.populate(obj)

    def populate(self, obj: dict):
        for index, (key, value) in enumerate(obj.items()):
            if key == "hat":
                for i, (hat, odd) in enumerate(value.items()):
                    self.hats += [Hat[hat.upper()]] * int((odd * 100))
            elif key == "optic":
                for i, (optic, odd) in enumerate(value.items()):
                    self.optics += [Optic[optic.upper()]] * int((odd * 100))
            elif key == "mood":
                for i, (mood, odd) in enumerate(value.items()):
                    self.moods += [Mood[mood.upper()]] * int((odd * 100))
            elif key == "scarf":
                for i, (scarf, odd) in enumerate(value.items()):
                    self.scarfs += [Scarf[scarf.upper()]] * int((odd * 100))
            elif key == "skin":
                for i, (skin, odd) in enumerate(value.items()):
                    self.skins += [Skin[skin.upper()]] * int((odd * 100))

    def get_random(self, type: TraitType) -> any:
        if type == TraitType.HAT:
            return random.choice(self.hats)
        elif type == TraitType.OPTIC:
            return random.choice(self.optics)
        elif type == TraitType.SKIN:
            return random.choice(self.skins)
        elif type == TraitType.MOOD:
            return random.choice(self.moods)
        elif type == TraitType.SCARF:
            return random.choice(self.scarfs)
