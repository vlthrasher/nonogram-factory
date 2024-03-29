from PIL import Image
import ColorClusterer

#Takes an image and adjusts it so it matches a completed puzzle
#The puzzle can be uniquly derived from the returned image
#One public method: adjustImage
class ImageAdjuster:
    def __init__(self):
        self.clusterer = ColorClusterer.ColorClusterer()

    def __openImage(self, fileName):
        try:
            img = Image.open(fileName)
        except IOError:
            return
        else:
            return img

    def __resizeImage(self, img, newMax):
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

    #recolors each pixel in the image to one of the clusters derived
    def __recolorImage(self, img, clusters):
        pixels = img.load()
        for k in clusters:
            for pixel in clusters[k]:
                color = (round(k[0]), round(k[1]), round(k[2]))
                pixels[pixel[0], pixel[1]] = color
        return img

    def adjustImage(self, fileName, maxSize, clusterCount, iterations, colorSet):
        img = self.__openImage(fileName)
        if img:
            img = self.__resizeImage(img, maxSize, )
            clusters = self.clusterer.clusterColors(img, clusterCount, iterations, colorSet)
            img = self.__recolorImage(img, clusters)
        return img