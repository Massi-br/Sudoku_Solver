import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
import color


def degre(graphe, sommet):
    return len(graphe[sommet])


def trier_sommets_par_degre(graphe):
    sommets = list(graphe.keys())
    sorted_sommets = sorted(sommets, key=lambda x: degre(graphe, x), reverse=True)
    return sorted_sommets


node_colors = color.valeurs_couleurs


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
    plt.show()


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
        nouvelle_couleur = next(c for c in node_colors if c not in voisins_couleurs)

        couleur_sommets[sommet] = nouvelle_couleur

    return couleur_sommets


# Exemple d'utilisation
monGraphe = {}

# couleur_sommets_base = welsh_powell(monGraphe)
# draw_colored_graph(monGraphe, couleur_sommets_base)


def action_bouton():
    sommet = nbr_vertex_entry.get()
    voisins = v_vertex_entry.get()

    try:
        sommet = int(sommet)
        voisins = list(map(int, voisins.split()))

        if sommet not in monGraphe:
            monGraphe[sommet] = []

        for v in voisins:
            monGraphe[sommet].append(v)
            if v not in monGraphe:
                monGraphe[v] = []
            monGraphe[v].append(sommet)

        # Appliquer l'algorithme de Welsh-Powell
        couleur_sommets = welsh_powell(monGraphe)
        draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        # Gérer une erreur si la conversion en entier échoue
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


# Création de la fenêtre principale
app = tk.Tk()
app.title("Graph Coloring Algorithm")
app.maxsize(400, 150)
app.minsize(400, 150)
largeur_ecran = app.winfo_screenwidth()
hauteur_ecran = app.winfo_screenheight()


largeur_fenetre = 400
hauteur_fenetre = 150

x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2


app.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")


nbr_vertex_label = tk.Label(app, text="Enter un sommet: ")
v_vertex_label = tk.Label(app, text="les voisins séparer avec des espaces: ")
nbr_vertex_entry = tk.Entry(app)
v_vertex_entry = tk.Entry(app)
bouton = tk.Button(app, text="Valider", command=action_bouton)


nbr_vertex_label.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
nbr_vertex_entry.grid(row=0, column=1, padx=10, pady=10)
v_vertex_label.grid(row=1, column=0, sticky=tk.N, padx=10, pady=10)
v_vertex_entry.grid(row=1, column=1, padx=10, pady=10)
bouton.grid(row=2, column=0, columnspan=2, pady=10)


# Lancement de la boucle principale
app.mainloop()
