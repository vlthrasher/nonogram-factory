import ImageAdjuster
import Displayer
import Colors


if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    adjuster = ImageAdjuster.ImageAdjuster()
    colorSet = Colors.CrayolaTwist30()
    img = adjuster.adjustImage(FILENAME, maxSize=20, clusterCount=5, iterations=5, colorSet=colorSet)
    img.show()
    displayer = Displayer.Displayer(img)
    displayer.generatePuzzle(colorSet)
