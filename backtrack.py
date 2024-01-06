import tkinter as tk
from tkinter import messagebox
from display import draw_colored_graph
from color import pallete_couleurs


# -----------------------------------DECLARATION-----------------------------------------#
monGraphe = {}
graph_drawing_window = None


# -----------------------------------FONCTIONS UTILITARES--------------------------------#
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


# -----------------------------------FONCTION DE BASE (BACKTRACK)---------------------#
def backtrack(graphe, vertex, colors, solution):
    if vertex is None:
        return True
    for col in colors:
        if isSafeToColor(graphe, vertex, col, solution):
            solution[vertex] = col

            next_vertex = getNextVertex(graphe, solution)

            if backtrack(graphe, next_vertex, colors, solution):
                return True

            solution[vertex] = None
    return False


# -----------------------------------------GUI-------------------------------------------#


def graph_from_backtrack():
    global monGraphe, error_detected

    def open_vertex_window():
        global entry_vertex, entry_neighbors, vertex_window

        def add_vertex_and_close():
            global error_detected
            add_vertex()
            # Supprimer la fenêtre pop-up seulement si aucune erreur n'est détectée
            if not error_detected:
                close_vertex_window()

        def add_vertex():
            global vertices, error_detected

            vertex_str = entry_vertex.get()
            neighbors_str = entry_neighbors.get().split()

            try:
                vertex = int(vertex_str)
                neighbors = [int(neighbor) for neighbor in neighbors_str]

                if vertex in neighbors:
                    raise ValueError("Un sommet ne peut pas être son propre voisin.")

                if len(neighbors) > vertices - 1:
                    raise ValueError(
                        f"La liste des voisins doit avoir une longueur inférieure à {vertices}."
                    )

                # Mise à jour du graphe
                if vertex not in monGraphe:
                    monGraphe[vertex] = []

                for neighbor in neighbors:
                    if neighbor == vertex:
                        raise ValueError(f"Erreur dans les voisins de {vertex}.")

                    if neighbor not in monGraphe:
                        if len(monGraphe) >= vertices:
                            raise ValueError(
                                f"Le graphe a déjà atteint le nombre maximal de sommets. Veuillez ressaisir les valeurs."
                            )

                        monGraphe[neighbor] = []

                    if vertex not in monGraphe[neighbor]:
                        monGraphe[neighbor].append(vertex)
                    if neighbor not in monGraphe[vertex]:
                        monGraphe[vertex].append(neighbor)

                # Affichage du graphe actuel
                print("Graphe actuel:", monGraphe)
                error_detected = False

            except ValueError as e:
                error_detected = True
                messagebox.showerror("Erreur", str(e))

            finally:
                # Réinitialiser les champs d'entrée
                entry_vertex.delete(0, tk.END)
                entry_neighbors.delete(0, tk.END)

        # Créer une fenêtre pop-up
        vertex_window = tk.Toplevel(app)
        vertex_window.title("Ajouter un sommet")

        label_vertex = tk.Label(vertex_window, text="Sommet:")
        entry_vertex = tk.Entry(vertex_window)

        label_neighbors = tk.Label(
            vertex_window, text="Voisins (séparés par des espaces):"
        )
        entry_neighbors = tk.Entry(vertex_window)

        validate_vertex_button = tk.Button(
            vertex_window, text="Valider", command=add_vertex_and_close
        )

        label_vertex.grid(row=0, column=0, padx=10, pady=5)
        entry_vertex.grid(row=0, column=1, padx=10, pady=5)
        label_neighbors.grid(row=1, column=0, padx=10, pady=5)
        entry_neighbors.grid(row=1, column=1, padx=10, pady=5)
        validate_vertex_button.grid(row=2, column=0, columnspan=2, pady=10)

    def close_vertex_window():
        global vertex_window
        vertex_window.destroy()

    def action_button():
        global monGraphe, vertices
        s = entry_1.get()

        try:
            vertices = int(s)
            i = 0
            while i < vertices:
                open_vertex_window()
                app.wait_window(
                    vertex_window
                )  # Attendre que la fenêtre pop-up soit fermée
                i += 1

            first_vertex = list(monGraphe.keys())[0] if monGraphe else None
            v_solution = {v: None for v in monGraphe}
            if first_vertex is not None:
                sol = backtrack(monGraphe, first_vertex, pallete_couleurs, v_solution)
            else:
                messagebox.showerror(
                    "Erreur", "Le graphe est vide. Ajoutez des sommets."
                )
            if sol:
                draw_colored_graph(monGraphe, v_solution)
            else:
                messagebox.showerror(
                    "Erreur",
                    "Aucune solution trouvée. Le graphe ne peut pas être coloré.",
                )
            monGraphe = {}
            app.destroy()
        except ValueError:
            messagebox.showerror(
                "Erreur",
                "Veuillez entrer un nombre entier valide pour le nombre de sommets.",
            )
            return

    def reset_graph():
        global monGraphe
        monGraphe = {}

    def quit_app():
        app.destroy()

    error_detected = False
    app = tk.Tk()
    app.title("backtrack Algorithm")
    app.geometry("250x150")
    app.maxsize(400, 200)
    app.minsize(350, 150)
    validate_button = tk.Button(
        app,
        text="Valider",
        width="20",
        background="blue",
        foreground="white",
        command=action_button,
    )
    quit_button = tk.Button(
        app,
        text="Quitter",
        width="20",
        background="red",
        foreground="white",
        command=quit_app,
    )
    label1 = tk.Label(app, text="Entrer le nombre de sommet: ")
    entry_1 = tk.Entry(app)

    label1.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10, columnspan=2)
    entry_1.grid(row=0, column=2, padx=10, pady=10, columnspan=2)
    validate_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
    quit_button.grid(row=2, column=2, padx=10, pady=10, columnspan=2)

    app.protocol("WM_DELETE_WINDOW", reset_graph)
    app.mainloop()
