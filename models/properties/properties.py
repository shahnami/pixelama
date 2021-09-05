import random
from models.properties.property import Property


class Properties:
    """
        Properties are a collection of Property objects
    """

    properties: list
    all_random_properties: dict
    selected_properties: dict

    def __init__(self, *, configuration: dict, assets_path: str):
        self.properties = []
        self.all_random_properties = {}
        self.populate(configuration=configuration, assets_path=assets_path)
        self.selected_properties = self.get_random_set_of_properties()

    def populate(self, *, configuration: dict, assets_path: str):
        for i, (prop_key, prop_value) in enumerate(configuration.items()):
            list_of_odds = []
            for j, (k, v) in enumerate(prop_value.items()):
                prop = Property(
                    layer=v["layer"], name=prop_key, value=k, asset=v["asset"] and assets_path+v["asset"] or "")
                self.properties.append(prop)
                list_of_odds += [prop] * int(v["odds"] * 100)
            self.all_random_properties[prop_key] = list_of_odds

    def get_random_set_of_properties(self) -> dict:
        traits = {}
        for i, (k, v) in enumerate(self.all_random_properties.items()):
            traits.update({k: self.get_random_property(key=k)})
        return traits

    def get_selected_properties(self) -> dict:
        return self.selected_properties

    def get_random_property(self, *, key: str, k: int = 1):
        if k > 1:
            return random.choices(self.all_random_properties[key], k=k)
        else:
            return random.choice(self.all_random_properties[key])

    def __iter__(self):
        return iter(self.properties)
