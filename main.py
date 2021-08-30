import getopt
import sys
import typing
import hashlib

from parser import Parser
from models import *


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


def generate(*, file_name: str, is_demo: bool = False):
    print(f"[ℹ] Generating...")
    parser = Parser(path="configs/llama.json")
    llama = parser.parse()

    if is_unique(llama):
        not is_demo and store_hash(llama)
        if(file_name):
            llama.save(
                file_name='assets/collections/'+file_name+'.svg',
                size=("1024px", "1024px")
            )
            print(
                f"[✓] Saved file to {'assets/collections/'+file_name+'.svg'}")
        else:
            llama.draw()
            llama.complete()
    else:
        nft_hash = hashlib.sha256(bytes(llama)).hexdigest()
        print(f"[✘] Duplicate Hash - {nft_hash}")


def demo():
    print(f"[ℹ] This is for demo purposes only, and will not store the hash.")
    generate(file_name="demo", is_demo=True)

    # traits = Traits(
    #     mood=Mood.DEFAULT,
    #     hat=Hat.DEFAULT,
    #     scarf=Scarf.BOWTIE,
    #     optic=Optic.DEFAULT,
    #     skin=Skin.DEFAULT,
    # )

    # palette = Palette(
    #     skin="#FFFFFF",
    #     shadow="#EEEEEE",
    #     dark="#000000",
    #     cheeks="#FFFFFF",
    #     scarf1="black",
    #     scarf2="gray",
    #     eyes="black",
    #     hat="black",
    #     background="#8FBDD9"
    # )

    # configuration = Config(pixel_size=22, pen_size=1, palette=palette)
    # artist = Artist(configuration=configuration)
    # llama = Llama(artist=artist, traits=traits)

    # llama.draw()
    # llama.complete()


if __name__ == '__main__':
    argumentList = sys.argv[1:]
    options = "hds:"
    long_options = ["help", "demo", "save="]

    try:
        # Parsing argument
        arguments, values = getopt.getopt(argumentList, options, long_options)

        # checking each argument
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-h", "--help"):
                print("[ℹ] Your options are: --help, --demo and --save <file_name>")
            elif currentArgument in ("-d", "--demo"):
                demo()
            elif currentArgument in ("-s", "--save"):
                generate(file_name=currentValue)
                exit(1)

    except getopt.error as err:
        # output error, and return with an error code
        print(str(err))
        exit(0)
