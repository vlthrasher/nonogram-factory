# nonogram-factory
A project that takes an image and returns a nonogram representation for that image.

**_Still requires clean-up and optimization_**

Expects users to print the resulting puzzle to solve
### Modules:

* main.py: main module that calls all the other modules and puts it all together.
    * Colors.py: a series of classes that represent collections of discrete colors.
    * ImageAdjuster.py: wrapper class for ColorClusterer the reduces the size of the image and recolors it to the clustered colors
        * ColorClusterer.py: dependent class of the ImageAdjuster class that clusters colors from an image to the colorset(if given)
    * Displayer.py: wrapper class for ImageGenerator that finds the default color and labels before generating an image
        * ImageGenerator.py: dependent class of the Displayer class that actually generates the final puzzle's image

### main.py User Input:
* colorSet: which set of colors from Colors.py to use
* fileName: the path to the image to make into a puzzle
* maxSize: the maximum dimension in the final puzzle
* clusterCount: how many different colors should be in the puzzle
* iterations: how many iterations to do k-means clustering for
* pageSize: the page dimensions on which the puzzle will be printed out
* level: how hard the puzzle is (which color is the default color)- 1 is the easiest, 5 is the hardest