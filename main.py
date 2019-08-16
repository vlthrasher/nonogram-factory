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

def colorDistance(color1, color2):
    dr = color2[0]-color1[0]
    dg = color2[1]-color1[1]
    db = color2[2]-color1[2]
    dr2 = dr**2
    dg2 = dg**2
    db2 = db**2
    return math.sqrt(dr2+dg2+db2)

def getClusterCenters(width, height, k):
    clusterCenters = {}
    for i in range(k):
        x = random.randint(0, width-1)
        y = random.randint(0, height-1)
        if (x, y) not in clusterCenters:
            clusterCenters[(x, y)] = []
    print(clusterCenters)
    return clusterCenters

def assignPixelsToCenters(img, clusterCenters):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            shortestDistance = 442
            for k in clusterCenters:
                dist = colorDistance(pixels[i,j], pixels[k[0],k[1]])
                if dist < shortestDistance:
                    cluster = k
                    shortestDistance = dist
            clusterCenters[cluster].append((i,j))
    print(clusterCenters)
    return clusterCenters

def clusterColors(img, k):
    clusterCenters = getClusterCenters(img.size[0], img.size[1], k)
    clusters = assignPixelsToCenters(img, clusterCenters)


if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    img = openImage(FILENAME)
    if img:
        img = resizeImage(img, 20)
        img = clusterColors(img, 5)