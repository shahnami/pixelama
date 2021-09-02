from models.palettes import Palette


class Config:
    def __init__(self, *, pixel_size: int, pen_size: int, palette: Palette, rows: int = 37, cols: int = 37):
        self.pixel_size = pixel_size
        self.pen_size = pen_size
        self.palette = palette
        self.rows = rows
        self.cols = cols

    def getpalette(self):
        return self.palette
