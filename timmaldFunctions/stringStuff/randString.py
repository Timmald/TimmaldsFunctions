import random
from typing import Union


def randChar() -> str:
    """Generates a random character from the alphabet.
    Takes no parameters.

    Returns
    ---------

    char: :class: `str`
        A string of length one containing a letter
    """
    letters='abcdefghijklmnopqrstuvwxyz'
    return random.choice(letters)
def randString(len:Union[int,float]) -> str:
    """Args:
            len: Length of the string to generate. If it is a float, will be rounded
       Returns:
           A string of length len, filled with random characters
    """
    returnString=''
    for i in range(int(round(len))):
        returnString+=randChar()
    return returnString