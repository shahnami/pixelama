import getopt
import sys
from turtle import *
from models.llama import Llama
from models.traits import Traits, Category, Hat, Scarf
from models.palette import Palette

if __name__ == '__main__':

    traits = Traits(
        category=Category.STANDARD,
        hat=Hat.HOMBURG,
        scarf=Scarf.PONCHO
    )

    palette: Palette = Palette(
        body="#FFFFFF",
        shadow="#EEEEEE",
        dark="#000000",
        cheeks="pink",
        scarf1="red",
        scarf2="yellow",
        background="#006400"
    )

    llama = Llama(
        asset_path="assets/animals/llama.txt",
        traits=traits,
        palette=palette
    )

    argumentList = sys.argv[1:]
    options = "hs:"
    long_options = ["help", "save="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print("Your options are: --help and --save <file_name>")

            elif currentArgument in ("-s", "--save"):
                print("Saving drawing to file:", currentValue)
                llama.save(
                    func=llama.draw,
                    file_name='assets/output/'+currentValue+'.svg',
                    size=("1024px", "1024px")
                )
                exit(1)

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))

    llama.draw()
    llama.complete()
