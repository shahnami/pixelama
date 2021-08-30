import typing

from turtle import *
from models.config import Config


class Artist:

    configuration: Config
    mapping: dict

    def __init__(self, *, configuration: Config):
        self.screen = Screen()
        self.configuration = configuration
        self.createMapping()
        self.screen.bgcolor(self.configuration.palette.background)

        setheading(0)
        speed(0)
        penup()

        goto(self.configuration.pen_size/2 - self.screen.window_width()/2,
             self.screen.window_height()/2 - self.configuration.pen_size/2)
        pendown()
        self.screen.tracer(False)

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
        self.screen.exitonclick()

    def createMapping(self):
        self.mapping = {
            0: self.configuration.palette.background,
            1: self.configuration.palette.skin,
            2: self.configuration.palette.shadow,
            3: self.configuration.palette.cheeks,
            4: self.configuration.palette.dark,
            5: self.configuration.palette.scarf1,
            6: self.configuration.palette.scarf2,
            7: self.configuration.palette.eyes,
            8: self.configuration.palette.hat
        }

    def backToStart(self):
        penup()
        goto(self.configuration.pen_size/2 - Screen().window_width()/2,
             Screen().window_height()/2 - self.configuration.pen_size/2)
        pendown()

    def switchToSave(self, *, newPen: any, newScreen: any):
        self.screen = newScreen
        Turtle._pen = newPen

    def reset(self):
        clear()

    def getconfiguration(self):
        return self.configuration
