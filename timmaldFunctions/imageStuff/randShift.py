import random
from typing import Union

from PIL.Image import *


def randShift(img: Image, extremeness:Union[int,float] = 50):
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