from PIL import Image
import math
import random

def openImage(fileName):
    try:
        img = Image.open(fileName)
    except IOError:
        return
    else:
        return img

def resizeImage(img, newMax):
    width, height = img.size
    if width > height:
        newWidth = newMax
        percent = float(newMax)/float(width)
        newHeight = round(percent*height)
    else:
        newHeight = newMax
        percent = float(newMax)/float(height)
        newWidth = round(percent*width)
    img = img.resize((newWidth, newHeight))
    return img

if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    img = openImage(FILENAME)
    if img:
        img = resizeImage(img, 20)