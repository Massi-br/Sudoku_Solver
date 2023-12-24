from enum import Enum


class Color(Enum):
    RED = "red"
    BLUE = "blue"
    GREEN = "green"
    BLACK = "black"
    BROWN = "brown"
    MAGENTA = "magenta"
    OLIVE = "olive"
    YELLOW = "yellow"
    CYAN = "cyan"
    MINT = "mint"
    PURPLE = "purple"
    ORANGE = "orange"
    LIME = "lime"
    AQUA = "aqua"
    NAVY = "navy"
    CORAL = "coral"
    TEAL = "teal"
    MUSTARD = "mustard"
    GREY = "grey"
    INDIGO = "indigo"
    AMBER = "amber"
    PEACH = "peach"
    MAROON = "maroon"


# Récupérer la partie droite (valeurs) dans une liste
valeurs_couleurs = [couleur.value for couleur in Color]
