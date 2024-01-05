import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox


monGraphe = {}
pallete_couleurs = [
    "red",
    "blue",
    "green",
    "black",
    "grey",
    "orange",
    "purple",
    "yellow",
    "pink",
]


def isSafeToColor(graphe, vertex, color, sol):
    for v in graphe[vertex]:
        if sol[v] == color:
            return False
    return True


def getNextVertex(g, sol):
    for v in g:
        if sol[v] is None:
            return v
    return None


def backtrack(graphe, vertex, colors, solution):
    if vertex is None:
        return True

    # print(f"Coloration de sommet {vertex} avec les couleurs disponibles : {colors} \n")
    for col in colors:
        if isSafeToColor(graphe, vertex, col, solution):
            solution[vertex] = col

            next_vertex = getNextVertex(graphe, solution)
            # print(
            #     f"   Essai de couleur {col} pour le sommet {vertex}. Solution actuelle : {solution}\n"
            # )
            if backtrack(graphe, next_vertex, colors, solution):
                return True

            solution[
                vertex
            ] = None  # Revenir en arrière (backtrack) en annulant la couleur
    #         print(
    #             f"   Retour en arrière. Annulation de la couleur pour le sommet {vertex}. Solution actuelle : {solution}\n"
    #         )

    # print(f"Aucune couleur n'est valide pour le sommet {vertex}.\n")
    return False


first_vertex = list(monGraphe.keys())[0]
vertex_color = {v: None for v in monGraphe}


def getSol():
    if backtrack(monGraphe, first_vertex, pallete_couleurs, vertex_color):
        return vertex_color
    return None


sol_from_backtrack = getSol()
print(sol_from_backtrack)
# # -----------------------------------------affichage-------------------------------------


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

    # Affichage
    plt.show()


# Dessiner le graphe coloré
if sol_from_backtrack is None:
    messagebox.showerror(
        "Erreur", "Aucune solution trouvée. Le graphe ne peut pas être coloré."
    )
else:
    draw_colored_graph(monGraphe, sol_from_backtrack)
