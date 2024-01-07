from tkinter import ttk
import tkinter as tk


# ---------------------------------------------FONCTIONS UTILITARES-------------------------------------------#
def assign_indices():
    """Cette fonction attribue des indices uniques à chaque position (x, y) dans une grille 9x9.
    Les indices sont utilisés pour représenter chaque cellule de la grille de manière linéaire
    """
    indices = {}
    count = 0
    for x in range(9):
        for y in range(9):
            indices[(x, y)] = count
            count += 1
    return indices


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


def afficher_interface_graphique(grille, sol_init, final_result):
    root = tk.Tk()
    SudokuGUI(root, grille, sol_init, final_result)
    root.mainloop()
