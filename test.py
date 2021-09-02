from models.artworks.llama import Llama
from parser import Parser

if __name__ == '__main__':

    print(f"[ℹ] Generating...")

    parser = Parser(path="configs/llama.json", class_type=Llama)
    llama = parser.parse()

    llama.draw()
    llama.complete()
