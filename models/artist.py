import typing
import svgwrite

from turtle import *
from models.config import Config
from models.svg_turtle import SvgTurtle


class Artist:

    configuration: Config
    mapping: dict
    screen: Screen

    def __init__(self, *, configuration: Config):
        self.configuration = configuration
        self.createMapping()
        bgcolor(self.configuration.palette.background)
        setheading(0)
        speed(0)
        penup()
        self.screen = Screen()
        goto(self.configuration.pen_size/2 - self.screen.window_width()/2,
             self.screen.window_height()/2 - self.configuration.pen_size/2)
        pendown()
        tracer(False)

    def draw_pixel(self, *, pixel_value: int, ignore_zero: bool = False):
        if(ignore_zero and pixel_value == 0):
            return
        pendown()
        pensize(self.configuration.pen_size)
        color(self.mapping[pixel_value])
        begin_fill()
        for x in range(4):
            forward(self.configuration.pixel_size)
            right(90)
        end_fill()
        penup()

    def move(self, *, pixels: float, heading: int = 0):
        penup()
        setheading(heading)
        forward(pixels * self.configuration.pixel_size)
        pendown()

    def complete(self):
        hideturtle()
        done()

    def createMapping(self):
        self.mapping = {
            0: self.configuration.palette.background,
            1: self.configuration.palette.body,
            2: self.configuration.palette.shadow,
            3: self.configuration.palette.cheeks,
            4: self.configuration.palette.dark,
            5: self.configuration.palette.scarf1,
            6: self.configuration.palette.scarf2
        }

    def backToStart(self):
        penup()
        goto(self.configuration.pen_size/2 - self.screen.window_width()/2,
             self.screen.window_height()/2 - self.configuration.pen_size/2)
        pendown()

    def save(self, *, func: any, file_name: str, size: tuple):
        drawing = svgwrite.Drawing(file_name, size=size)
        drawing.add(drawing.rect(
            fill=self.configuration.palette.background, size=("100%", "100%")))
        t = SvgTurtle(drawing)
        Turtle._screen = t.screen
        Turtle._pen = t
        func()
        drawing.save()
