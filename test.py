import networkx as nx
import matplotlib.pyplot as plt


def backtrack(graph, current_solution, current_vertex, colors):
    if current_vertex is None:
        # Tous les sommets ont été colorés avec succès
        return True

    for color in colors:
        if is_safe(graph, current_vertex, color, current_solution):
            # Attribuer la couleur au sommet
            current_solution[current_vertex] = color

            # Affichage pour illustrer l'exécution
            print(f"Coloration de sommet {current_vertex} avec {color}")
            print("Solution actuelle:", current_solution)
            print()

            # Appel récursif pour le sommet suivant
            next_vertex = get_next_vertex(graph, current_solution)
            if backtrack(graph, current_solution, next_vertex, colors):
                return True  # Solution trouvée

            # Backtrack en annulant la couleur du sommet actuel
            current_solution[current_vertex] = None

    return False  # Aucune solution trouvée avec les choix actuels


def is_safe(graph, vertex, color, solution):
    for neighbor in graph[vertex]:
        if solution[neighbor] == color:
            return False
    return True


def get_next_vertex(graph, solution):
    for vertex in graph:
        if solution[vertex] is None:
            return vertex
    return None


# Graphe
monGraphe = {1: [2, 3], 2: [1, 3], 3: [1, 2]}

# Couleurs disponibles
colors = ["Red", "Green"]

# Solution initiale avec tous les sommets non colorés
initial_solution = {vertex: None for vertex in monGraphe}

# Appel de la fonction de backtracking
print(backtrack(monGraphe, initial_solution, next(iter(monGraphe)), colors))


# from enum import Enum


# class Color(Enum):
#     RED = "red"
#     BLUE = "blue"
#     GREEN = "green"
#     BLACK = "black"
#     PINK = "pink"
#     WHITE = "white"
#     OLIVE = "olive"
#     YELLOW = "yellow"
#     CYAN = "cyan"
#     MAGENTA = "magenta"
#     MINT = "mint"
#     PURPLE = "purple"
#     ORANGE = "orange"
#     LIME = "lime"
#     AQUA = "aqua"
#     NAVY = "navy"
#     CORAL = "coral"
#     TEAL = "teal"
#     MUSTARD = "mustard"
#     GREY = "grey"
#     BROWN = "brown"
#     INDIGO = "indigo"
#     AMBER = "amber"
#     PEACH = "peach"
#     MAROON = "maroon"


# # Récupérer la partie droite (valeurs) dans une liste
# valeurs_couleurs = [couleur.value for couleur in Color]


# # # # import pydot
# # # # from IPython.display import Image, display


# # # # def WelshPowell(G):
# # # #     # Color chart
# # # #     couleurs = ["blue", "green", "red", "brown", "gray", "pink"]
# # # #     Ma = MAdjacence(G, genre)
# # # #     sommets = Sommets(G)
# # # #     degres, result = [], []
# # # #     nb = 0
# # # #     for sommet in sommets:
# # # #         degres.append(len(Voisinage(G, sommet)))
# # # #         result.append(0)
# # # #     degres.sort()
# # # #     for i in range(len(degres)):
# # # #         if result[i] == 0:
# # # #             nb += 1
# # # #             result[i] = couleurs[nb]
# # # #             for j in range(len(degres)):
# # # #                 if Ma[i][j] == 0 and result[j] == 0:
# # # #                     for k in range(len(degres)):
# # # #                         passe = 0
# # # #                         if Ma[j][k] == 1 and result[k] == result[i]:
# # # #                             passe = 1
# # # #                             break
# # # #                     if passe == 0:
# # # #                         result[j] = result[i]
# # # #     d, i = {}, 0
# # # #     for sommet in sommets:
# # # #         d[sommet] = result[i]
# # # #         i += 1
# # # #     # Graphical representation of our graph after applying the algorithm
# # # #     graph = pydot.Dot(graph_type="graph")
# # # #     for i in sommets:
# # # #         node = pydot.Node(i, style="filled", fillcolor=d[i])
# # # #         graph.add_node(node)
# # # #     for i in G:
# # # #         for j in G[i]:
# # # #             arc = pydot.Edge(i, j)
# # # #             graph.add_edge(arc)
# # # #     img = Image(graph.create_png())
# # # #     display(img)


# # # # WelshPowell(G)

# # # import numpy as np
# # # import networkx as nx
# # # import matplotlib.pyplot as plt

# # # # Matrice d'adjacence
# # # M = np.array(
# # #     [
# # #         [0, 1, 1, 1, 0],
# # #         [1, 0, 1, 0, 0],
# # #         [1, 1, 0, 1, 1],
# # #         [1, 0, 1, 0, 1],
# # #         [0, 0, 1, 1, 0],
# # #     ]
# # # )

# # # # Création du graphe à partir de la matrice
# # # G = nx.from_numpy_array(M)

# # # # Dessiner le graphe
# # # pos = nx.spring_layout(G)  # disposition des nœuds
# # # nx.draw(
# # #     G,
# # #     pos,
# # #     with_labels=True,
# # #     font_weight="bold",
# # #     node_size=700,
# # #     node_color="skyblue",
# # #     font_color="black",
# # #     font_size=8,
# # #     font_family="Arial",
# # # )

# # # # Afficher le graphe
# # # plt.show()


# # import networkx as nx
# # import matplotlib.pyplot as plt

# # G = nx.path_graph(10)
# # node_colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # Sans spécifier cmap
# # pos = nx.spring_layout(G)
# # nx.draw(
# #     G,
# #     pos,
# #     with_labels=True,
# #     node_color=node_colors,
# #     font_color="white",
# #     font_size=8,
# #     font_family="Arial",
# # )
# # plt.title("Sans spécifier cmap")

# # plt.show()

# # # En spécifiant cmap
# # pos = nx.spring_layout(G)
# # nx.draw(
# #     G,
# #     pos,
# #     with_labels=True,
# #     node_color=node_colors,
# #     cmap=plt.cm.Blues,
# #     font_color="white",
# #     font_size=8,
# #     font_family="Arial",
# # )
# # plt.title("En spécifiant cmap")
# # plt.show()
