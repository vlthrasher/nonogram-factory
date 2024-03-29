import operator
import ImageGenerator


class Displayer:
    def __init__(self, img):
        self.img = img
        self.ig = ImageGenerator.ImageGenerator()

    def __findDefaultColor(self, level):
        pixels = self.img.load()
        colorCount = {}
        for i in range(self.img.size[0]):
            for j in range(self.img.size[1]):
                if pixels[i,j] in colorCount:
                    colorCount[pixels[i,j]] += 1
                else:
                    colorCount[pixels[i,j]] = 1
        sortedCounts = sorted(colorCount.items(), key=lambda kv: (kv[1], kv[0]))
        index = round((float(level)/5.0)*len(colorCount))-1
        return sortedCounts[index][0]

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

    def __gatherBorderLabels(self, level):
        self.defaultColor = self.__findDefaultColor(level)
        #print(self.defaultColor)
        #print("--------------------")
        self.columnLabels = self.__getColumnLabels()
        self.rowLabels = self.__getRowLabels()

    #Creates a puzzle from an image by deriving the default color and number clues and forming an image
    def generatePuzzle(self, pageSize, level=3, colorSet=None):
        self.__gatherBorderLabels(level)
        puzzle = self.ig.generatePuzzle(self.rowLabels, self.columnLabels, self.defaultColor, pageSize, colorSet)
        return puzzle
