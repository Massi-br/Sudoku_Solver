from tkinter import ttk
import backtrack as bkt
from display import draw_colored_graph
import tkinter as tk
from tkinter import messagebox


# -----------------------------------------------------DECLARATION--------------------------------------------#
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


# ---------------------------------------------FONCTIONS UTILITARES-------------------------------------------#
def assign_indices():
    indices = {}
    count = 0
    for x in range(9):
        for y in range(9):
            indices[(x, y)] = count
            count += 1
    return indices


def inverse_dict(d):
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


# --------------------------------------------APPELS AU FONCTIONS---------------------------------------------#

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

# -------------------------------------------CLASSE D'AFFICHAGE (GUI)--------------------------------------#


class SudokuGUI:
    def __init__(self, master, sudoku_initial, color_grid, sudoku_solution):
        self.master = master
        self.master.title("Sudoku Solver")
        self.sudoku_initial = sudoku_initial
        self.color_grid = color_grid
        self.sudoku_solution = sudoku_solution
        self.create_grid()

    def create_grid(self):
        frame_initial = ttk.Frame(self.master)
        frame_initial.grid(row=0, column=0, padx=5)

        frame_color = ttk.Frame(self.master)
        frame_color.grid(row=0, column=1, padx=5)

        frame_solution = ttk.Frame(self.master)
        frame_solution.grid(row=0, column=2, padx=5)

        # Grille initiale
        ttk.Label(frame_initial, text="Sudoku Initial", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=9
        )
        canvas_initial = tk.Canvas(frame_initial, width=400, height=450)
        canvas_initial.grid(row=1, column=0, columnspan=9)
        self.draw_grid(canvas_initial, self.sudoku_initial)

        # Grille de couleurs
        ttk.Label(frame_color, text="Grille de Couleurs", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=9
        )
        canvas_color = tk.Canvas(frame_color, width=400, height=450)
        canvas_color.grid(row=1, column=0, columnspan=9)
        self.draw_color_grid(canvas_color, self.color_grid)

        # Grille solution
        ttk.Label(frame_solution, text="Sudoku Solution", font=("Arial", 16)).grid(
            row=0, column=0, columnspan=9
        )
        canvas_solution = tk.Canvas(frame_solution, width=400, height=450)
        canvas_solution.grid(row=1, column=0, columnspan=9)
        self.draw_grid(canvas_solution, self.sudoku_solution)

    def draw_grid(self, canvas, grid):
        cell_size = 40

        for i in range(9):
            for j in range(9):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                if isinstance(
                    grid, list
                ):  # Pour la grille initiale et la grille solution (liste de listes)
                    value = grid[i][j]
                else:  # Pour la grille de couleurs (dictionnaire)
                    value = grid[assign_indices()[i, j]]

                if value != 0:
                    canvas.create_text(
                        (x1 + x2) / 2,
                        (y1 + y2) / 2,
                        text=str(value),
                        font=("Arial", 16),
                    )

    def draw_color_grid(self, canvas, color_grid):
        cell_size = 40

        for i in range(9):
            for j in range(9):
                x1, y1 = j * cell_size, i * cell_size
                x2, y2 = x1 + cell_size, y1 + cell_size
                canvas.create_rectangle(
                    x1,
                    y1,
                    x2,
                    y2,
                    fill=color_grid[assign_indices()[i, j]],
                    outline="black",
                )


if __name__ == "__main__":
    # Utilisation de la classe avec les grilles initiale, de couleurs et solution
    root = tk.Tk()
    app = SudokuGUI(root, grille, sol_init, final_result)
    root.mainloop()
