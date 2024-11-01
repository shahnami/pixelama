import argparse
import hashlib

from parser import Parser
from models import *


def is_unique(art: ArtWork) -> bool:
    hash_to_check = art.hash()
    with open("assets/hashes/hashes.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().replace("\n", "")
            if line == hash_to_check:
                return False
        return True


def store_hash(art: ArtWork):
    with open("assets/hashes/hashes.txt", "a") as f:
        f.write(hashlib.sha256(bytes(art)).hexdigest() + "\n")


def generate(*, config_path: str, file_name: str, is_demo: bool = False):
    try:
        print(f"[ℹ] Generating...")

        parser = Parser(path=config_path)
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
    except Exception as e:
        print(f"[✘] Error Occurred. {e}")


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser(description='Generate Pixelated Art')

        parser.add_argument(
            '-o', '--output', help='Path to save the output image', type=str)
        parser.add_argument(
            '-c', '--config', help='Path to the configuration file', type=str)
        parser.add_argument(
            '-d', '--demo', help='Execute a demo version of the script', action='store_true')

        args = parser.parse_args()
        if args.config:
            generate(config_path=args.config,
                     file_name=args.output or "", is_demo=args.demo or False)
        else:
            print(
                "[✘] Argument --config was not provided. Use -h for more information.")
    except:
        # output error, and return with an error code
        exit(0)
