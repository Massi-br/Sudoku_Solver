import backtrack as bkt
from display import draw_colored_graph
from tkinter import messagebox
from sudokuGUI import afficher_interface_graphique, assign_indices

# -----------------------------------------------------DECLARATION--------------------------------------------#
# Exemple d'utilisation
# grille = [
#     [5, 3, 0, 0, 7, 0, 0, 0, 0],
#     [6, 0, 0, 1, 9, 5, 0, 0, 0],
#     [0, 9, 8, 0, 0, 0, 0, 6, 0],
#     [8, 0, 0, 0, 6, 0, 0, 0, 3],
#     [4, 0, 0, 8, 0, 3, 0, 0, 1],
#     [7, 0, 0, 0, 2, 0, 0, 0, 6],
#     [0, 6, 0, 0, 0, 0, 2, 8, 0],
#     [0, 0, 0, 4, 1, 9, 0, 0, 5],
#     [0, 0, 0, 0, 8, 0, 0, 7, 9],
# ]

grille = []
colors_dict = {
    1: "red",
    2: "blue",
    3: "green",
    4: "black",
    5: "grey",
    6: "orange",
    7: "purple",
    8: "yellow",
    9: "pink",
}

# ----------------------------------------FONCTIONS QUI INITIALISE UN SUDOKU CORRECT---------------------------#


def est_valide(grille, num, ligne, colonne):
    # Vérifier la validité du chiffre num à la position donnée
    # dans la ligne, colonne et le carré 3x3 correspondant.
    # Retourne True si le chiffre est valide, False sinon.

    # Vérifier la ligne
    if num in grille[ligne]:
        return False

    # Vérifier la colonne
    if num in [grille[i][colonne] for i in range(9)]:
        return False

    # Vérifier le carré 3x3
    carre_ligne, carre_colonne = ligne // 3 * 3, colonne // 3 * 3
    for i in range(carre_ligne, carre_ligne + 3):
        for j in range(carre_colonne, carre_colonne + 3):
            if grille[i][j] == num:
                return False

    return True


def initGrille():
    """
    Cette fonction demande à l'utilisateur d'entrer les chiffres pour compléter la grille Sudoku.
    La grille est une liste bidimensionnelle de 9x9. L'utilisateur est invité à entrer les valeurs
    pour chaque case en spécifiant les coordonnées de la case (ligne, colonne). La valeur 0 est utilisée
    pour indiquer une case vide.
    Returns:
    - grille: Une grille 9x9 remplie avec les chiffres entrés par l'utilisateur.
    """
    print("Entrez les chiffres pour compléter la grille (0 pour les cases vides):")
    grille = [[0] * 9 for _ in range(9)]

    for i in range(9):
        for j in range(9):
            while True:
                try:
                    valeur = int(
                        input(f"Entrez la valeur pour la case ({i+1}, {j+1}): ")
                    )
                    if valeur == 0:
                        grille[i][j] = valeur
                        break
                    else:
                        if (0 < valeur <= 9) and est_valide(grille, valeur, i, j):
                            grille[i][j] = valeur
                            break
                        else:
                            print("Veuillez entrer une valeur valide pour cette case.")
                except ValueError:
                    print("Veuillez entrer un chiffre valide.")
    return grille


# ---------------------------------------------FONCTION UTILITARE-------------------------------------------#


def inverse_dict(d):
    """
    Inverse les clés et les valeurs d'un dictionnaire.

    cette fonction est utilisée pour inverser le dictionnaire colors_dict.
    Colors_dict a les chiffres de 1 à 9 comme clés et les noms des couleurs comme valeurs.
    L'appel à inverse_dict(colors_dict) crée un nouveau dictionnaire (colors_inv)
    où les clés sont les noms des couleurs et les valeurs sont les chiffres associés.
    Cela est utilisé plus tard dans la fonction sol_final pour convertir les couleurs de la solution
    de leur représentation dans le graphe (colors_dict) à leur représentation initiale (colors_inv).
    """
    return {v: k for k, v in d.items()}


# --------------------------------------------FONCTIONS DE BASE----------------------------------------------#
def graph_from_grid():
    graph = {}
    # Ajouter tous les sommets au graphe et bien les indicés
    indices = assign_indices()
    # Ajouter les voisins pour chaque sommet en respectant les règles du Sudoku
    for x in range(9):
        for y in range(9):
            neighbors = set()
            # Ajouter les voisins de la même ligne
            for i in range(9):
                if i != y:
                    neighbors.add(indices[(x, i)])
            # Ajouter les voisins de la même colonne
            for j in range(9):
                if j != x:
                    neighbors.add(indices[(j, y)])
            # Ajouter les voisins du même carré (2x2)
            square_start_x = 3 * (x // 3)
            square_start_y = 3 * (y // 3)
            for i in range(square_start_x, square_start_x + 3):
                for j in range(square_start_y, square_start_y + 3):
                    if i != x and j != y:
                        neighbors.add(indices[(i, j)])
            # Mettre à jour le graphe avec les voisins du sommet actuel
            graph[indices[(x, y)]] = list(neighbors)
    return graph


def sol():
    first_vertex = list(monGraphe.keys())[0]
    vertex_color = {v: None for v in monGraphe}

    for value, color_name in colors_dict.items():
        # Trouver toutes les positions où la valeur est présente dans la grille
        positions = [
            (x, y) for x in range(9) for y in range(9) if grille[x][y] == value
        ]
        # Attribuer la couleur à ces positions
        for p in positions:
            vertex_color[assign_indices()[p]] = value  # Utiliser la valeur comme clé

    if bkt.backtrack(monGraphe, first_vertex, colors_dict.keys(), vertex_color):
        # Correction lors de l'impression du résultat
        result = {
            k: colors_dict[v] if v is not None else None
            for k, v in vertex_color.items()
        }
        return result
    return None


def sol_final(sol_from_backtrack):
    return {k: colors_inv[v] for k, v in sol_from_backtrack.items()}


# --------------------------------------------FONCTION DE RESOLUTION ---------------------------------------------#
def sudokuSolver():
    global monGraphe, sol_init, final_result, colors_inv
    monGraphe = graph_from_grid()
    sol_init = sol()
    colors_inv = inverse_dict(colors_dict)
    final_result = sol_final(sol_init)
    # ---------------------------------------AFFICHAGE DANS LE TERMINAL ----------------------------------------#
    # ----------------------------------------AFFICHAGE DU SUDOKU INITIAL --------------------#
    print("Sudoku initial :")
    for row in grille:
        print(" ".join(map(str, row)))
    # ---------------------------------------AFFICHAGE DE LA SOLUTION-------------------------#
    print("Solution du Sudoku :")
    for i in range(9):
        for j in range(9):
            print(colors_inv[sol_init[assign_indices()[(i, j)]]], end=" ")
        print()
    # ------------------------------------DESSINER LE GRAPHE COLORË--------------------------------------------#
    if sol_init is None:
        messagebox.showerror(
            "Erreur", "Aucune solution trouvée. Le graphe ne peut pas être coloré."
        )
    else:
        draw_colored_graph(monGraphe, sol_init)


# ------------------------------------FONCTION PRINCIPAL--------------------------------------------#
if __name__ == "__main__":
    grille = initGrille()
    sudokuSolver()
    afficher_interface_graphique(grille, sol_init, final_result)
