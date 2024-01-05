import tkinter as tk
from display import draw_colored_graph
from color import pallete_couleurs

# -----------------------------------DECLARATION---------------------------------------------#
monGraphe = {}


# -----------------------------------FONCTIONS UTILITARES------------------------------------#
def degre(graphe, sommet):
    """
    Calcule le degré d'un sommet dans un graphe représenté par un dictionnaire.

    Parameters:
    - graphe (dict): Dictionnaire représentant le graphe.
    - sommet (int): Le sommet pour lequel on veut calculer le degré.

    Returns:
    - int: Le degré du sommet.
    """
    return len(graphe[sommet])


def trier_sommets_par_degre(graphe):
    """
    Trie les sommets d'un graphe par degré décroissant.

    Parameters:
    - graphe (dict): Dictionnaire représentant le graphe.

    Returns:
    - list: Liste des sommets triés par degré décroissant.
    """
    sommets = list(graphe.keys())
    sorted_sommets = sorted(sommets, key=lambda x: degre(graphe, x), reverse=True)
    return sorted_sommets


# -----------------------------------FONCTION DE BASE (WELSH_POWELL)-------------------------#
def welsh_powell(graphe):
    sommets_tries = trier_sommets_par_degre(graphe)
    couleur_sommets = (
        {}
    )  # Dictionnaire pour stocker les couleurs attribuées à chaque sommet

    while sommets_tries:
        sommet = sommets_tries.pop(
            0
        )  # Prendre le sommet de plus haut degré non encore colorié
        voisins_couleurs = {
            couleur_sommets[voisin]
            for voisin in graphe[sommet]
            if voisin in couleur_sommets
        }

        # Trouver la première couleur disponible pour le sommet
        nouvelle_couleur = next(
            c for c in pallete_couleurs if c not in voisins_couleurs
        )

        couleur_sommets[sommet] = nouvelle_couleur

    return couleur_sommets


# -------------------------------------------GUI---------------------------------------------#
def graphe_from_welsh():
    global monGraphe

    def add_vertex_and_close():
        add_vertex()
        close_vertex_window()

    def add_vertex():
        global entry_vertex, entry_neighbors
        vertex = entry_vertex.get()
        neighbors = entry_neighbors.get().split()

        if vertex in neighbors:
            tk.messagebox.showerror(
                "Erreur",
                " Un sommet ne peut pas être son propre voisin. Veuillez ressaisir.",
            )
            return

        # Mise à jour du graphe
        if vertex not in monGraphe:
            monGraphe[vertex] = []

        for neighbor in neighbors:
            if neighbor != vertex and neighbor not in monGraphe[vertex]:
                monGraphe[vertex].append(neighbor)

            if neighbor not in monGraphe:
                monGraphe[neighbor] = []

            if vertex != neighbor and vertex not in monGraphe[neighbor]:
                monGraphe[neighbor].append(vertex)

        # Affichage du graphe actuel
        print("Graphe actuel:", monGraphe)

        # Réinitialiser les champs d'entrée
        entry_vertex.delete(0, tk.END)
        entry_neighbors.delete(0, tk.END)

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

    def action_button():
        global monGraphe
        s = entry_1.get()
        try:
            vertices = int(s)
            for _ in range(vertices):
                open_vertex_window()
                app.wait_window(
                    vertex_window
                )  # Attendre que la fenêtre pop-up soit fermée
            sol = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, sol)
            monGraphe = {}
            app.destroy()
        except ValueError:
            tk.messagebox.showerror(
                "Erreur", " Veuillez entrer des nombres entiers valides."
            )
            return

    def reset_graph():
        global monGraphe
        monGraphe = {}

    app = tk.Tk()
    app.title("Welsh_Powell Algorithm")
    app.geometry("250x150")

    app.maxsize(400, 200)
    app.minsize(400, 150)

    validate_button = tk.Button(app, text="Valider", width="20", command=action_button)

    label1 = tk.Label(app, text="Entrer le nombre de sommet: ")
    entry_1 = tk.Entry(app)

    label1.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10, columnspan=2)
    entry_1.grid(row=0, column=2, padx=10, pady=10, columnspan=2)

    validate_button.grid(row=2, column=1, padx=10, pady=10, columnspan=2)
    app.protocol("WM_DELETE_WINDOW", reset_graph)
    app.mainloop()
