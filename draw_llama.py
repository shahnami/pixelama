from turtle import *
from models.llama import Llama
from models.traits import Traits, Category

if __name__ == '__main__':
    traits = Traits(category=Category.STANDARD)
    llama = Llama(asset_path="assets/llama.txt", traits=traits)
    llama.draw()
