import tkinter as tk
from welsh_powell import create_graph_interface


def on_button_click(algorithm_function):
    algorithm_function()


app = tk.Tk()
app.title("Graph Coloring Algorithm")
app.maxsize(400, 150)
app.minsize(200, 150)
largeur_ecran = app.winfo_screenwidth()
hauteur_ecran = app.winfo_screenheight()

largeur_fenetre = 300
hauteur_fenetre = 300

x_position = (largeur_ecran - largeur_fenetre) // 2
y_position = (hauteur_ecran - hauteur_fenetre) // 2

app.geometry(f"{largeur_fenetre}x{hauteur_fenetre}+{x_position}+{y_position}")

ajoutS = tk.Button(
    app,
    text="Backtrack Algorithm",
    width="20",
    command=lambda: on_button_click(backtrack_algorithm_interface),
)
ajoutA = tk.Button(
    app,
    text="Welsh-Powell Algorithm",
    width="20",
    command=lambda: on_button_click(create_graph_interface),
)
suppS = tk.Button(
    app,
    text="Greedy Algorithm",
    width="20",
    command=lambda: on_button_click(greedy_algorithm_interface),
)

ajoutS.grid(row=0, column=1, padx=10, pady=10)
ajoutA.grid(row=1, column=1, padx=10, pady=10)
suppS.grid(row=2, column=1, padx=10, pady=10)

app.columnconfigure(1, weight=1)

app.mainloop()
