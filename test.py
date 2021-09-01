from models.properties.property import Property
from models.properties.properties import Properties
from models.artworks.llama import Llama
from parser import Parser

if __name__ == '__main__':

    print(f"[ℹ] Generating...")

    parser = Parser(path="configs/llama.json")
    llama = parser.parse()

    llama.draw()
    llama.complete()
