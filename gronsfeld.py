#!/usr/bin/env python
from sys import argv

def main ( argc: int, argv: str ):
    if argc < 4:
        print("ERROR: too few args")
        print("usage: virgenere.py [-e/-d] 'text' 'key'")
        exit(1)

    ## TODO: implement error checking for argv[3] (must be a digits string)
    if argv[1] == "-e":
        print( cifrar( argv[2], argv[3] ) )
    elif argv[1] == "-d":
        print( decifrar( argv[2], argv[3] ) )

    exit(0)


################################################################################
alfabeto = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", #"ñ",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
]

char_to_num = dict();
num_to_char = dict();
for num, char in enumerate( alfabeto ):
    char_to_num[char] = num;
    num_to_char[num] = char;


# key_list = [ "c", "d", "f", "h", "l", "n", "r", "t", "x", "c" ]
key_list = [ "b", "c", "e", "g", "k", "n", "r", "t", "x", "c" ]
gronsfeld = list()
for key in key_list:
    gronsfeld.append(key)

############################## MODULES #########################################

def cifrar ( texto: str, clave: str ) -> str:
    output = ""
    clave = clave.lower()

    i = 0
    for ch in texto.lower():
        if i == len(clave):
            i = 0

        c = gronsfeld[ int(clave[i]) ]
        enc = num_to_char[ (char_to_num[ch] + char_to_num[c]) % len(alfabeto)  ]
        output += enc

        i += 1

    return output


def decifrar ( texto: str, clave: str ) -> str:
    output = ""
    clave = clave.lower()

    i = 0
    for ch in texto.lower():
        if i == len(clave):
            i = 0

        c = gronsfeld[ int(clave[i]) ]
        enc = num_to_char[ (char_to_num[ch] - char_to_num[c]) % len(alfabeto)  ]
        output += enc

        i += 1

    return output


################################################################################

main( len(argv), argv )

