from enum import Enum


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    CYAN = "cyan"
    MAGENTA = "magenta"
    YELLOW = "yellow"
    BLACK = "black"
    WHITE = "white"
    ORANGE = "orange"
    PURPLE = "purple"
    GRAY = "gray"
    BROWN = "brown"
    PINK = "pink"
    OLIVE = "olive"
    LIME = "lime"


pallete_couleurs = [couleur.value for couleur in Color]
