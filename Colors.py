#Crayola rgb colors based on images from each pack on the Crayola.com website

#parent class all other colorsets inherit from
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

class Crayola120(Crayola50):
    def __init__(self):
        super().__init__()
        self.colors[(190, 55, 89)] = "brick red"
        self.colors[(244, 119, 94)] = "lobster red"
        self.colors[(248, 185, 192)] = "melon"
        self.colors[(250, 169, 47)] = "orange circuit"
        self.colors[(247, 197, 87)] = "sun yellow"
        self.colors[(247, 204, 153)] = "heat wave"
        self.colors[(250, 223, 202)] = "atomic tangerine"
        self.colors[(251, 225, 221)] = "sizzling sunset"
        self.colors[(249, 208, 208)] = "outrageous orange"
        self.colors[(240, 238, 181)] = "daffodil"
        self.colors[(244, 240, 197)] = "unmellow yellow"
        self.colors[(243, 241, 175)] = "lemon glacier"
        self.colors[(224, 236, 184)] = "palm leaf"
        self.colors[(227, 240, 218)] = "arctic lime"
        self.colors[(217, 236, 187)] = "spring frost"
        self.colors[(209, 233, 177)] = "screamin\' green"
        self.colors[(207, 232, 170)] = "granny smith apple"
        self.colors[(188, 222, 132)] = "fern"

        self.colors[(139, 195, 139)] = "forest green"
        self.colors[(165, 154, 55)] = "olive"
        self.colors[(168, 220, 173)] = "shamrock"
        self.colors[(135, 227, 203)] = "sea green"
        self.colors[(100, 199, 175)] = "tropical rainforest"
        self.colors[(199, 238, 251)] = "absolute zero"
        self.colors[(170, 206, 243)] = "blue bell"
        self.colors[(204, 225, 242)] = "cornflower"
        self.colors[(226, 233, 243)] = "wild blue yonder"
        self.colors[(195, 207, 235)] = "manatee"
        self.colors[(66, 86, 133)] = "midnight blue"
        self.colors[(75, 66, 112)] = "outer space"
        self.colors[(88, 112, 185)] = "pacific blue"
        self.colors[(117, 174, 224)] = "blue bolt"
        self.colors[(72, 149, 236)] = "true blue"
        self.colors[(84, 126, 213)] = "bluetiful"
        self.colors[(87, 92, 188)] = "indigo"
        self.colors[(79, 74, 170)] = "dark blue"

        self.colors[(179, 144, 225)] = "purple mountain majesty"
        self.colors[(213, 205, 241)] = "purple heart"
        self.colors[(213, 191, 231)] = "periwinkle"
        self.colors[(180, 144, 222)] = "ultra violet"
        self.colors[(167, 131, 217)] = "blue violet"
        self.colors[(181, 127, 210)] = "royal purple"
        self.colors[(124, 79, 162)] = "plum"
        self.colors[(215, 192, 231)] = "lilac"
        self.colors[(236, 205, 228)] = "mauvelous"
        self.colors[(231, 150, 193)] = "dark mauve"
        self.colors[(221, 24, 175)] = "red violet"
        self.colors[(248, 105, 210)] = "jazzberry jam"
        self.colors[(250, 107, 160)] = "ruby red"
        self.colors[(246, 148, 169)] = "parrot pink"
        self.colors[(249, 201, 215)] = "fiery rose"
        self.colors[(251, 186, 222)] = "winter sky"
        self.colors[(249, 125, 196)] = "pink flamingo"
        self.colors[(252, 205, 235)] = "razzle dazzle rose"
        self.colors[(250, 226, 243)] = "blush"
        self.colors[(250, 182, 227)] = "tickle me pink"
        self.colors[(252, 190, 205)] = "fuzzy wuzzy"
        self.colors[(247, 244, 240)] = "almond"
        self.colors[(247, 231, 218)] = "apricot"

        self.colors[(249, 216, 185)] = "khaki"
        self.colors[(254, 207, 193)] = "cantaloupe"
        self.colors[(247, 188, 170)] = "coral reef"
        self.colors[(246, 171, 132)] = "burnt sienna"
        self.colors[(245, 192, 171)] = "copper"
        self.colors[(217, 165, 147)] = "antique brass"
        self.colors[(188, 113, 101)] = "cocoa"
        self.colors[(182, 124, 102)] = "dark chocolate"
        self.colors[(142, 100, 78)] = "beaver"
        self.colors[(153, 142, 143)] = "ash"
        self.colors[(202, 186, 179)] = "warm gray"
        self.colors[(224, 222, 223)] = "timberwolf"

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