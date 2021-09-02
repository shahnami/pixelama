from models.artist import Artist
from models.artworks.artwork import ArtWork
from models.properties.properties import Properties
from models.properties.property import Property
from models.palettes.colour import Colour


class Llama(ArtWork):

    custom_prop: Property

    def __init__(self, *, artist: Artist, properties: Properties):
        ArtWork.__init__(self, artist=artist, properties=properties)

    def populate(self):
        ArtWork.populate(self)

        self.custom_prop = Property(layer=0, name="fix",
                                    value="default", asset="assets/artwork/llama/skins/fix.txt")
        with open(str(self.custom_prop.asset), "r") as f:
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                self.custom_prop.setpixel([int(character)
                                           for character in line])

    def draw(self):
        ArtWork.draw(self)
        skin_property = [prop[1]
                         for prop in self.properties if prop[0] == "skin"][0]

        skin_colour = self.artist.getconfiguration(
        ).getpalette().get_colour(prop=skin_property, pixel_value=1)

        self.draw_part(prop=self.custom_prop, custom_colour=skin_colour)
