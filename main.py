import ImageAdjuster
import Displayer
import Colors

# TODO: Add Crayola Colored Pencil Color Analysis

if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    adjuster = ImageAdjuster.ImageAdjuster()
    colorSet = Colors.Crayola24()
    img = adjuster.adjustImage(FILENAME, maxSize=20, clusterCount=7, iterations=5, colorSet=colorSet)
    img.show()
    displayer = Displayer.Displayer(img)
    displayer.generatePuzzle(colorSet)
