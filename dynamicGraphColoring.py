import tkinter as tk
from tkinter import messagebox
from welsh_powell import welsh_powell
from display import draw_colored_graph

# -----------------------------------DECLARATION-------------------------------------------------------------#
monGraphe = {}


# -------------------------------------------AJOUT D'UN OU PLUSIEURS SOMMET(S)-------------------------------#
def ajoutSommet():
    vertexFrame = tk.Tk()
    vertexFrame.title("Ajout Sommet")
    nbr_vertex_label = tk.Label(
        vertexFrame, text="Enter un ou plusieurs sommet séparer par un espace: "
    )
    nbr_vertex_entry = tk.Entry(vertexFrame)
    bouton = tk.Button(
        vertexFrame,
        text=" Valider ",
        command=lambda: action_bouton_vertex_add(nbr_vertex_entry),
    )

    nbr_vertex_label.grid(row=0, column=0, sticky=tk.E, padx=5, pady=10)
    nbr_vertex_entry.grid(row=0, column=1, padx=10, pady=10)
    bouton.grid(row=2, column=0, columnspan=2, pady=10)
    vertexFrame.mainloop()


def action_bouton_vertex_add(entry):
    vertex_entry = entry.get()
    if not vertex_entry:
        messagebox.showerror("Erreur", "Veuillez entrer au moins un sommet.")
        return
    try:
        vertex_list = list(map(int, vertex_entry.split()))
        for v in vertex_list:
            if v not in monGraphe:
                monGraphe[v] = []
            else:
                messagebox.showwarning(
                    "Warnning",
                    "il existe des sommets identiques , par défaut on les considère comme étant un seul sommet ",
                )
        update_buttons_state()
        couleur_sommets = welsh_powell(monGraphe)
        draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


# -------------------------------------------AJOUT D'UN ARC----------------------------------------------------#
def ajoutArc():
    edgeFrame = tk.Tk()
    edgeFrame.title("Ajout arc")
    vertex_1 = tk.Label(edgeFrame, text="Entrer le première extrémité : ")
    vertex_2 = tk.Label(edgeFrame, text="Entrer la deuxième extrémité : ")
    vertex_entry_1 = tk.Entry(edgeFrame)
    vertex_entry_2 = tk.Entry(edgeFrame)
    bouton = tk.Button(
        edgeFrame,
        text=" Valider ",
        command=lambda: action_bouton_egde_add(vertex_entry_1, vertex_entry_2),
    )
    vertex_1.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
    vertex_entry_1.grid(row=0, column=1, padx=10, pady=10)
    vertex_2.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
    vertex_entry_2.grid(row=1, column=1, padx=10, pady=10)

    bouton.grid(row=2, column=0, columnspan=2, pady=10)
    edgeFrame.mainloop()


def action_bouton_egde_add(entry1, entry2):
    sommet1 = entry1.get()
    sommet2 = entry2.get()
    try:
        v1 = int(sommet1)
        v2 = int(sommet2)
        if (v1 in monGraphe) and (v2 in monGraphe):
            monGraphe[v1].append(v2)
            monGraphe[v2].append(v1)
            update_buttons_state()
            couleur_sommets = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, couleur_sommets)
        else:
            messagebox.showwarning(
                "Warning",
                message=f"L'un ou les deux sommets n'existe pas dans le graphe",
            )
            couleur_sommets = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


# -----------------------------------------SUPPRESSION D'UN SOMMET--------------------------------------------#
def suppressionS():
    vertexFrame = tk.Tk()
    vertexFrame.title("Suppression Sommet")
    nbr_vertex_label = tk.Label(vertexFrame, text="Enter un sommet: ")
    nbr_vertex_entry = tk.Entry(vertexFrame)
    bouton = tk.Button(
        vertexFrame,
        text=" Valider ",
        command=lambda: action_bouton_vertex_supp(nbr_vertex_entry),
    )

    nbr_vertex_label.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
    nbr_vertex_entry.grid(row=0, column=1, padx=10, pady=10)
    bouton.grid(row=2, column=0, columnspan=2, pady=10)
    vertexFrame.mainloop()


def action_bouton_vertex_supp(entry):
    sommet = entry.get()
    try:
        sommet = int(sommet)
        if sommet in monGraphe:
            del monGraphe[sommet]
            for v in monGraphe:
                monGraphe[v] = [voisin for voisin in monGraphe[v] if voisin != sommet]
            messagebox.showinfo(
                "Info", message=f"le sommet '{sommet}' a été supprimé avec success"
            )
            update_buttons_state()
            couleur_sommets = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, couleur_sommets)
        else:
            messagebox.showwarning(
                "Warning", message=f"le sommet '{sommet}' n'existe pas dans le graphe"
            )
            couleur_sommets = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


