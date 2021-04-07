import random
from PIL.Image import *


def randShift(img: Image, extremeness: int = 50):
    def pixelRandShift(num: int):
        return num + random.randint(extremeness, -extremeness)

    aspect = img.height / img.width
    newWidth = round((extremeness / 50) * img.width)
    newHeight = round(newWidth * aspect)
    img = img.resize((newWidth, newHeight))
    return eval(img, pixelRandShift)
