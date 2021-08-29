from models.traits import Traits, Mood, Hat, Scarf, Optic, Body


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
        elif mood == Mood.BLUSH:
            return 10
        elif mood == Mood.SICK:
            return 15
        else:
            return 60

    def odds_for_scarf(self, scarf: Scarf) -> int:
        if scarf == Scarf.PONCHO:
            return 50
        else:
            return 50

    def odds_for_body(self, body: Body) -> int:
        if body == Body.BEIGE:
            return 1
        elif body == Body.BLACK:
            return 14
        else:
            return 85
