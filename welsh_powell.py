import networkx as nx
import matplotlib.pyplot as plt
import color

# -----------------------------------DECLARATION----------------------------------#
pallete_couleurs = color.valeurs_couleurs

# Exemple d'utilisation
monGraphe = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [1, 3, 5],
    5: [3, 4],
}

# -----------------------------------FONCTIONS UTILITARES----------------------------------#


def degre(graphe, sommet):
    """
    Calcule le degré d'un sommet dans un graphe représenté par un dictionnaire.

    Parameters:
    - graphe (dict): Dictionnaire représentant le graphe.
    - sommet (int): Le sommet pour lequel on veut calculer le degré.

    Returns:
    - int: Le degré du sommet.
    """
    return len(graphe[sommet])


def trier_sommets_par_degre(graphe):
    """
    Trie les sommets d'un graphe par degré décroissant.

    Parameters:
    - graphe (dict): Dictionnaire représentant le graphe.

    Returns:
    - list: Liste des sommets triés par degré décroissant.
    """
    sommets = list(graphe.keys())
    sorted_sommets = sorted(sommets, key=lambda x: degre(graphe, x), reverse=True)
    return sorted_sommets


# -----------------------------------FONCTION DE BASE (WELSH_POWELL)-----------------------------#


def welsh_powell(graphe):
    sommets_tries = trier_sommets_par_degre(graphe)
    couleur_sommets = (
        {}
    )  # Dictionnaire pour stocker les couleurs attribuées à chaque sommet

    while sommets_tries:
        sommet = sommets_tries.pop(
            0
        )  # Prendre le sommet de plus haut degré non encore colorié
        voisins_couleurs = {
            couleur_sommets[voisin]
            for voisin in graphe[sommet]
            if voisin in couleur_sommets
        }

        # Trouver la première couleur disponible pour le sommet
        nouvelle_couleur = next(
            c for c in pallete_couleurs if c not in voisins_couleurs
        )

        couleur_sommets[sommet] = nouvelle_couleur

    return couleur_sommets


# -----------------------------------APPEL A LA FONCTION ----------------------------------------#

couleur_sommets = welsh_powell(monGraphe)

# -----------------------------------CREATION ET AFFICHAGE DU GRAPHE------------------------------------------#


def draw_colored_graph(graph, colors):
    G = nx.from_dict_of_lists(graph)
    # Dessiner le graphe avec les couleurs attribuées
    pos = nx.spring_layout(G)
    node_colors = [colors[sommet] for sommet in G.nodes]
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        font_color="white",
        font_size=10,
        font_family="Arial",
    )
    plt.show()


# draw_colored_graph(monGraphe, couleur_sommets)
