#!/usr/bin/env python
from sys import argv

def main ( argc: int, argv: str ):
    if argc < 4:
        print("ERROR: too few args")
        exit(1)

    if argv[1] == "-e":
        print( cifrar( argv[2], argv[3] ) )
    elif argv[1] == "-d":
        print( decifrar( argv[2], argv[3] ) )

    exit(0)


############################## MODULES #########################################

alfabeto = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

char_to_num = dict();
num_to_char = dict();
for num, char in enumerate( alfabeto ):
    char_to_num[char] = num;
    num_to_char[num] = char;


def cifrar ( texto: str, clave: str ) -> str:
    output = ""

    i = 0
    for ch in texto:
        if i == len(clave):
            i = 0

        num = char_to_num[ ch.lower() ] + char_to_num[ clave[i] ]
        output += num_to_char[ num % len(alfabeto) ]

        i += 1

    return output


def decifrar ( texto: str, clave: str ) -> str:
    output = ""

    i = 0
    for ch in texto:
        if i == len(clave):
            i = 0

        num = char_to_num[ ch.lower() ] - char_to_num[ clave[i] ]
        output += num_to_char[ num % len(alfabeto) ]

        i += 1

    return output

################################################################################

main( len(argv), argv )

