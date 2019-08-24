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
        self.colors[(243, 42, 58)] = "red"
        self.colors[(240, 60, 37)] = "red orange"
        self.colors[(231, 122, 57)] = "orange"
        self.colors[(252, 235, 67)] = "yellow"
        self.colors[(109, 197, 87)] = "yellow green"
        self.colors[(42, 164, 91)] = "green"
        self.colors[(17, 171, 221)] = "sky blue"
        self.colors[(0, 88, 173)] = "blue"
        self.colors[(96, 62, 157)] = "violet"
        self.colors[(255, 255, 255)] = "white"
        self.colors[(143, 93, 56)] = "brown"
        self.colors[(0,0,0)] = "black"

class Crayola24(Crayola12):
    def __init__(self):
        super().__init__()
        self.colors[(245, 158, 45)] = "yellow orange"
        self.colors[(255, 223, 0)] = "golden yellow"
        self.colors[(132, 177, 122)] = "jade green"
        self.colors[(69, 188, 166)] = "aqua green"
        self.colors[(107, 137, 199)] = "light blue"
        self.colors[(238, 168, 202)] = "pink"
        self.colors[(207, 36, 150)] = "magenta"
        self.colors[(241, 199, 139)] = "peach"
        self.colors[(180, 111, 72)] = "light brown"
        self.colors[(147, 53, 41)] = "mahogany"
        self.colors[(219, 164, 100)] = "tan"
        self.colors[(147, 147, 147)] = "gray"

class Crayola50(Crayola24):
    def __init__(self):
        super().__init__()
        self.colors[(196, 34, 92)] = "raspberry"
        self.colors[(155, 36, 74)] = "maroon"
        self.colors[(240, 176, 105)] = "light orange"
        self.colors[(244, 186, 50)] = "mango"
        self.colors[(240, 237, 84)] = "lemon yellow"
        self.colors[(158, 206, 97)] = "lime green"
        self.colors[(53, 133, 108)] = "pine green"
        self.colors[(63, 149, 150)] = "teal"
        self.colors[(37, 117, 126)] = "green blue"
        self.colors[(86, 190, 199)] = "turquoise"
        self.colors[(17, 171, 221)] = "sky blue"
        self.colors[(20, 134, 194)] = "cerulean"
        self.colors[(32, 49, 105)] = "navy blue"
        self.colors[(189, 100, 166)] = "orchid"
        self.colors[(170, 122, 134)] = "mauve"
        self.colors[(186, 157, 162)] = "pale rose"
        self.colors[(250, 162, 186)] = "bubblegum"
        self.colors[(241, 178, 171)] = "salmon"
        self.colors[(95, 80, 59)] = "dark brown"
        self.colors[(198, 169, 137)] = "taupe"
        self.colors[(228, 205, 164)] = "sand"
        self.colors[(226, 172, 84)] = "harvest gold"
        self.colors[(180, 156, 68)] = "bronze yellow"
        self.colors[(120, 140, 129)] = "cool gray"
        self.colors[(120, 134, 147)] = "slate"

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