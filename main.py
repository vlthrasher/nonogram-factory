from PIL import Image
import math
import random
from statistics import mean

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

def getClusterCenters(img, k):
    pixels = img.load()
    clusterCenters = {}
    for i in range(k):
        x = random.randint(0, img.size[0]-1)
        y = random.randint(0, img.size[1]-1)
        if pixels[x,y] not in clusterCenters:
            clusterCenters[pixels[x,y]] = []
    print(clusterCenters)
    return clusterCenters

def assignPixelsToCenters(img, clusterCenters):
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            shortestDistance = 442
            for k in clusterCenters:
                dist = colorDistance(pixels[i,j], k)
                if dist < shortestDistance:
                    cluster = k
                    shortestDistance = dist
            clusterCenters[cluster].append((i,j))
    print(clusterCenters)
    return clusterCenters

def recenterClusters(clusters, img):
    newClusters = {}
    pixels = img.load()
    for k in clusters:
        r = []
        g = []
        b = []
        for pixel in clusters[k]:
            color = pixels[pixel[0],pixel[1]]
            r.append(color[0])
            g.append(color[1])
            b.append(color[2])
        newClusters[(mean(r), mean(g), mean(b))] = []
    return newClusters

def clusterColors(img, k, iterations):
    clusterCenters = getClusterCenters(img, k)
    for i in range(iterations):
        clusters = assignPixelsToCenters(img, clusterCenters)
        clusterCenters = recenterClusters(clusters, img)
    clusters = assignPixelsToCenters(img, clusterCenters)
    print(clusters)
    for k in clusters:
        print(len(clusters[k]))
    return clusters

def recolorImage(img, clusters):
    pixels = img.load()
    for k in clusters:
        for pixel in clusters[k]:
            color = (round(k[0]), round(k[1]), round(k[2]))
            pixels[pixel[0], pixel[1]] = color
    return img

if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    img = openImage(FILENAME)
    if img:
        img = resizeImage(img, 20)
        clusters = clusterColors(img, 7, 5)
        img = recolorImage(img, clusters)
        img.show()