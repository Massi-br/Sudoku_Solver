import tkinter as tk
from welsh_powell import graphe_from_welsh
from backtrack import graph_from_backtrack
from greedy import graph_from_greedy


def run_algorithm(algorithm_function):
    algorithm_function()


def main_window():
    app = tk.Tk()
    app.title("Graph Coloring Algorithm")
    app.maxsize(400, 250)
    app.minsize(300, 200)

    # Center the window on the screen
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    window_width = 300
    window_height = 300

    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    app.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    bk_button = tk.Button(
        app,
        text="Backtrack Algorithm",
        width="20",
        command=lambda: run_algorithm(graph_from_backtrack),
    )
    wp_button = tk.Button(
        app,
        text="Welsh-Powell Algorithm",
        width="20",
        command=lambda: run_algorithm(graphe_from_welsh),
    )
    greedy_button = tk.Button(
        app,
        text="Greedy Algorithm",
        width="20",
        command=lambda: run_algorithm(graph_from_greedy),
    )

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

    bk_button.grid(row=0, column=1, padx=10, pady=10)
    wp_button.grid(row=1, column=1, padx=10, pady=10)
    greedy_button.grid(row=2, column=1, padx=10, pady=10)
    quitter.grid(row=3, column=1, padx=10, pady=10)

    app.columnconfigure(1, weight=1)
    app.mainloop()


if __name__ == "__main__":
    main_window()
