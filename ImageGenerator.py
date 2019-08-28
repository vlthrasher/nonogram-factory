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

    def __drawGrid(self, totalRows, totalColumns, maxRow, maxColumn):
        width = self.img.size[0]
        height = self.img.size[1]
        self.drawer = ImageDraw.Draw(self.img)
        lr = (width - self.WIDTH_BUFFER, height - self.HEIGHT_BUFFER)
        for r in range(totalRows):
            for c in reversed(range(totalColumns)):
                ul = (lr[0] - self.BOX_SIZE, lr[1] - self.BOX_SIZE)
                self.drawer.rectangle([ul, lr], fill=(255, 255, 255), outline=(0, 0, 0), width=3)
                lr = (ul[0], lr[1])
            lr = (width - self.WIDTH_BUFFER, ul[1])
        self.grid_ul = ul

    def __drawRowLabels(self):
        #TODO: Add bolded lines every 5 boxes for separation
        ul = self.grid_ul
        ul = (ul[0]- self.BOX_SIZE, ul[1])
        lr = (ul[0] + self.BOX_SIZE, ul[1] + self.BOX_SIZE)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', round(.72*self.BOX_SIZE))
        for row in self.rowLabels:
            for rowLab in reversed(row):
                self.drawer.rectangle([ul, lr], fill=rowLab[0], outline=(0, 0, 0), width=3)
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
        #TODO: Add bolded lines every 5 boxes for separation
        ul = self.grid_ul
        ul = (ul[0], ul[1]-self.BOX_SIZE)
        lr = (ul[0]+self.BOX_SIZE, ul[1]+self.BOX_SIZE)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', round(.72*self.BOX_SIZE))
        for column in self.columnLabels:
            for columnLab in reversed(column):
                self.drawer.rectangle([ul, lr], fill=columnLab[0], outline=(0,0,0), width=3)
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

    def __drawColorKey(self, colorSet=None):
        width = self.grid_ul[0]-self.WIDTH_BUFFER-self.PUZZLE_BUFFER
        height = self.grid_ul[1]-self.HEIGHT_BUFFER-self.PUZZLE_BUFFER
        allColors = self.__getAllColors()
        boxHeight = floor(float(height)/float(len(allColors)))
        ul = (self.WIDTH_BUFFER, self.HEIGHT_BUFFER)
        lr = (ul[0]+width, ul[1]+boxHeight)
        fnt = ImageFont.truetype('/Library/Fonts/Arial.ttf', boxHeight-5)
        for color in allColors:
            self.drawer.rectangle([ul, lr], fill=color, outline=(255,255,255), width=3)
            if sum(color) > 382:
                textColor = (0, 0, 0)
            else:
                textColor = (255, 255, 255)
            # TODO: change font size if the color name is too long
            if colorSet:
                if color == self.defaultColor:
                    w, h = self.drawer.textsize("*"+colorSet.getColorName(color), font=fnt)
                    self.drawer.text((ul[0] + ((width - w) / 2), ul[1] + ((boxHeight - h) / 2)),
                                     "*"+colorSet.getColorName(color), font=fnt, fill=textColor, align="center")
                else:
                    w, h = self.drawer.textsize(colorSet.getColorName(color), font=fnt)
                    self.drawer.text((ul[0] + ((width - w) / 2), ul[1] + ((boxHeight - h) / 2)),
                                     colorSet.getColorName(color), font=fnt, fill=textColor, align="center")
            else:
                if color == self.defaultColor:
                    w, h = self.drawer.textsize("*", font=fnt)
                    self.drawer.text((ul[0] + ((width - w) / 2), ul[1] + ((boxHeight - h) / 2)), "*",
                                     font=fnt, fill=textColor, align="center")
            ul = (ul[0], ul[1]+boxHeight)
            lr = (lr[0], lr[1]+boxHeight)

    def __drawPuzzle(self, pageSize, colorSet=None):
        emptyRows, emptyColumns, maxClueRows, maxClueColumns = self.__findGridDims()
        print(maxClueRows, maxClueColumns)
        w, h = self.__getImageSize(emptyColumns+maxClueRows, emptyRows+maxClueColumns, pageSize)
        self.img = Image.new('RGB', (w,h), color=(255, 255, 255))
        print(self.img.size)
        self.__drawGrid(emptyRows, emptyColumns, maxClueRows, maxClueColumns)
        self.__drawLabels(emptyRows, emptyColumns, maxClueRows, maxClueColumns)
        self.__drawColorKey(colorSet)

    def generatePuzzle(self, rowLabels, columnLabels, defaultColor, pageSize, colorSet=None):
        self.WIDTH_BUFFER = 200
        self.HEIGHT_BUFFER = 200
        self.BOX_SIZE = 100
        self.PUZZLE_BUFFER = 100
        self.rowLabels = rowLabels
        self.columnLabels = columnLabels
        self.defaultColor = defaultColor
        self.__drawPuzzle(pageSize, colorSet)


        """
        d.line([(500, 300), (500, 900)], fill=(0, 0, 0), width=3)
        d.rectangle([(100, 100), (150, 150)], fill=(255, 0, 0), outline=(0, 0, 0), width=3)
        """
        self.img.show()
        return self.img