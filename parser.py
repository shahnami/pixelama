import json
import typing
import random

from models import *
from odds_handler import OddsHandler


class Parser:

    oddsHandler: OddsHandler
    path: str

    def __init__(self, *, path: str):
        self.path = path

    def parse(self) -> Llama:
        print(f"[ℹ] Reading Configuration File: {self.path}")
        with open(self.path, "r") as f:
            settings = json.load(f)
            self.init_odds(obj=settings["odds"])
            print(f"[✓] Loaded Configuration File")
            return self.init_configuration(obj=settings["configuration"])

    def init_configuration(self, *, obj: dict) -> Config:
        print(f"[ℹ] Initialising Configuration Object")

        traits = Traits(
            mood=self.oddsHandler.get_random(type=TraitType.MOOD),
            hat=self.oddsHandler.get_random(type=TraitType.HAT),
            scarf=self.oddsHandler.get_random(type=TraitType.SCARF),
            optic=self.oddsHandler.get_random(type=TraitType.OPTIC),
            skin=self.oddsHandler.get_random(type=TraitType.SKIN),
        )

        palette = self.init_palette(obj=obj["palette"], traits=traits)

        configuration = Config(
            pixel_size=obj["pixel_size"], pen_size=obj["pen_size"], palette=palette)
        artist = Artist(configuration=configuration)

        print(f"[✓] Generated Configuration Object")

        return Llama(
            artist=artist,
            traits=traits
        )

    def init_odds(self, *, obj: dict):
        print(f"[ℹ] Initialising Odds Handler")
        self.oddsHandler = OddsHandler(obj)
        print(f"[✓] Generated Odds Handler")

    def init_palette(self, *, obj: dict, traits: Traits) -> Palette:
        print(f"[ℹ] Initialising Palette")
        scarf_colours = traits.scarf == Scarf.DEFAULT and obj['light'][0] or random.choices(
            obj['scarfs'], k=2)

        hat_colour = traits.hat == Hat.DEFAULT and obj['light'][0] or random.choice(
            obj['hats'])

        eye_colour = traits.getoptic() != Optic.DEFAULT and random.choice(
            obj["optics"][traits.getoptic().name.lower()]) or random.choice(obj["eyes"])

        background_colour = random.choice(obj["background"])

        skin_colour = random.choice(
            obj["skin"][traits.getskin().name.lower()]["skin"])
        shadow_colour = random.choice(
            obj["skin"][traits.getskin().name.lower()]["shadow"])

        cheeks_colour = random.choice(
            obj["mood"][traits.getmood().name.lower()])

        print(f"[✓] Generated Palette")
        return Palette(
            skin=skin_colour,
            shadow=shadow_colour,
            dark=obj["dark"][0],
            cheeks=cheeks_colour,
            scarf1=scarf_colours[0],
            scarf2=scarf_colours[1],
            eyes=eye_colour,
            hat=hat_colour,
            background=background_colour
        )
