import typing
import svgwrite

from models.svg_turtle import SvgTurtle
from models.artist import Artist
from models.config import Config
from models.traits import Mood, Traits, Hat, Scarf


class Llama:

    body: list = []
    fix: list = []
    hat: list = []
    scarf: list = []
    mood: list = []
    configuration: Config
    artist: Artist

    def __init__(self, *, asset_path: str, traits: Traits, configuration: Config):
        self.configuration = configuration
        self.traits = traits
        self.populate(asset=asset_path)

    def set_artist(self):
        self.artist = Artist(configuration=self.configuration)

    def draw(self):
        self.draw_part(pixels=self.body)
        self.draw_part(pixels=self.fix, ignore_zero=True)
        self.draw_part(pixels=self.hat, ignore_zero=True)
        self.draw_part(pixels=self.scarf, ignore_zero=True)
        self.draw_part(pixels=self.mood, ignore_zero=True)

    def complete(self):
        self.artist.complete()

    def save(self, *, file_name: str, size: tuple):
        drawing = svgwrite.Drawing(file_name, size=size)
        drawing.add(drawing.rect(
            fill=self.configuration.palette.background, size=("100%", "100%")))
        t = SvgTurtle(drawing)
        self.artist.switchToSave(newPen=t, newScreen=t.screen)
        self.draw()
        drawing.save()

    def populate(self, asset: str):
        # https://www.dcode.fr/binary-image

        # Read Body
        with open(asset, "r") as f:
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                self.body.append([int(character) for character in line])

         # Read Fix
        with open("assets/animals/fix.txt", "r") as f:
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                self.fix.append([int(character) for character in line])

        # Read Hat
        if self.traits.hat != Hat.STANDARD:
            with open(str(self.traits.hat), "r") as f:
                for line in f.readlines():
                    line = line.strip().replace("\n", "")
                    self.hat.append([int(character) for character in line])

        # Read Scarf
        if self.traits.scarf != Scarf.STANDARD:
            with open(str(self.traits.scarf), "r") as f:
                for line in f.readlines():
                    line = line.strip().replace("\n", "")
                    self.scarf.append([int(character) for character in line])

        # Read mood
        if self.traits.mood != Mood.STANDARD:
            with open(str(self.traits.mood), "r") as f:
                for line in f.readlines():
                    line = line.strip().replace("\n", "")
                    self.mood.append([int(character) for character in line])

    def draw_part(self, *, pixels: list, ignore_zero: bool = False):
        self.artist.backToStart()
        for i in range(0, len(pixels)):
            for j in range(0, len(pixels[i])):
                if(pixels[i][j] >= 1):
                    self.artist.draw_pixel(
                        pixel_value=pixels[i][j], ignore_zero=ignore_zero)
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(pixels[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

    def __eq__(self, other):
        return self.traits == other.traits and self.configuration.palette == other.configuration.palette

    def __hash__(self):
        return hash((self.traits, self.configuration.palette))

    def __bytes__(self):
        return bytes(self.traits) + bytes(self.configuration.palette)
