import ImageAdjuster


if __name__ == "__main__":
    FILENAME = "./Images/silks.jpg"
    adjuster = ImageAdjuster.ImageAdjuster()
    img = adjuster.adjustImage(FILENAME)
    img.show()