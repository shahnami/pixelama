import argparse
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


def generate(*, config_path: str, class_type: ArtWork, file_name: str, is_demo: bool = False):
    print(f"[ℹ] Generating...")

    parser = Parser(path=config_path, class_type=class_type)
    art = parser.parse()

    if not is_demo and is_unique(art):
        store_hash(art)
        if(file_name):
            art.save(
                file_name='assets/collections/'+file_name+'.svg',
                size=("1024px", "1024px")
            )
            print(
                f"[✓] Saved file to {'assets/collections/'+file_name+'.svg'}")
        else:
            art.draw()
            art.complete()
    elif is_demo:
        print(f"[ℹ] This is for demo purposes only, and will not store the hash.")
        if(file_name):
            art.save(
                file_name='assets/collections/demo/'+file_name+'.svg',
                size=("1024px", "1024px")
            )
            print(
                f"[✓] Saved file to {'assets/collections/demo/'+file_name+'.svg'}")
        else:
            art.draw()
            art.complete()
    else:
        nft_hash = hashlib.sha256(bytes(art)).hexdigest()
        print(f"[✘] Duplicate Hash - {nft_hash}")


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Generate Pixelated Art')

        parser.add_argument(
            '-o', '--output', help='Path to save the output image', type=str)
        parser.add_argument(
            '-c', '--config', help='Path to the configuration file', type=str)
        parser.add_argument('-t', '--type', help='Class Type')
        parser.add_argument(
            '-d', '--demo', help='Execute a demo version of the script', action='store_true')

        args = parser.parse_args()

        if args.config and args.type:
            generate(config_path=args.config, class_type=eval(args.type),
                     file_name=args.output or "", is_demo=args.demo or False)
        else:
            print(
                "[✘] Arguments --config and --type were not provided. Use -h for more information.")
    except:
        # output error, and return with an error code
        exit(0)
