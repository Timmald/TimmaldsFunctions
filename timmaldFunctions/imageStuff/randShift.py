import random
from typing import Union

from PIL.Image import *


def randShift(img: Image, extremeness:Union[int,float] = 50):
    """
    Uses PIL.Image eval(img, function) to apply a function to all pixels in the image, adjusting their color by a random amount

    Args:
        img: A PIL.Image Image object to be randomized
        extremeness: An arbitrary number that will increase the extremeness of the randomization. Ideally from 1 to 100, but all numbers are accepted. If it is a float, it will be rounded. If it is negative, it will be made positive
    Returns:
        A PIL.Image Image object that has had the colors randomized
    """
    def pixelRandShift(num: int):
        return num + random.randint(-round(abs(extremeness)),round(abs(extremeness)))
    if extremeness==0:
        extremeness=1
    aspect = img.height / img.width
    newWidth = round(abs(10/extremeness) * img.width)
    newHeight = round(newWidth * aspect)
    if newHeight==float('inf') and newWidth==float('inf'):
        newHeight,newWidth=img.height*2,img.width*2
    img = img.resize((int(newWidth), int(newHeight)))
    return eval(img, pixelRandShift)
    #TODO: set up individual band randshift methods, make an option to separate extremeness from pixellation