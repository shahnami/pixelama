from models.palettes import Palette


class Config:
    def __init__(self, *, pixel_size: int, pen_size: int, palette: Palette):
        self.pixel_size = pixel_size
        self.pen_size = pen_size
        self.palette = palette

    def getpalette(self):
        return self.palette
