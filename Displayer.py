import operator
import ImageGenerator


class Displayer:
    def __init__(self, img):
        self.img = img
        self.ig = ImageGenerator.ImageGenerator()

    def __findDefaultColor(self):
        pixels = self.img.load()
        colorCount = {}
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                if pixels[i,j] in colorCount:
                    colorCount[pixels[i,j]] += 1
                else:
                    colorCount[pixels[i,j]] = 1
        print(colorCount)
        return max(colorCount.items(), key=operator.itemgetter(1))[0]

    def __getColumnLabels(self):
        pixels = self.img.load()
        labels = []
        for c in range(self.img.size[0]):
            currentColor = (300,300,300)
            currentCount = 0
            columnLabel = []
            for r in range(self.img.size[1]):
                if pixels[c, r] == currentColor:
                    currentCount += 1
                else:
                    if currentColor != self.defaultColor:
                        columnLabel.append((currentColor, currentCount))
                    currentColor = pixels[c, r]
                    currentCount = 1
            if currentColor != self.defaultColor:
                columnLabel.append((currentColor, currentCount))
            columnLabel.pop(0)
            labels.append(columnLabel)
        return labels

    def __getRowLabels(self):
        pixels = self.img.load()
        labels = []
        for r in range(self.img.size[1]):
            currentColor = (300, 300, 300)
            currentCount = 0
            rowLabel = []
            for c in range(self.img.size[0]):
                if pixels[c, r] == currentColor:
                    currentCount += 1
                else:
                    if currentColor != self.defaultColor:
                        rowLabel.append((currentColor, currentCount))
                    currentColor = pixels[c, r]
                    currentCount = 1
            if currentColor != self.defaultColor:
                rowLabel.append((currentColor, currentCount))
            rowLabel.pop(0)
            labels.append(rowLabel)
        return labels

    def __gatherBorderLabels(self):
        self.defaultColor = self.__findDefaultColor()
        #print(self.defaultColor)
        #print("--------------------")
        self.columnLabels = self.__getColumnLabels()
        self.rowLabels = self.__getRowLabels()

    def generatePuzzle(self, colorSet=None):
        self.__gatherBorderLabels()
        puzzle = self.ig.generatePuzzle(self.rowLabels, self.columnLabels, self.defaultColor, colorSet)
