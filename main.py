import ImageAdjuster
import Displayer
import Colors


if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    adjuster = ImageAdjuster.ImageAdjuster()
    colorSet = Colors.Crayola120()
    img = adjuster.adjustImage(FILENAME, maxSize=20, clusterCount=7, iterations=5, colorSet=colorSet)
    img.show()
    displayer = Displayer.Displayer(img)
    puzzle = displayer.generatePuzzle(pageSize=(8.5, 11), level=1, colorSet=colorSet)
