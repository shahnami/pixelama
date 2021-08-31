import typing
import svgwrite

from models.svg_turtle import SvgTurtle
from models.artist import Artist
from models.config import Config
from models.traits import Mood, Traits, Hat, Scarf, Optic, Skin
from models.artworks.artwork import ArtWork


class Llama(ArtWork):

    def __init__(self, *, artist: Artist, properties: [Property]):
        ArtWork.__init__(self, artist=artist, properties=properties)

    def draw(self):
        self.draw_part(pixels=self.skin)
        self.draw_part(pixels=self.fix, ignore_zero=True)
        self.draw_part(pixels=self.hat, ignore_zero=True)
        self.draw_part(pixels=self.scarf, ignore_zero=True)
        self.draw_part(pixels=self.mood, ignore_zero=True)
        self.draw_part(pixels=self.optic, ignore_zero=True)

    def populate(self):
        ArtWork.populate(self, ignore_props=["fix"])

        # we need to do this last so ignore in abstract class
        with open("assets/artwork/llama/skins/fix.txt", "r") as f:
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                prop = self.get_property("fix")
                prop.setpixel([int(character) for character in line])
