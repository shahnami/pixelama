from models.artist import Artist
from models.artworks import ArtWork
from models.properties import Properties, Property


class Punk(ArtWork):

    def __init__(self, *, artist: Artist, properties: Properties):
        ArtWork.__init__(self, artist=artist, properties=properties)
