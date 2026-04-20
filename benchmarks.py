import time
import random
import matplotlib.pyplot as plt
import numpy as np
from structures import GraphMatrix, GraphPredecessors
from algorithms import kahn_sort, tarjan_sort


def generate_dag(n, saturation=0.5):
    """Generuje losowy DAG o n wierzchołkach."""
    max_edges = n * (n - 1) // 2
    num_edges = int(max_edges * saturation)
    all_possible = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    return random.sample(all_possible, num_edges)


def run_tests():
    n_values = [100, 250, 500, 750]
    results = {"K_Mat": [], "K_List": [], "T_Mat": [], "T_List": []}

    for n in n_values:
        print(f"Testowanie n={n}...")
        edges = generate_dag(n)

        # Inicjalizacja
        g_mat = GraphMatrix(n)
        g_list = GraphPredecessors(n)
        for u, v in edges:
            g_mat.add_edge(u, v)
            g_list.add_edge(u, v)
        g_mat.build_matrix()

        # Pomiary
        for label, algo, g_obj in [
            ("K_Mat", kahn_sort, g_mat), ("K_List", kahn_sort, g_list),
            ("T_Mat", tarjan_sort, g_mat), ("T_List", tarjan_sort, g_list)
        ]:
            start = time.perf_counter()
            algo(g_obj)
            results[label].append(time.perf_counter() - start)

    return n_values, results


def plot_all(n_values, res):
    # Wykresy liniowe
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    ax1.plot(n_values, res["K_Mat"], 'r-o', label='Kahn (Matrix)')
    ax1.plot(n_values, res["T_Mat"], 'b-o', label='Tarjan (Matrix)')
    ax1.set_title("Macierz Incydencji")
    ax1.legend()

    ax2.plot(n_values, res["K_List"], 'r-s', label='Kahn (List)')
    ax2.plot(n_values, res["T_List"], 'b-s', label='Tarjan (List)')
    ax2.set_title("Lista Poprzedników")
    ax2.legend()

    plt.show()

    # Wykresy logarytmiczne
    plt.figure(figsize=(7, 5))
    for k, v in res.items():
        plt.loglog(n_values, v, label=k)
    plt.title("Skala logarytmiczna - Porównanie")
    plt.legend()
    plt.show()