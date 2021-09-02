from turtle import *
from models.config import Config


class Artist:

    configuration: Config

    def __init__(self, *, configuration: Config):
        self.screen = Screen()
        self.configuration = configuration

        self.screen.bgcolor(self.configuration.getpalette().background)

        setheading(0)
        speed(0)

        self.screen.tracer(False)

    def draw_pixel(self, *, colour: str):
        pendown()
        pensize(self.configuration.pen_size)
        color(colour)
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

    def backToStart(self):
        penup()
        goto((-self.configuration.rows * self.configuration.pixel_size) / 2 - self.configuration.pixel_size * 4,
             (self.configuration.cols * self.configuration.pixel_size) / 2 - self.configuration.pixel_size/2)
        pendown()

    def switchToSave(self, *, newPen: any, newScreen: any):
        self.screen = newScreen
        Turtle._pen = newPen

    def reset(self):
        clear()

    def getconfiguration(self):
        return self.configuration