# -------------------------------------------SUPPRESSION D'UN ARC-----------------------------------------------#
def suppressionA():
    edgeFrame = tk.Tk()
    edgeFrame.title("Suppression arc")
    vertex_1 = tk.Label(edgeFrame, text="Entrer le première extrémité : ")
    vertex_2 = tk.Label(edgeFrame, text="Entrer la deuxième extrémité : ")
    vertex_entry_1 = tk.Entry(edgeFrame)
    vertex_entry_2 = tk.Entry(edgeFrame)
    bouton = tk.Button(
        edgeFrame,
        text=" Valider ",
        command=lambda: action_bouton_egde_supp(vertex_entry_1, vertex_entry_2),
    )
    vertex_1.grid(row=0, column=0, sticky=tk.E, padx=10, pady=10)
    vertex_entry_1.grid(row=0, column=1, padx=10, pady=10)
    vertex_2.grid(row=1, column=0, sticky=tk.E, padx=10, pady=10)
    vertex_entry_2.grid(row=1, column=1, padx=10, pady=10)

    bouton.grid(row=2, column=0, columnspan=2, pady=10)
    edgeFrame.mainloop()


def action_bouton_egde_supp(entry1, entry2):
    sommet1 = entry1.get()
    sommet2 = entry2.get()
    try:
        v1 = int(sommet1)
        v2 = int(sommet2)
        if (v1 in monGraphe) and (v2 in monGraphe):
            if v2 in monGraphe[v1] and v1 in monGraphe[v2]:
                monGraphe[v1].remove(v2)
                monGraphe[v2].remove(v1)
                update_buttons_state()
                couleur_sommets = welsh_powell(monGraphe)
                draw_colored_graph(monGraphe, couleur_sommets)
            else:
                messagebox.showwarning(
                    "Warning", " L'arc entre ces deux sommets n'existe pas."
                )
                couleur_sommets = welsh_powell(monGraphe)
                draw_colored_graph(monGraphe, couleur_sommets)
        else:
            messagebox.showwarning(
                "Warning", " L'un ou les deux sommets n'existe pas dans le graphe."
            )
            couleur_sommets = welsh_powell(monGraphe)
            draw_colored_graph(monGraphe, couleur_sommets)

    except ValueError:
        messagebox.showerror("Erreur", " Veuillez entrer des nombres entiers valides.")
        return


# -------------------------------------------FENETRE PRINCIPALE---------------------------------------------------#
app = tk.Tk()
app.title("Graph Coloring Apk")
app.maxsize(400, 350)
app.minsize(300, 300)
largeur_ecran = app.winfo_screenwidth()
hauteur_ecran = app.winfo_screenheight()


largeur_fenetre = 300
hauteur_fenetre = 300

x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2


app.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")


ajoutS = tk.Button(app, text="Ajouter un Sommet", width="20", command=ajoutSommet)
suppS = tk.Button(app, text="Supprimer un Sommet", width="20", command=suppressionS)
ajoutA = tk.Button(app, text="Ajouter un Arc", width="20", command=ajoutArc)
suppA = tk.Button(app, text="Supprimer un Arc", width="20", command=suppressionA)


def quitter_application():
    app.destroy()


quitter = tk.Button(
    app,
    text="Quit",
    width="20",
    background="red",
    foreground="white",
    command=quitter_application,
)


def reset_action():
    global monGraphe
    monGraphe = {}
    suppS["state"] = tk.DISABLED
    suppA["state"] = tk.DISABLED
    ajoutA["state"] = tk.DISABLED
    messagebox.showinfo("Info", " le graphe a été réinitialiser")


reset = tk.Button(
    app,
    text="Reset",
    width="20",
    background="blue",
    foreground="white",
    command=reset_action,
)


def update_buttons_state():
    if len(monGraphe) >= 1:
        suppS["state"] = tk.NORMAL
    else:
        suppS["state"] = tk.DISABLED

    if len(monGraphe) >= 2:
        ajoutA["state"] = tk.NORMAL
    else:
        ajoutA["state"] = tk.DISABLED
    nb_arcs = sum(len(neighbors) for neighbors in monGraphe.values()) // 2
    if nb_arcs >= 1:
        suppA["state"] = tk.NORMAL
    else:
        suppA["state"] = tk.DISABLED


ajoutS.grid(row=0, column=1, padx=10, pady=10)
suppS.grid(row=1, column=1, padx=10, pady=10)
ajoutA.grid(row=2, column=1, padx=10, pady=10)
suppA.grid(row=3, column=1, padx=10, pady=10)
reset.grid(row=4, column=1, padx=10, pady=10)
quitter.grid(row=5, column=1, padx=10, pady=10)


app.columnconfigure(1, weight=1)

update_buttons_state()
app.mainloop()
