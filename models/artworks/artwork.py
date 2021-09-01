import typing
import svgwrite
import hashlib

from models.svg_turtle import SvgTurtle
from models.artist import Artist
from models.config import Config
from models.traits import Mood, Traits, Hat, Scarf, Optic, Skin
from models.properties.property import Property


class ArtWork:
    """
        An ArtWork is an abstract class that defines a piece of Art
    """

    artist: Artist
    properties: [Property]

    def __init__(self, *, artist: Artist, properties: [Property]):
        self.artist = artist
        self.properties = sorted(
            properties, key=lambda x: x.layer, reverse=False)
        self.populate()

    def draw(self):
        for prop in self.properties:
            self.draw_part(prop=prop)

    def get_property(self, name: str) -> Property:
        for prop in self.properties:
            if prop.name == name:
                return prop

    def complete(self):
        self.artist.complete()

    def reset(self):
        self.artist.reset()

    def save(self, *, file_name: str, size: tuple):
        drawing = svgwrite.Drawing(file_name, size=size)
        drawing.add(drawing.rect(
            fill=self.artist.getconfiguration().palette.background, size=("100%", "100%")))
        t = SvgTurtle(drawing)
        self.artist.switchToSave(newPen=t, newScreen=t.screen)
        self.draw()
        drawing.save()

    def populate(self, *, ignore_props: list = []):
        for prop in self.properties:
            if prop.name not in ignore_props:
                if prop.value != "default":
                    with open(str(prop.asset), "r") as f:
                        for line in f.readlines():
                            line = line.strip().replace("\n", "")
                            prop.setpixel([int(character)
                                          for character in line])

    def draw_part(self, *, prop: Property):
        self.artist.backToStart()
        pixels = prop.getpixels()
        for i in range(0, len(pixels)):
            for j in range(0, len(pixels[i])):
                if(pixels[i][j] >= 1):
                    print(self.artist.getconfiguration().getpalette(
                    ).get_random_colour(name=prop.getname(), value=prop.getvalue()))
                    self.artist.draw_pixel(colour=self.artist.getconfiguration(
                    ).getpalette().get_random_colour(prop.getname(), prop.getvalue()))
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(pixels[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

    def __eq__(self, other):
        return self.properties == other.properties and self.artist.getconfiguration().palette == other.artist.getconfiguration().palette

    def __hash__(self):
        return hashlib.sha256(bytes(self)).hexdigest()

    def __bytes__(self):
        return bytes(self.properties) + bytes(self.artist.getconfiguration().palette)
