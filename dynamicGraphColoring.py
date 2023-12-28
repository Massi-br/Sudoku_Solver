import tkinter as tk
from tkinter import messagebox
import welsh_powell as wp


# -----------------------------------DECLARATION----------------------------------#

node_colors = wp.pallete_couleurs

monGraphe = {}


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
        couleur_sommets = wp.welsh_powell(monGraphe)
        wp.draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        # Gérer une erreur si la conversion en entier échoue
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


def ajoutSommet():
    print("s")


def ajoutArc():
    print("s")


def suppressionS():
    print("s")


def suppressionA():
    print("s")


# Création de la fenêtre principale
app = tk.Tk()
app.title("Graph Coloring Algorithm")
app.maxsize(400, 250)
app.minsize(300, 200)
largeur_ecran = app.winfo_screenwidth()
hauteur_ecran = app.winfo_screenheight()


largeur_fenetre = 300
hauteur_fenetre = 200

x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2


app.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")


ajoutS = tk.Button(app, text="Ajouter un Sommet", width="20", command=ajoutSommet)
ajoutA = tk.Button(app, text="Ajouter un Arc", width="20", command=ajoutArc)
suppS = tk.Button(app, text="Supprimer un Sommet", width="20", command=suppressionS)
suppA = tk.Button(app, text="Supprimer un Arc", width="20", command=suppressionA)


ajoutS.grid(row=0, column=1, padx=10, pady=10)
ajoutA.grid(row=1, column=1, padx=10, pady=10)
suppS.grid(row=2, column=1, padx=10, pady=10)
suppA.grid(row=3, column=1, padx=10, pady=10)

app.columnconfigure(1, weight=1)

# nbr_vertex_label = tk.Label(app, text="Enter un sommet: ")
# v_vertex_label = tk.Label(app, text="les voisins séparer avec des espaces: ")
# nbr_vertex_entry = tk.Entry(app)
# v_vertex_entry = tk.Entry(app)
# bouton = tk.Button(app, text=" Valider ", command=action_bouton)


# nbr_vertex_label.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
# nbr_vertex_entry.grid(row=0, column=1, padx=10, pady=10)
# v_vertex_label.grid(row=1, column=0, sticky=tk.N, padx=10, pady=10)
# v_vertex_entry.grid(row=1, column=1, padx=10, pady=10)
# bouton.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
