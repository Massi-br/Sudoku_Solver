import numpy as np
import time


# colors_dict = {
#     1: "red",
#     2: "blue",
#     3: "green",
#     4: "purple",
#     5: "orange",
#     6: "brown",
#     7: "pink",
#     8: "cyan",
#     9: "gray",
# }
# # Exemple d'utilisation
# for number, color in colors_dict.items():
#     print(f"Number {number} is associated with the color {color}")


# grid = [
#     [0, 0, 8, 0, 2, 0, 0, 0, 9],
#     [0, 0, 7, 0, 0, 0, 4, 0, 2],
#     [2, 0, 0, 7, 9, 0, 0, 1, 0],
#     [0, 0, 9, 0, 0, 5, 3, 0, 6],
#     [0, 6, 0, 0, 4, 0, 8, 9, 0],
#     [7, 0, 4, 9, 0, 0, 1, 0, 0],
#     [0, 7, 0, 0, 3, 6, 0, 0, 1],
#     [5, 0, 3, 0, 0, 0, 7, 0, 0],
#     [6, 0, 0, 0, 5, 0, 2, 8, 0],
# ]


# def est_possible(grille, ligne, colonne, valeur):
#     # test de la ligne
#     for i in range(9):
#         if grille[ligne][i] == valeur:
#             return False
#     # test de la colonne
#     for i in range(9):
#         if grille[i][colonne] == valeur:
#             return False
#     # test du bloc
#     # la case en haut à gauche de bloc a pour coordonnées
#     # (3 * (ligne // 3), 3 * (colonne // 3))
#     for i in range(3 * (ligne // 3), 3 * (ligne // 3) + 3):
#         for j in range(3 * (colonne // 3), 3 * (colonne // 3) + 3):
#             if grille[i][j] == valeur:
#                 return False
#     return True


# def est_possible(grille, ligne, colonne, valeur):
#     # test de la ligne
#     for i in range(4):
#         if grille[ligne][i] == valeur:
#             return False
#     # test de la colonne
#     for i in range(4):
#         if grille[i][colonne] == valeur:
#             return False
#         # test du bloc
#     bloc_ligne = 2 * (ligne // 2)
#     bloc_colonne = 2 * (colonne // 2)
#     for i in range(bloc_ligne, bloc_ligne + 2):
#         for j in range(bloc_colonne, bloc_colonne + 2):
#             if grille[i][j] == valeur:
#                 return False
#     return True


def assign_indices():
    indices = {}
    count = 0
    for x in range(4):
        for y in range(4):
            indices[(x, y)] = count
            count += 1
    return indices


def graph_from_grid():
    graph = {}

    # Ajouter tous les sommets au graphe et bien les indicés
    indices = assign_indices()

    # Ajouter les voisins pour chaque sommet en respectant les règles du Sudoku
    for x in range(4):
        for y in range(4):
            neighbors = set()

            # Ajouter les voisins de la même ligne
            for i in range(4):
                if i != y:
                    neighbors.add(indices[(x, i)])

            # Ajouter les voisins de la même colonne
            for j in range(4):
                if j != x:
                    neighbors.add(indices[(j, y)])

            # Ajouter les voisins du même carré (2x2)
            square_start_x = 2 * (x // 2)
            square_start_y = 2 * (y // 2)
            for i in range(square_start_x, square_start_x + 2):
                for j in range(square_start_y, square_start_y + 2):
                    if i != x and j != y:
                        neighbors.add(indices[(i, j)])

            # Mettre à jour le graphe avec les voisins du sommet actuel
            graph[indices[(x, y)]] = list(neighbors)

    return graph


# Exemple d'utilisation
grille = [[3, 0, 0, 0], [0, 1, 3, 0], [0, 4, 2, 0], [0, 0, 0, 4]]
monGraphe = graph_from_grid()

# Affichage du graphe
for sommet, voisins in monGraphe.items():
    print(f"{sommet} : {voisins}")


# def solver(grille):
#     for x in range(4):
#         for y in range(4):
#             if grille[x][y] == 0:
#                 for n in range(1, 5):
#                     if est_possible(grille, x, y, n):
#                         grille[x][y] = n
#                         if solver(grille):
#                             return True
#                         grille[x][y] = 0
#                 return False
#     print(np.matrix(grille))
#     return True


# g = [[3, 0, 0, 0], [0, 1, 3, 0], [0, 4, 2, 0], [0, 0, 0, 4]]


# solver(grid)


# start_time = time.time()
# sudoku_grid = generate_sudoku()
# generation_time = time.time() - start_time


# print("Solving Time: %.6f seconds" % generation_time)
