import random
from typing import Union


def randChar():
    letters='abcdefghijklmnopqrstuvwxyz'
    return random.choice(letters)
def randString(len:Union[int,float]):
    returnString=''
    for i in range(int(round(len))):
        returnString+=randChar()
    return returnString