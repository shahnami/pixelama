from models.artist import Artist
from models.config import Config
from models.traits import Category, Traits, Hat, Scarf
from models.palette import Palette
import typing


class Llama:

    body: list = []
    fix: list = []
    hat: list = []
    scarf: list = []

    def __init__(self, *, asset_path: str, traits: Traits, palette: Palette):
        self.artist = Artist(
            configuration=Config(pixel_size=20, pen_size=2, palette=palette)
        )
        self.traits = traits
        self.populate(asset=asset_path)

    def draw(self):
        self.artist.backToStart()
        # Draw Body
        for i in range(0, len(self.body)):
            for j in range(0, len(self.body[i])):
                if(self.body[i][j] >= 1):
                    self.artist.draw_pixel(pixel_value=self.body[i][j])
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(self.body[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

        self.artist.backToStart()

        # Draw fix for leg overlap
        for i in range(0, len(self.fix)):
            for j in range(0, len(self.fix[i])):
                if(self.fix[i][j] >= 1):
                    self.artist.draw_pixel(
                        pixel_value=self.fix[i][j], ignore_zero=True)
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(self.fix[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

        self.artist.backToStart()

        # Draw hat
        for i in range(0, len(self.hat)):
            for j in range(0, len(self.hat[i])):
                if(self.hat[i][j] >= 1):
                    self.artist.draw_pixel(
                        pixel_value=self.hat[i][j], ignore_zero=True)
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(self.hat[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

        self.artist.backToStart()

        # Draw scarf
        for i in range(0, len(self.scarf)):
            for j in range(0, len(self.scarf[i])):
                if(self.scarf[i][j] >= 1):
                    self.artist.draw_pixel(
                        pixel_value=self.scarf[i][j], ignore_zero=True)
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(self.scarf[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)

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
