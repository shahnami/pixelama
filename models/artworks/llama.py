import typing
import svgwrite

from models.svg_turtle import SvgTurtle
from models.artist import Artist
from models.config import Config
from models.traits import Mood, Traits, Hat, Scarf, Optic, Skin
from models.artworks.artwork import ArtWork
from models.properties.property import Property


class Llama(ArtWork):

    def __init__(self, *, artist: Artist, properties: [Property]):
        ArtWork.__init__(self, artist=artist, properties=properties)
