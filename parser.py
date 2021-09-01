import json
import typing
import random

from models.palettes.palette import Palette
from models.properties.properties import Properties
from models.config import Config
from models.artist import Artist
from models.artworks.artwork import ArtWork
from models.artworks.llama import Llama


class Parser:

    path: str

    def __init__(self, *, path: str):
        self.path = path

    def parse(self) -> Llama:
        print(f"[ℹ] Reading Configuration File: {self.path}")
        with open(self.path, "r") as f:
            settings = json.load(f)
            print(f"[✓] Loaded Configuration File")
            return self.populate(obj=settings["configuration"])

    def populate(self, *, obj: dict) -> ArtWork:
        print(f"[ℹ] Initialising Properties Object")

        properties = Properties(configuration=obj['properties'])

        print(f"[ℹ] Initialising Palette")
        palette = Palette(properties=properties,
                          configuration=obj)
        print(f"[✓] Generated Palette")

        config = Config(pixel_size=obj["pixel_size"],
                        pen_size=obj["pen_size"], palette=palette)

        artist = Artist(configuration=config)

        print(f"[✓] Generated Configuration Object")

        return Llama(artist=artist, properties=properties)
