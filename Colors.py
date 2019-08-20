#Crayola rgb colors based on https://ipfs.io/ipfs/QmXoypizjW3WknFiJnKLwHCnL72vedxjQkDDP1mXWo6uco/wiki/List_of_Crayola_colored_pencil_colors.html

class ColorSet:
    def __init__(self):
        self.colors = {}

    def getColors(self):
        return self.colors.keys()

class Crayola12(ColorSet):
    def __init__(self):
        super().__init__()
        self.colors = {}
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
        self.colors[(3, 187, 133)] = "aqua_green"
        self.colors[(255, 223, 0)] = "golden_yellow"
        self.colors[(139, 134, 128)] = "gray"
        self.colors[(10, 107, 13)] = "jade_green"
        self.colors[(143, 216, 216)] = "light_blue"
        self.colors[(246, 83, 166)] = "magenta"
        self.colors[(202, 52, 53)] = "mahogany"
        self.colors[(255, 203, 164)] = "peach"
        self.colors[(205, 145, 158)] = "pink"
        self.colors[(250, 157, 90)] = "tan"
        self.colors[(163, 111, 64)] = "light_brown"
        self.colors[(255, 174, 66)] = "yellow_orange"

class Crayola36(Crayola24):
    def __init__(self):
        super().__init__()

class Crayola50(Crayola36):
    def __init__(self):
        super().__init__()

def Crayola100(Crayola50):
    def __init__(self):
        super().__init__()