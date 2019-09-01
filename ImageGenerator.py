from PIL import Image, ImageDraw, ImageFont
from math import floor
import Colors

class ImageGenerator:
    def __init__(self):
        pass

    def __findGridDims(self):
        maxClueRows = 0
        maxClueColumns = 0
        for row in self.rowLabels:
            if len(row) > maxClueRows:
                maxClueRows = len(row)
        for column in self.columnLabels:
            if len(column) > maxClueColumns:
                maxClueColumns = len(column)
        emptyRows = len(self.rowLabels)
        emptyColumns = len(self.columnLabels)
        return emptyRows, emptyColumns, maxClueRows, maxClueColumns

    def __getImageSize(self, gridWidth, gridHeight, pageSize):
        minWidth = ((gridWidth * self.BOX_SIZE) + 2 * self.WIDTH_BUFFER)
        minHeight = ((gridHeight * self.BOX_SIZE) + 2 * self.HEIGHT_BUFFER)
        if minWidth < minHeight:
            pageWidthDim = min(pageSize)
            pageHeightDim = max(pageSize)
        else:
            pageWidthDim = max(pageSize)
            pageHeightDim = min(pageSize)

        if (pageWidthDim*minHeight)/float(pageHeightDim) < minWidth:
            pageHeight = round((pageHeightDim*minWidth)/float(pageWidthDim))
            pageWidth = minWidth
        else:
            pageWidth = round((pageWidthDim*minHeight)/float(pageHeightDim))
            pageHeight = minHeight

        return pageWidth, pageHeight

    def __drawGrid_HeavyLines(self):
        upper = self.grid_ul
        lower = (upper[0], self.img.size[1]-self.HEIGHT_BUFFER)
        upper = (upper[0] + (self.BOX_SIZE * 5), upper[1])
        lower = (lower[0] + (self.BOX_SIZE * 5), lower[1])
        while upper[0] < self.img.size[0]-self.WIDTH_BUFFER:
            self.drawer.line([upper, lower], fill=(0,0,0), width = self.BOX_LINE_WEIGHT*3)
            upper = (upper[0]+(self.BOX_SIZE*5), upper[1])
            lower = (lower[0]+(self.BOX_SIZE*5), lower[1])

        left = self.grid_ul
        right = (self.img.size[0]-self.WIDTH_BUFFER, left[1])
        left = (left[0], left[1] + (self.BOX_SIZE * 5))
        right = (right[0], right[1] + (self.BOX_SIZE * 5))
        while left[1] < self.img.size[1]-self.HEIGHT_BUFFER:
            self.drawer.line([left, right], fill=(0, 0, 0), width=self.BOX_LINE_WEIGHT * 3)
            left = (left[0], left[1] + (self.BOX_SIZE * 5))
            right = (right[0], right[1] + (self.BOX_SIZE * 5))

    def __drawGrid(self, totalRows, totalColumns, maxRow, maxColumn):
        width = self.img.size[0]
        height = self.img.size[1]
        self.drawer = ImageDraw.Draw(self.img)
        lr = (width - self.WIDTH_BUFFER, height - self.HEIGHT_BUFFER)
        for r in range(totalRows):
            for c in reversed(range(totalColumns)):
                ul = (lr[0] - self.BOX_SIZE, lr[1] - self.BOX_SIZE)
                self.drawer.rectangle([ul, lr], fill=(255, 255, 255), outline=(0, 0, 0), width=self.BOX_LINE_WEIGHT)
                lr = (ul[0], lr[1])
            lr = (width - self.WIDTH_BUFFER, ul[1])
        self.grid_ul = ul
        self.__drawGrid_HeavyLines()

    def __drawRowLabels(self):
        ul = self.grid_ul
        ul = (ul[0]- self.BOX_SIZE, ul[1])
        lr = (ul[0] + self.BOX_SIZE, ul[1] + self.BOX_SIZE)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', round(.72*self.BOX_SIZE))
        for row in self.rowLabels:
            for rowLab in reversed(row):
                self.drawer.rectangle([ul, lr], fill=rowLab[0], outline=(0, 0, 0), width=self.BOX_LINE_WEIGHT)
                w, h = self.drawer.textsize(str(rowLab[1]), font=fnt)
                if sum(rowLab[0]) > 382:
                    textColor = (0, 0, 0)
                else:
                    textColor = (255, 255, 255)
                self.drawer.text((ul[0] + ((self.BOX_SIZE - w) / 2), ul[1] + ((self.BOX_SIZE - h) / 2)),
                                 str(rowLab[1]), font=fnt, fill=textColor, align="center")
                ul = (ul[0]-self.BOX_SIZE, ul[1])
                lr = (ul[0] + self.BOX_SIZE, ul[1] + self.BOX_SIZE)
            ul = (self.grid_ul[0]-self.BOX_SIZE, ul[1] + self.BOX_SIZE)
            lr = (ul[0] + self.BOX_SIZE, ul[1] + self.BOX_SIZE)

    def __drawColumnLabels(self):
        ul = self.grid_ul
        ul = (ul[0], ul[1]-self.BOX_SIZE)
        lr = (ul[0]+self.BOX_SIZE, ul[1]+self.BOX_SIZE)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', round(.72*self.BOX_SIZE))
        for column in self.columnLabels:
            for columnLab in reversed(column):
                self.drawer.rectangle([ul, lr], fill=columnLab[0], outline=(0,0,0), width=self.BOX_LINE_WEIGHT)
                w, h = self.drawer.textsize(str(columnLab[1]), font=fnt)
                if sum(columnLab[0]) > 382:
                    textColor = (0,0,0)
                else:
                    textColor = (255, 255, 255)
                self.drawer.text((ul[0]+((self.BOX_SIZE-w)/2), ul[1]+((self.BOX_SIZE-h)/2)), str(columnLab[1]), font = fnt, fill=textColor, align="center")
                ul = (ul[0], ul[1]-self.BOX_SIZE)
                lr = (ul[0]+self.BOX_SIZE, ul[1]+self.BOX_SIZE)
            ul = (ul[0]+self.BOX_SIZE, self.grid_ul[1]-self.BOX_SIZE)
            lr = (ul[0] + self.BOX_SIZE, ul[1] + self.BOX_SIZE)


    def __drawLabels(self, selftotalRows, totalColumns, maxRow, maxColumn):
        self.__drawRowLabels()
        self.__drawColumnLabels()

    def __getAllColors(self):
        allColors = set()
        allColors.add(self.defaultColor)
        for row in self.rowLabels:
            for lab in row:
                allColors.add(lab[0])
        for column in self.columnLabels:
            for lab in column:
                allColors.add(lab[0])
        return allColors

    def __getTextColor(self, color):
        if sum(color) > 382:
            return (0,0,0)
        else:
            return (255,255,255)

    def __drawColorKey(self, color, ul, lr, boxWidth, boxHeight, colorSet=None):
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', round(boxHeight*.75))
        textColor = self.__getTextColor(color)
        self.drawer.rectangle([ul, lr], fill=color, outline=textColor, width=self.BOX_LINE_WEIGHT)
        if colorSet:
            if color==self.defaultColor:
                colorName = "*" + colorSet.getColorName(color)
            else:
                colorName = colorSet.getColorName(color)
        else:
            if color==self.defaultColor:
                colorName = "*"
            else:
                colorName = ""
        w, h = self.drawer.textsize(colorName, font=fnt)
        while w >= boxWidth*.9:
            fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', fnt.size-5)
            w, h = self.drawer.textsize(colorName, font=fnt)
        self.drawer.text((ul[0] + ((boxWidth - w) /2), ul[1] + ((boxHeight - h) / 2)), colorName, font=fnt, fill=textColor, align="center")

    def __drawColorKeys(self, colorSet=None):
        width = self.grid_ul[0]-self.WIDTH_BUFFER-self.PUZZLE_BUFFER
        height = self.grid_ul[1]-self.HEIGHT_BUFFER-self.PUZZLE_BUFFER
        allColors = self.__getAllColors()
        boxHeight = floor(float(height)/float(len(allColors)))
        ul = (self.WIDTH_BUFFER, self.HEIGHT_BUFFER)
        lr = (ul[0]+width, ul[1]+boxHeight)
        for color in allColors:
            self.__drawColorKey(color, ul, lr, width, boxHeight, colorSet)
            ul = (ul[0], ul[1]+boxHeight)
            lr = (lr[0], lr[1]+boxHeight)

    def __drawPuzzle(self, pageSize, colorSet=None):
        emptyRows, emptyColumns, maxClueRows, maxClueColumns = self.__findGridDims()
        w, h = self.__getImageSize(emptyColumns+maxClueRows, emptyRows+maxClueColumns, pageSize)
        self.img = Image.new('RGB', (w,h), color=(255, 255, 255))
        print(self.img.size)
        self.__drawGrid(emptyRows, emptyColumns, maxClueRows, maxClueColumns)
        self.__drawLabels(emptyRows, emptyColumns, maxClueRows, maxClueColumns)
        self.__drawColorKeys(colorSet)

    #Uses a set of constants and parameters to form an image of the puzzle
    def generatePuzzle(self, rowLabels, columnLabels, defaultColor, pageSize, colorSet=None):
        self.WIDTH_BUFFER = 200
        self.HEIGHT_BUFFER = 200
        self.BOX_SIZE = 100
        self.PUZZLE_BUFFER = 100
        self.BOX_LINE_WEIGHT = 4
        self.rowLabels = rowLabels
        self.columnLabels = columnLabels
        self.defaultColor = defaultColor
        self.__drawPuzzle(pageSize, colorSet)
        self.img.show()
        return self.img