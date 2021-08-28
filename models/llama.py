from models.artist import Artist
from models.config import Config
from models.traits import Category, Traits

import typing


class Llama:

    pixels: list = []

    def __init__(self, *, asset_path: str, traits: Traits):
        self.artist = Artist(configuration=Config(pixel_size=15, pen_color="white",
                                                  pen_size=5, background_color="black", shadow_color="gray"))
        self.traits = traits
        self.populate(asset=asset_path)

    def draw(self):
        for i in range(0, len(self.pixels)):
            for j in range(0, len(self.pixels[i])):
                if(self.pixels[i][j] >= 1):
                    self.artist.draw_pixel(self.pixels[i][j] > 1)
                self.artist.move(pixels=1)
            self.artist.move(pixels=len(self.pixels[i]), heading=180)
            self.artist.move(pixels=1, heading=270)
            self.artist.move(pixels=0, heading=0)
        self.artist.done()

    def populate(self, asset: str):
        # https://www.dcode.fr/binary-image
        with open(asset, "r") as f:
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                self.pixels.append([int(character) for character in line])
