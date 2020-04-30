import argparse
import sys

def main ():
parser = argparse.ArgumentParser(description='Name - Victoria')
parser.add_argument("nazev", "help = "napsat nazev", action = "store_true")
parser.add_argument("--znaky", "help = "napsat znaky", action = "store_true")
parser.add_argument("--slova", "help = "napsat slova",action = "store_true" )
parser.add_argument("--rad", "help = "napsat rad", action = "store_true")
args = parser.parse_args()

try:

if args.znaky and args.slova and args.rad: #"must to be"
file = open(args.nazev)
znaky = len(text)
rad = len(text.split("\n"))
slova = len(text.split(" ")) + (rad - 1)
vysledek = f"Pocet znaku {znaky} | Pocet radku {radky} | Pocet slova {slova}"

elif args.znaky and args.rad
file = open(args.nazev)
znaky = len(text)
rad = len(text.split("\n"))
vysledek = f"Pocet znaku {znaky} | Pocet radku {radky}"

elif args.znaky and args.slova:
file = open(args.nazev)
znaky = len(text)
slova = len(text.split(" ")) + (rad - 1)
vysledek = f"Pocet znaku {znaky} | Pocet slova {slova}"

elif args.znaky:
file = open(args.nazev)
znaky = len(text)
vysledek = f"Pocet znaku {znaky} | Pocet slova {slova}"

elif args.slova and args.rad:
file = open(args.nazev)
rad = len(text.split("\n"))
slova = len(text.split(" ")) + (rad - 1)
vysledek = f"Pocet radku {radky} | Pocet slova {slova}"

elif args.slova:
file = open(args.nazev)
slova = len(text.split(" ")) + (rad - 1)
vysledek = f"Pocet slova {slova}"

elif args.rad:
file = open(args.nazev)
rad = len(text.split("\n"))
vysledek = f"Pocet radku {radky}"

file.close()
