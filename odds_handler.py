from models.traits import Traits, Mood, Hat, Scarf, Optic


class OddsHandler:

    def odds_for_hat(self, hat: Hat) -> int:
        if hat == Hat.HOMBURG:
            return 5
        else:
            return 95

    def odds_for_optic(self, optic: Optic) -> int:
        if optic == Optic.COOL:
            return 15
        else:
            return 85

    def odds_for_mood(self, mood: Mood) -> int:
        if mood == Mood.ANGRY:
            return 15
        elif mood == Mood.HAPPY:
            return 15
        elif mood == Mood.SICK:
            return 20
        else:
            return 50

    def odds_for_scarf(self, scarf: Scarf) -> int:
        if scarf == Scarf.PONCHO:
            return 50
        else:
            return 50
