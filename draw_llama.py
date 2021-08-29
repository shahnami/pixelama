import getopt
import sys
import typing
import random
import hashlib
from models.llama import Llama
from models.traits import Traits, Mood, Hat, Scarf
from models.palette import Palette
from models.config import Config


def is_unique(llama: Llama) -> bool:
    hash_to_check = hashlib.sha256(bytes(llama)).hexdigest()
    with open("assets/hashes/hashes.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace("\n", "")
            if line == hash_to_check:
                return False
        return True


def store_hash(llama: Llama):
    with open("assets/hashes/hashes.txt", "a") as f:
        f.write(hashlib.sha256(bytes(llama)).hexdigest() + "\n")


def generate_random_background() -> str:
    options = [
        "#506C33", "#5C4837", "#3C2252",
        "#953830", "#9D8232", "#35547A",
        "#35547A", "#35547A", "#57226F",
        "#E16CB0", "#E16CB0", "#E16CB0"
    ]
    return random.choice(options)


def generate_random_mood() -> Mood:
    options = [Mood.STANDARD, Mood.HAPPY, Mood.ANGRY]
    return random.choice(options)


def generate_random_hat() -> Hat:
    options = [Hat.STANDARD, Hat.HOMBURG]
    return random.choice(options)


def generate_random_scarf() -> Scarf:
    options = [Scarf.STANDARD, Scarf.PONCHO]
    return random.choice(options)


def generate_random_scarf_colours() -> [str, str]:
    options = [
        "#FFF000", "#08E8DE", "#1974D2",
        "#66FF00", "#FFAA1D", "#FF007F",
        "#FF007F", "#FA30A2", "#FF73E6",
        "#B87BFF", "#A763FF", "#A763FF"
    ]
    return random.choices(options, k=2)


def create_traits() -> Traits:
    return Traits(
        mood=generate_random_mood(),
        hat=generate_random_hat(),
        scarf=generate_random_scarf()
    )


def create_palette() -> Palette:
    scarf_colours = generate_random_scarf_colours()

    return Palette(
        body="#FFFFFF",
        shadow="#EEEEEE",
        dark="#000000",
        cheeks="pink",
        scarf1=scarf_colours[0],
        scarf2=scarf_colours[1],
        eyes="red",
        background=generate_random_background()
    )


def create_llama(*, traits: Traits, configuration: Config) -> Llama:
    return Llama(
        asset_path="assets/animals/llama.txt",
        traits=traits,
        configuration=configuration
    )


def generate_collection(items: int, output: str = ''):
    for i in range(items):
        traits = create_traits()
        palette = create_palette()
        configuration = Config(pixel_size=20, pen_size=4, palette=palette)
        llama = create_llama(traits=traits, configuration=configuration)

        while not is_unique(llama):
            traits = create_traits()
            palette = create_palette()
            configuration = Config(pixel_size=20, pen_size=4, palette=palette)
            llama = create_llama(traits=traits, configuration=configuration)

        llama.set_artist()
        store_hash(llama)

        if(output):
            llama.save(
                file_name='assets/output/'+output+'.svg',
                size=("500px", "800px")
            )
        else:
            llama.draw()
            llama.complete()


if __name__ == '__main__':

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
                generate_collection(items=1, output=currentValue)
                exit(1)
            else:
                generate_collection(items=1)

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
