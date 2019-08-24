#Crayola rgb colors based on https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_Crayola_colored_pencil_colors.html

class ColorSet:
    def __init__(self):
        self.colors = {}

    def getColors(self):
        return self.colors.keys()

    def getColorName(self, color):
        if color in self.colors:
            return self.colors[color]
        else:
            return ""

class BW(ColorSet):
    def __init__(self):
        super().__init__()
        self.colors[(0,0,0)] = "black"
        self.colors[(255,255,255)] = "white"

class Greyscale(ColorSet):
    def __init__(self):
        super().__init__()
        self.colors[(0,0,0)] = "black"
        self.colors[(15,15,15)] = "practically black"
        self.colors[(30,30,30)] = "almost black"
        self.colors[(45,45,45)] = "extra dark"
        self.colors[(60,60,60)] = "super dark"
        self.colors[(75,75,75)] = "really dark"
        self.colors[(90,90,90)] = "dark grey"
        self.colors[(105,105,105)] = "pretty dark"
        self.colors[(120,120,120)] = "almost dark"
        self.colors[(130,130,130)] = "grey"
        self.colors[(145,145,145)] = "almost light"
        self.colors[(160,160,160)] = "pretty light"
        self.colors[(175,175,175)] = "light grey"
        self.colors[(190,190,190)] = "really light"
        self.colors[(205,205,205)] = "super light"
        self.colors[(220,220,220)] = "extra light"
        self.colors[(235,235,235)] = "almost white"
        self.colors[(245,245,245)] = "practically white"
        self.colors[(255,255,255)] = "white"

class Crayola12(ColorSet):
    def __init__(self):
        super().__init__()
        self.colors[(237, 10, 63)] = "red"
        self.colors[(255, 63, 52)] = "red_orange"
        self.colors[(255, 134, 31)] = "orange"
        self.colors[(251, 232, 112)] = "yellow"
        self.colors[(197, 225, 122)] = "yellow_green"
        self.colors[(1, 163, 104)] = "green"
        self.colors[(118, 215, 234)] = "sky_blue"
        self.colors[(0,102,255)] = "blue"
        self.colors[(131, 89, 163)] = "violet"
        self.colors[(255, 255, 255)] = "white"
        self.colors[(175, 89, 62)] = "brown"
        self.colors[(0,0,0)] = "black"

class Crayola24(Crayola12):
    def __init__(self):
        super().__init__()
        self.colors[(3, 187, 133)] = "aqua green"
        self.colors[(255, 223, 0)] = "golden yellow"
        self.colors[(139, 134, 128)] = "gray"
        self.colors[(10, 107, 13)] = "jade green"
        self.colors[(143, 216, 216)] = "light blue"
        self.colors[(246, 83, 166)] = "magenta"
        self.colors[(202, 52, 53)] = "mahogany"
        self.colors[(255, 203, 164)] = "peach"
        self.colors[(205, 145, 158)] = "pink"
        self.colors[(250, 157, 90)] = "tan"
        self.colors[(163, 111, 64)] = "light brown"
        self.colors[(255, 174, 66)] = "yellow orange"


class Crayola50(Crayola24):
    def __init__(self):
        super().__init__()

def Crayola120(Crayola50):
    def __init__(self):
        super().__init__()

class CrayolaTwist30(ColorSet):
    def __init__(self):
        super().__init__()
        self.colors[(237, 10, 63)] = "red"
        self.colors[(255, 63, 52)] = "red orange"
        self.colors[(255, 134, 31)] = "orange"
        self.colors[(242,138,3)] = "yellow orange"
        self.colors[(246, 167, 2)] = "mango"
        self.colors[(255, 223, 0)] = "golden yellow"
        self.colors[(251, 232, 112)] = "yellow"
        self.colors[(218, 223, 0)] = "green yellow"
        self.colors[(211, 224, 1)] = "lime green"
        self.colors[(137, 189, 1)] = "yellow green"
        self.colors[(1, 163, 104)] = "green"
        self.colors[(28, 106, 1)] = "asparagus"
        self.colors[(3, 187, 133)] = "aqua green"
        self.colors[(3, 134, 220)] = "blue"
        self.colors[(3, 128, 196)] = "cerulean"
        self.colors[(0,1,110)] = "blue violet"
        self.colors[(143, 0, 100)] = "orchid"
        self.colors[(98, 38, 149)] = "violet"
        self.colors[(133,0,0)] = "mahogany"
        self.colors[(48,0,0)] = "maroon"
        self.colors[(222,0, 96)] = "magenta"
        self.colors[(253, 175, 192)] = "carnation pink"
        self.colors[(231, 183, 220)] = "wisteria"
        self.colors[(226, 132, 2)] = "tan"
        self.colors[(193, 78, 4)] = "light brown"
        self.colors[(81, 13, 1)] = "brown"
        self.colors[(255, 218, 146)] = "apricot"
        self.colors[(255,255,255)] = "white"
        self.colors[(117, 120, 113)] = "grey"
        self.colors[(0,0,0)] = "black"