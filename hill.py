#!/usr/bin/env python

import option as op

from math import ceil
from sys import argv
import numpy as np
from random import randint

def main ( argc: int, argv: str ):
    if argc < 2:
        print("ERROR: too few args")
        exit(1)


    texto = argv[1];

    if op.option_flag("-h"):
        print("usage: hill.py TEXTO [-e/-d] [-k]")
        print("usage: -e \t encriptar")
        print("usage: -d \t desencriptar")
        print("usage: -k \t llave")
        exit(0)

    if op.option_flag("-e"):
        clave     = op.option_arg_val("-k")

        if clave == op.NO_VALUE:
            clave = generar_clave( DEFAULT_DIMENSION )
            print(f"-> CLAVE GENERADA: '{clave}'")

        dimension = int( len(clave)**(0.5) )
        print( f"'{cifrar( texto, clave, int(dimension) ) }'" )

    elif op.option_flag("-d"):
        clave = op.option_arg_val("-k")
        if clave == op.NO_VALUE:
            print("ERROR: key parameter not provided")
            exit(1)

        dimension = int( len(clave)**(0.5) )

        print( f"'{decifrar( texto, clave, dimension ) }'" )

    exit(0)


################################################################################
alfabeto = [
    " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", #"ñ",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

char_to_num = dict();
num_to_char = dict();
for num, char in enumerate( alfabeto ):
    char_to_num[char] = num;
    num_to_char[num] = char;

############################## HELPER MODULES ##################################
DEFAULT_DIMENSION = 3

def generar_clave ( dimension: int ) -> str:
    """ ADVERTENCIA: este modulo no puede generar llaves validas """
    clave = np.empty( (dimension, dimension) )

    for i in range(dimension):
        for j in range(dimension):
            clave[i][j] = randint( 0, len(alfabeto)-1 )
    det =  np.linalg.det( clave )
    div = find_mod_inv(det, len(alfabeto))

    while ( det == 0 or not div or mcd(det, div) != 1  ):
    # while ( det != 441 and div != 25  ):
        for i in range(dimension):
            for j in range(dimension):
                clave[i][j] = randint( 0, len(alfabeto)-1 )

        det =  np.linalg.det( clave )
        div = find_mod_inv(det, len(alfabeto))

    # print(det, div)
    return array_to_str(clave)

def str_to_array ( texto: str, dimension: int ) -> np.array :
    arr = np.empty( (ceil(len(texto)/dimension), dimension) )

    i = 0
    row = 0
    for ch in texto:
        if i == dimension:
            row += 1
            i = 0

        arr[row][i] = char_to_num[ ch.lower() ]
        i += 1

    while i < dimension:
        arr[row][i] = char_to_num[" "]
        i += 1

    return arr


def array_to_str ( arr: np.array ) -> str:
    output = ""

    for j in range( arr.shape[1]):
        for i in range( arr.shape[0]):
            num = arr[i][j] % len(alfabeto)
            output += num_to_char[ round(num) ]

    return output

def mcd(a, b):
    while b != 0 :
        a, b = b, a % b
    return a

def find_mod_inv (num, mod):
    for x in range(1,mod):
        if( (num % mod) * ( x % mod) % mod == 1 ):
            return x
    return None


############################## MODULES #########################################

def cifrar ( texto: str, clave: str, dimension: int ) -> str:
    key       = str_to_array( clave, dimension )
    to_cipher = np.transpose( str_to_array(texto, dimension) )

    result = np.dot(key, to_cipher)

    return array_to_str(result)



def decifrar ( texto: str, clave: str, dimension: int ) -> str:
    clave       = str_to_array( clave, dimension )
    to_decipher = np.transpose( str_to_array(texto, dimension) )

    det = np.linalg.det(clave)
    if ( det == 0 ):
        print("ERROR: key matrix doesn't have inverse")
        exit(1)

    div = find_mod_inv(det, len(alfabeto))
    if ( not div ):
        print("ERROR: key matrix's determinant doesn't have a modulus inverse")
        exit(1)

    key = det * np.linalg.inv(clave) * div
    result = np.dot(key, to_decipher)

    return array_to_str(result)



################################################################################

main( len(argv), argv )


