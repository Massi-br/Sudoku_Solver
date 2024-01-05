import tkinter as tk
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


# -----------------------------------FONCTION DE BASE (WELSH_POWELL)---------------------#
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


# -----------------------------------------GUI-------------------------------------------#


def graph_from_backtrack():
    global monGraphe, graph_drawing_window

    def open_vertex_window():
        global entry_vertex, entry_neighbors, vertex_window

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

    def add_vertex_and_close():
        add_vertex()
        close_vertex_window()

    def add_vertex():
        global monGraphe, entry_vertex, entry_neighbors, graph_drawing_window

        # Ajout du sommet au graphe
        vertex = entry_vertex.get()
        neighbors = entry_neighbors.get().split()

        if vertex in neighbors:
            tk.messagebox.showerror(
                "Erreur",
                " Un sommet ne peut pas être son propre voisin. Veuillez ressaisir.",
            )
            return

        if vertex not in monGraphe:
            monGraphe[vertex] = []
        for neighbor in neighbors:
            if neighbor != vertex and neighbor not in monGraphe[vertex]:
                monGraphe[vertex].append(neighbor)

            if neighbor not in monGraphe:
                monGraphe[neighbor] = []

            if vertex != neighbor and vertex not in monGraphe[neighbor]:
                monGraphe[neighbor].append(vertex)

        # Réinitialisation des champs d'entrée
        entry_vertex.delete(0, tk.END)
        entry_neighbors.delete(0, tk.END)
        if graph_drawing_window is not None:
            graph_drawing_window.protocol("WM_DELETE_WINDOW", reset_graph)
        graph_drawing_window = None

    def action_button():
        global graph_drawing_window
        s = entry_1.get()
        try:
            vertices = int(s)
            # Appel de la fonction pour ajouter les sommets
            for _ in range(vertices):
                open_vertex_window()
                app.wait_window(vertex_window)
            # Affichage du graphe actuel
            print("Graphe actuel:", monGraphe)

            # Appel de la fonction backtrack avec le graphe spécifié par l'utilisateur
            first_vertex = list(monGraphe.keys())[0] if monGraphe else None
            v_solution = {v: None for v in monGraphe}
            if first_vertex is not None:
                sol = backtrack(monGraphe, first_vertex, pallete_couleurs, v_solution)
            else:
                tk.messagebox.showerror(
                    "Erreur", "Le graphe est vide. Ajoutez des sommets."
                )
            if sol:
                draw_colored_graph(monGraphe, v_solution)
            else:
                tk.messagebox.showerror(
                    "Erreur",
                    "Aucune solution trouvée. Le graphe ne peut pas être coloré.",
                )
            if graph_drawing_window is not None:
                graph_drawing_window.protocol("WM_DELETE_WINDOW", reset_graph)
                graph_drawing_window = None
            app.destroy()
        except ValueError:
            tk.messagebox.showerror(
                "Erreur", " Veuillez entrer un nombre entiers valides."
            )
            return

    def reset_graph():
        global monGraphe
        monGraphe = {}

    app = tk.Tk()
    app.title("Backtrack Algorithm")
    app.geometry("250x150")

    app.maxsize(400, 200)
    app.minsize(400, 150)

    validate_button = tk.Button(app, text="Valider", width="20", command=action_button)

    label1 = tk.Label(app, text="Entrer le nombre de sommet: ")
    entry_1 = tk.Entry(app)

    label1.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10, columnspan=2)
    entry_1.grid(row=0, column=2, padx=10, pady=10, columnspan=2)

    validate_button.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

    app.mainloop()
