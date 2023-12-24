import networkx as nx
import matplotlib.pyplot as plt
import color


palette_couleur = color.valeurs_couleurs

monGraphe = {
    1: [2, 3, 4],
    2: [1, 3],
    3: [1, 2, 4, 5],
    4: [1, 3, 5],
    5: [3, 4],
}


def gloutton(graphe):
    vertex_list = list(graphe.keys())
    colored = {}
    while vertex_list:
        vertex = vertex_list.pop(0)
        couleurs_voisins = {
            colored[voisin] for voisin in graphe[vertex] if voisin in colored
        }

        index_couleurs = [palette_couleur.index(c) for c in couleurs_voisins]

        # Trouver l'indice minimum non utilisé
        indice_couleur = 0
        while indice_couleur in index_couleurs:
            indice_couleur += 1

        colored[vertex] = palette_couleur[indice_couleur]

    return colored


resultats_gloutton = gloutton(monGraphe)

G = nx.from_dict_of_lists(monGraphe)

# Récupération des couleurs attribuées par la fonction gloutton
couleurs_noeuds = [resultats_gloutton[n] for n in G.nodes]

pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=couleurs_noeuds,
    font_color="white",
    font_size=10,
    font_family="Arial",
)

# Affichage
plt.show()
