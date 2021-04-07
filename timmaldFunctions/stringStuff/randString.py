import random
from typing import Union


def randChar() -> str:
    """Generates a random character from the alphabet.
    Takes no parameters.

    Returns
    ---------

    A string of length one containing a letter
    """
    letters = 'abcdefghijklmnopqrstuvwxyz'
    return random.choice(letters)


def randString(len: Union[int, float]) -> str:
    """Generates string of random characters of length `len`

    Parameters
    -----------
    **len**(`Union[int,float]`):
        The length of the random string to generate. If it is a float, it will be rounded.

    ##Returns
    A string of random characters of length len
    """
    returnString = ''
    for i in range(int(round(len))):
        returnString += randChar()
    return returnString
