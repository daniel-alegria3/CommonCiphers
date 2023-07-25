
from sys import argv
import re

ARGV = " ".join( argv[1:] )
NO_VALUE = ""

def option_arg_val ( option: str, argv: str = ARGV ) -> str:
    i0 = argv.find(option)
    if i0 < 0:
        return NO_VALUE
    i0 += len(option)

    resu = re.search("-\D", argv[i0:] )
    if not resu:
        iF = len(argv)
    else:
        iF = i0 + resu.start() - 1

    return argv[ i0 : iF+1 ].strip()

def option_flag( option: str, argv: str = ARGV ) -> bool:
    return False if argv.find(option) == -1 else True

