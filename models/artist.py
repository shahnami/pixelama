from turtle import *
from models.config import Config
import typing


class Artist:

    configuration: Config

    def __init__(self, *, configuration: Config):
        self.configuration = configuration
        bgcolor(configuration.background_color)
        setheading(0)
        speed(0)
        penup()
        screen = Screen()
        goto(self.configuration.pen_size/2 - screen.window_width()/2,
             screen.window_height()/2 - self.configuration.pen_size/2)
        pendown()
        tracer(False)

    def draw_pixel(self, is_shadow: bool = False):

        pendown()
        pensize(self.configuration.pen_size)
        color(
            is_shadow and self.configuration.shadow_color or self.configuration.pen_color)
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

    def done(self):
        hideturtle()
        done()
