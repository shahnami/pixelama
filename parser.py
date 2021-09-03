import json

from models.palettes import Palette
from models.properties import Properties
from models.config import Config
from models.artist import Artist
from models.artworks import *


class Parser:

    path: str
    class_type: ArtWork

    def __init__(self, *, path: str):
        self.path = path
        self.class_type = ArtWork

    def parse(self) -> ArtWork:
        print(f"[ℹ] Reading Configuration File: {self.path}")
        with open(self.path, "r") as f:
            settings = json.load(f)
            print(f"[✓] Loaded Configuration File")
            self.class_type = eval(settings["class"])
            print(f"[✓] Identified Class Type: {self.class_type.__name__}")
            return self.populate(obj=settings["configuration"])

    def populate(self, *, obj: dict) -> ArtWork:
        print(f"[ℹ] Initialising Properties Object")

        properties = Properties(
            configuration=obj['properties']).get_selected_properties()

        print(f"[ℹ] Initialising Palette")
        palette = Palette(properties=properties,
                          configuration=obj)
        print(f"[✓] Generated Palette")

        config = Config(
            pixel_size=obj["pixel_size"],
            pen_size=obj["pen_size"],
            palette=palette,
            rows=obj["rows"],
            cols=obj["cols"]
        )

        artist = Artist(configuration=config)

        print(f"[✓] Generated Configuration Object")

        DetectedClass = type(
            self.class_type.__name__,
            (ArtWork, ),
            {}
        )

        return DetectedClass(artist=artist, properties=properties)
