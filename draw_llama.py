import getopt
import sys
import typing
import random
import hashlib

from enum import Enum
from odds_handler import OddsHandler
from models.llama import Llama
from models.traits import Traits, Mood, Hat, Scarf, Optic, TraitType, Body
from models.palette import Palette
from models.config import Config
from models.artist import Artist


def get_odds(value: any, trait: TraitType) -> float:
    handler = OddsHandler()
    if trait == TraitType.HAT:
        return handler.odds_for_hat(value)
    elif trait == TraitType.OPTIC:
        return handler.odds_for_optic(value)
    elif trait == TraitType.MOOD:
        return handler.odds_for_mood(value)
    elif trait == TraitType.SCARF:
        return handler.odds_for_scarf(value)
    elif trait == TraitType.BODY:
        return handler.odds_for_body(value)


def generate_odds_options(options: list, trait: TraitType) -> list:
    new_options = []
    for option in options:
        new_options += [option] * get_odds(option, trait)
    return new_options


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


def generate_random_hat_colours() -> str:
    options = [
        "#000000", "#C19A6B", "#6E260E"
    ]
    return random.choice(options)


def generate_random_hat() -> Hat:
    options = generate_odds_options([Hat.STANDARD, Hat.HOMBURG], TraitType.HAT)
    return random.choice(options)


def get_eyes_for_mood(mood: Mood) -> str:
    return "#000000"


def get_eyes_for_optic(optic: Optic) -> str:
    if optic == Optic.COOL:
        return "#7DF9FF"
    else:
        return "#000000"


def generate_random_optic() -> Optic:
    options = generate_odds_options(
        [Optic.STANDARD, Optic.COOL], TraitType.OPTIC)
    return random.choice(options)


def get_cheeks_for_mood(mood: Mood) -> str:
    if mood == Mood.BLUSH:
        return "#f7c4c8"
    elif mood == Mood.ANGRY:
        return "#CF4339"
    elif mood == Mood.SICK:
        return "#e2fee2"
    else:
        return "#FFFFFF"


def generate_random_mood() -> Mood:
    options = generate_odds_options([Mood.STANDARD,
                                    Mood.BLUSH, Mood.ANGRY, Mood.SICK], TraitType.MOOD)
    return random.choice(options)


def get_body_colours(body: Body) -> dict:
    if body == Body.BEIGE:
        return {"body": "#faf0e6", "shadow": "#eed9c4"}
    elif body == Body.BLACK:
        return {"body": "#b2b2b2", "shadow": "#666666"}
    else:
        return {"body": "#FFFFFF", "shadow": "#EEEEEE"}


def generate_random_body() -> Optic:
    options = generate_odds_options(
        [Body.STANDARD, Body.BEIGE, Body.BLACK], TraitType.BODY)
    return random.choice(options)


def generate_random_scarf() -> Scarf:
    options = generate_odds_options(
        [Scarf.STANDARD, Scarf.PONCHO], TraitType.SCARF)
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
        scarf=generate_random_scarf(),
        optic=generate_random_optic(),
        body=generate_random_body(),
    )


def create_palette(traits: Traits) -> Palette:
    scarf_colours = generate_random_scarf_colours()
    has_optics = traits.getoptic() != Optic.STANDARD
    return Palette(
        body=get_body_colours(traits.getbody())["body"],
        shadow=get_body_colours(traits.getbody())["shadow"],
        dark="#000000",
        cheeks=get_cheeks_for_mood(traits.getmood()),
        scarf1=scarf_colours[0],
        scarf2=scarf_colours[1],
        eyes=has_optics and get_eyes_for_optic(
            traits.getoptic()) or get_eyes_for_mood(traits.getmood()),
        hat=generate_random_hat_colours(),
        background=generate_random_background()
    )


def create_llama(*, artist: Artist, traits: Traits) -> Llama:
    return Llama(
        artist=artist,
        traits=traits
    )


def generate_collection(output: str = ''):
    traits = create_traits()
    palette = create_palette(traits)
    configuration = Config(pixel_size=22, pen_size=1, palette=palette)
    artist = Artist(configuration=configuration)
    llama = create_llama(artist=artist, traits=traits)

    if is_unique(llama):
        store_hash(llama)
        if(output):
            llama.save(
                file_name='assets/output/'+output+'.svg',
                size=("1024px", "1024px")
            )
        else:
            llama.draw()
            llama.complete()
    else:
        nft_hash = hashlib.sha256(bytes(llama)).hexdigest()
        print(f"[!] - [Hash already exists] - {nft_hash}")


if __name__ == '__main__':

    argumentList = sys.argv[1:]
    options = "hps:"
    long_options = ["help", "print", "save="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:

            if currentArgument in ("-h", "--help"):
                print("Your options are: --help and --save <file_name>")
            elif currentArgument in ("-p", "--print"):
                generate_collection()
            elif currentArgument in ("-s", "--save"):
                print("Saving drawing to file:", currentValue)
                generate_collection(output=currentValue)
                exit(1)

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        exit(0)
