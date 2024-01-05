import networkx as nx
import matplotlib.pyplot as plt


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

    # Affichage
    plt.show()
