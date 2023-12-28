import backtrack as bkt
import networkx as nx
import matplotlib.pyplot as plt
from tkinter import messagebox, ttk
import tkinter as tk
import scipy as sp


def assign_indices():
    indices = {}
    count = 0
    for x in range(9):
        for y in range(9):
            indices[(x, y)] = count
            count += 1
    return indices


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


monGraphe = graph_from_grid()
# Affichage du graphe
# for sommet, voisins in monGraphe.items():
#     print(f"{sommet} : {voisins}")

# Exemple d'utilisation
grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

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


sol_init = sol()
print(sol_init)


def inverse_dict(d):
    return {v: k for k, v in d.items()}


colors_inv = inverse_dict(colors_dict)


def sol_final(sol_from_backtrack):
    return {k: colors_inv[v] for k, v in sol_from_backtrack.items()}


final_result = sol_final(sol_init)

# Affichage du Sudoku initial
print("Sudoku initial :")
for row in grille:
    print(" ".join(map(str, row)))


# Afficher la solution du Sudoku
print("Solution du Sudoku :")
for i in range(9):
    for j in range(9):
        print(colors_inv[sol_init[assign_indices()[(i, j)]]], end=" ")
    print()

# # -----------------------------------------affichage-------------------------------------


def draw_colored_graph(graph, colors):
    G = nx.from_dict_of_lists(graph)
    # Dessiner le graphe avec les couleurs attribuées
    pos = nx.kamada_kawai_layout(G)
    node_colors = [
        colors.get(sommet, 0) for sommet in G.nodes
    ]  # Utilisez les couleurs attribuées
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        font_color="white",
        font_size=8,
        font_family="Arial",
    )
    # Affichage
    plt.show()


# Dessiner le graphe coloré
if sol_init is None:
    messagebox.showerror(
        "Erreur", "Aucune solution trouvée. Le graphe ne peut pas être coloré."
    )
else:
    draw_colored_graph(monGraphe, sol_init)


class SudokuGUI:
    def __init__(self, master, sudoku_initial, sudoku_solution):
        self.master = master
        self.master.title("Sudoku Solver")
        self.sudoku_initial = sudoku_initial
        self.sudoku_solution = sudoku_solution
        self.create_grid()

    def create_grid(self):
        frame_initial = ttk.Frame(self.master)
        frame_initial.grid(row=0, column=0, padx=5)

        frame_solution = ttk.Frame(self.master)
        frame_solution.grid(row=0, column=1, padx=5)

        # Grille initiale
        ttk.Label(frame_initial, text="Sudoku Initial", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=9
        )
        canvas_initial = tk.Canvas(frame_initial, width=450, height=450)
        canvas_initial.grid(row=1, column=0, columnspan=9)
        self.draw_grid(canvas_initial, self.sudoku_initial)

        # Grille solution
        ttk.Label(frame_solution, text="Sudoku Solution", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=9
        )
        canvas_solution = tk.Canvas(frame_solution, width=450, height=450)
        canvas_solution.grid(row=1, column=0, columnspan=9)
        self.draw_grid(canvas_solution, self.sudoku_solution)

    def draw_grid(self, canvas, grid):
        cell_size = 50

        for i in range(9):
            for j in range(9):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                if isinstance(grid, list):  # Pour la grille initiale (liste de listes)
                    value = grid[i][j]
                elif isinstance(grid, dict):  # Pour la grille solution (dictionnaire)
                    value = grid[assign_indices()[(i, j)]]

                if value != 0:
                    canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text=str(value),
                        font=("Arial", 16),
                    )


if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root, grille, final_result)
    root.mainloop()
