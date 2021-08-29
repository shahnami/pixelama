from models.artist import Artist
from models.config import Config
from models.traits import Face, Traits, Hat, Scarf
from models.palette import Palette
import typing


class Llama:

    body: list = []
    fix: list = []
    hat: list = []
    scarf: list = []
    face: list = []

    def __init__(self, *, asset_path: str, traits: Traits, palette: Palette):
        self.artist = Artist(
            configuration=Config(pixel_size=20, pen_size=2, palette=palette)
        )
        self.traits = traits
        self.populate(asset=asset_path)

    def draw(self):
        self.draw_part(pixels=self.body)
        self.draw_part(pixels=self.fix, ignore_zero=True)
        self.draw_part(pixels=self.hat, ignore_zero=True)
        self.draw_part(pixels=self.scarf, ignore_zero=True)
        self.draw_part(pixels=self.face, ignore_zero=True)

    def complete(self):
        self.artist.complete()

    def save(self, *, func: any, file_name: str, size: tuple):
        self.artist.save(func=func, file_name=file_name, size=size)

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

        # Read Scarf
        if self.traits.face != Face.STANDARD:
            with open(str(self.traits.face), "r") as f:
                for line in f.readlines():
                    line = line.strip().replace("\n", "")
                    self.face.append([int(character) for character in line])

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
