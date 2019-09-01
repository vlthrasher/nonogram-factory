import math
import random
from statistics import mean
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cmc, delta_e_cie2000
from colormath.color_conversions import convert_color


class ColorClusterer:
    def __init__(self):
        pass

    def __euclidean_distance(self, color1, color2):
        dr = color2[0] - color1[0]
        dg = color2[1] - color1[1]
        db = color2[2] - color1[2]
        dr2 = dr ** 2
        dg2 = dg ** 2
        db2 = db ** 2
        return math.sqrt(dr2 + dg2 + db2)

    #uses colormath formulas for more exact differences in color
    def __cmc_distance(self, color1, color2):
        color1 = sRGBColor(color1[0], color1[1], color1[2], is_upscaled=True)
        color1 = convert_color(color1, LabColor)
        color2 = sRGBColor(color2[0], color2[1], color2[2], is_upscaled=True)
        color2 = convert_color(color2, LabColor)
        return delta_e_cie2000(color1, color2)
        #return delta_e_cmc(color1, color2, pl=1, pc=1)

    def __colorDistance(self, color1, color2):
        #return self.__euclidean_distance(color1, color2)
        return self.__cmc_distance(color1, color2)

    #finds the closest color to the provided color that is in the colorset
    def __quantizeColor(self, iColor, colorSet):
        closestColor = (1000,1000,1000)
        dist = 1000
        for color in colorSet.getColors():
            d = self.__colorDistance(iColor, color)
            if d < dist:
                dist = d
                closestColor = color
        return closestColor

    #changes each pixel color in an image to the closest match in the colorset
    def __quantizeImage(self, img, colorSet):
        img = img.copy()
        pixels = img.load()
        colorCounts = {}
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                closestColor = self.__quantizeColor(pixels[i,j], colorSet)
                if closestColor in colorCounts:
                    colorCounts[closestColor] += 1
                else:
                    colorCounts[closestColor] = 1
                pixels[i,j] = closestColor
        return colorCounts

    #initializes the clusters to be centered at the most common pixel colors after quantizing to the colorset
    def __getColorSetClusterCenters(self, img, k, colorSet):
        counts = self.__quantizeImage(img, colorSet)
        sortedCounts = sorted(counts.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
        clusterCenters = {}
        for i in range(k):
            clusterCenters[sortedCounts[i][0]] = []
        return clusterCenters

    #picks k distinct colors from randomly (uniform) selected pixels
    def __getRandomClusterCenters(self, img, k, colorSet=None):
        pixels = img.load()
        clusterCenters = {}
        if colorSet:
            while len(clusterCenters) < k:
                x = random.randint(0, img.size[0] - 1)
                y = random.randint(0, img.size[1] - 1)
                closestColor = (300, 300, 300)
                dist = 10000
                for color in colorSet.getColors():
                    d = self.__colorDistance(color, pixels[x, y])
                    if d < dist:
                        dist = d
                        closestColor = color
                if closestColor not in clusterCenters:
                    clusterCenters[closestColor] = []
        else:
            while len(clusterCenters) < k:
                x = random.randint(0, img.size[0] - 1)
                y = random.randint(0, img.size[1] - 1)
                if pixels[x, y] not in clusterCenters:
                    clusterCenters[pixels[x, y]] = []
        return clusterCenters

    def __initializeClusters(self, img, k, colorSet=None):
        if colorSet:
            return self.__getColorSetClusterCenters(img, k, colorSet)
        else:
            return self.__getRandomClusterCenters(img, k)

    #once clusters centers have been set, determines which pixels will be assigned to each center
    def __assignPixelsToCenters(self, img, clusterCenters):
        pixels = img.load()
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                shortestDistance = 442
                for k in clusterCenters:
                    dist = self.__colorDistance(pixels[i, j], k)
                    if dist < shortestDistance:
                        cluster = k
                        shortestDistance = dist
                clusterCenters[cluster].append((i, j))
        return clusterCenters

    #averages the colors in each cluter to find the new center
    #if a colorSet is specified, matches the average color to the closest color in the colorSet
    def __recenterClusters(self, clusters, img, colorSet=None):
        newClusters = {}
        pixels = img.load()
        for k in clusters:
            if len(clusters[k]) == 0:
                randColor = random.choice(colorSet.getColors())
                while randColor in newClusters:
                    randColor = random.choice(colorSet.getColors())
                newClusters[randColor] = []
            else:
                r = []
                g = []
                b = []
                for pixel in clusters[k]:
                    color = pixels[pixel[0], pixel[1]]
                    r.append(color[0])
                    g.append(color[1])
                    b.append(color[2])
                if colorSet:
                    closestColor = self.__quantizeColor((mean(r), mean(g), mean(b)), colorSet)
                    while closestColor in newClusters:
                        closestColor = random.choice(colorSet.getColors())
                    newClusters[closestColor] = []
                else:
                    newClusters[(mean(r), mean(g), mean(b))] = []

        return newClusters

    #uses k-means clustering to reduce the number of colors in the image
    def clusterColors(self, img, k, iterations, colorSet=None):
        clusterCenters = self.__initializeClusters(img, k, colorSet)
        for i in range(iterations):
            clusters = self.__assignPixelsToCenters(img, clusterCenters)
            clusterCenters = self.__recenterClusters(clusters, img, colorSet)
        clusters = self.__assignPixelsToCenters(img, clusterCenters)
        return clusters