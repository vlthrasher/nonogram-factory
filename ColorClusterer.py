import math
import random
from statistics import mean

class ColorClusterer:
    def __init__(self):
        pass

    def clusterColors(self, img, k, iterations):
        clusterCenters = self.__getRandomClusterCenters(img, k)
        self.__getSetClusterCenters(img, k)
        for i in range(iterations):
            clusters = self.__assignPixelsToCenters(img, clusterCenters)
            clusterCenters = self.__recenterClusters(clusters, img)
        clusters = self.__assignPixelsToCenters(img, clusterCenters)
        """
        print(clusters)
        for k in clusters:
            print(len(clusters[k]))
        """
        return clusters

    def __getRandomClusterCenters(self, img, k):
        pixels = img.load()
        clusterCenters = {}
        for i in range(k):
            x = random.randint(0, img.size[0] - 1)
            y = random.randint(0, img.size[1] - 1)
            if pixels[x, y] not in clusterCenters:
                clusterCenters[pixels[x, y]] = []
        return clusterCenters

    def __getSetClusterCenters(self, img, k):
        prop = float(img.width)/float(img.width+img.height)
        print(prop)
        clusterWidth = math.floor(prop*k)
        print(clusterWidth)
        clusterHeight = math.floor(k/clusterWidth)
        print(clusterHeight)



    def __colorDistance(self, color1, color2):
        dr = color2[0] - color1[0]
        dg = color2[1] - color1[1]
        db = color2[2] - color1[2]
        dr2 = dr ** 2
        dg2 = dg ** 2
        db2 = db ** 2
        return math.sqrt(dr2 + dg2 + db2)

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

    def __recenterClusters(self, clusters, img):
        newClusters = {}
        pixels = img.load()
        for k in clusters:
            r = []
            g = []
            b = []
            for pixel in clusters[k]:
                color = pixels[pixel[0], pixel[1]]
                r.append(color[0])
                g.append(color[1])
                b.append(color[2])
            newClusters[(mean(r), mean(g), mean(b))] = []
        return newClusters