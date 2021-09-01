import random
from models.properties.property import Property


class Properties:
    """
        Properties are a collection of Property objects
    """

    properties: list
    random_properties: dict

    def __init__(self, *, configuration: dict):
        self.properties = []
        self.random_properties = {}
        self.populate(configuration=configuration)

    def populate(self, *, configuration: dict):
        for i, (prop_key, prop_value) in enumerate(configuration.items()):
            list_of_odds = []
            for j, (k, v) in enumerate(prop_value.items()):
                prop = Property(
                    layer=v["layer"], name=prop_key, value=k, asset=v["asset"])
                self.properties.append(prop)
                list_of_odds += [prop] * int(v["odds"] * 100)
            self.random_properties[prop_key] = list_of_odds

    def get_random_property(self, *, key: str, k: int = 1):
        if k > 1:
            return random.choices(self.random_properties[key], k=k)
        else:
            return random.choice(self.random_properties[key])

    def __iter__(self):
        return iter(self.properties)
