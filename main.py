import ImageAdjuster
import Displayer
import Colors

# TODO: Add Crayola Colored Pencil Color Analysis

if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    adjuster = ImageAdjuster.ImageAdjuster()
    img = adjuster.adjustImage(FILENAME, maxSize=20, clusterCount=5, iterations=5, colorSet=Colors.Crayola12())
    img.show()
    displayer = Displayer.Displayer(img)
    displayer.generatePuzzle()
