import time
import random
import matplotlib.pyplot as plt
from structures import GraphMatrix, GraphPredecessors
from algorithms import kahn_sort, tarjan_sort


def generate_dag(n, saturation=0.5):
    """Generuje losowy acykliczny skierowany graf (DAG) o n wierzchołkach."""
    max_edges = n * (n - 1) // 2
    num_edges = int(max_edges * saturation)
    all_possible = [(i, j) for i in range(1, n + 1) for j in range(i + 1, n + 1)]
    return random.sample(all_possible, num_edges)


def shorten_list(lst, limit=10):
    """Skraca długą listę do formatu [1, 2, 3, ..., 98, 99, 100]."""
    if lst is None: return "CYKL WYKRYTY"
    if len(lst) <= limit:
        return str(lst)
    return f"[{', '.join(map(str, lst[:5]))}, ..., {', '.join(map(str, lst[-5:]))}]"


def format_input_sample(n, edges, limit=5):
    """Generuje fragment tekstu, który byłby w pliku wejściowym."""
    sample = f"{n} {len(edges)}\n"
    for u, v in edges[:limit]:
        sample += f"{u} {v}\n"
    sample += "..."
    return sample


def run_tests():
    n_values = [100, 250, 400, 550, 700, 850, 1000, 1150, 1300, 1500]
    results = {"K_Mat": [], "K_List": [], "T_Mat": [], "T_List": []}

    print("# Raport - sortowanie topologiczne grafów")

    for n in n_values:
        edges = generate_dag(n)

        print(f"\n## Testowanie dla n = {n}")
        print("### Parametry wejściowe (fragment pliku):")
        print("```text")
        print(format_input_sample(n, edges))
        print("```")

        # Inicjalizacja
        g_mat = GraphMatrix(n)
        g_list = GraphPredecessors(n)
        for u, v in edges:
            g_mat.add_edge(u, v)
            g_list.add_edge(u, v)
        g_mat.build_matrix()

        print("\n### Wyniki sortowania:")
        print("| Algorytm | Reprezentacja | Czas [s] | Wynik (fragment) |")
        print("| :--- | :--- | :--- | :--- |")

        # Pomiary
        test_cases = [
            ("Kahna", "Macierz Incydencji", kahn_sort, g_mat, "K_Mat"),
            ("Kahna", "Lista Poprzedników", kahn_sort, g_list, "K_List"),
            ("Tarjana", "Macierz Incydencji", tarjan_sort, g_mat, "T_Mat"),
            ("Tarjana", "Lista Poprzedników", tarjan_sort, g_list, "T_List")
        ]

        for name, repr_name, algo, g_obj, res_key in test_cases:
            start = time.perf_counter()
            sort_res = algo(g_obj)
            end = time.perf_counter()

            duration = end - start
            results[res_key].append(duration)

            short_res = shorten_list(sort_res)
            print(f"| {name} | {repr_name} | {duration:.6f} | {short_res} |")

        print('---')

    return n_values, results


def plot_all(n_values, res):
    # WYKRESY LINIOWE

    # Macierz incydencji
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, res["K_Mat"], 'r-o', label='Algorytm Kahna')
    plt.plot(n_values, res["T_Mat"], 'b-o', label='Algorytm Tarjana')
    plt.title("Macierz Incydencji")
    plt.xlabel("Liczba wierzchołków (n)")
    plt.ylabel("Czas obliczeń [s]")
    plt.legend()
    plt.savefig("plot_linear_matrix.png")
    plt.show()

    # Lista poprzedników
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, res["K_List"], 'r-s', label='Algorytm Kahna')
    plt.plot(n_values, res["T_List"], 'b-s', label='Algorytm Tarjana')
    plt.title("Lista Poprzedników")
    plt.xlabel("Liczba wierzchołków (n)")
    plt.ylabel("Czas obliczeń [s]")
    plt.legend()
    plt.savefig("plot_linear_predecessors.png")
    plt.show()


    # WYKRESY LOGARYTMICZNE

    # Metoda Kahna
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, res["K_Mat"], 'r-o', label='Macierz Incydencji')
    plt.plot(n_values, res["K_List"], 'b-s', label='Lista Poprzedników')

    plt.yscale('log')  # Skala logarytmiczna tylko dla osi Y
    plt.title('Sortowanie Topologiczne: Metoda Kahna')
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas obliczeń [s] (skala logarytmiczna)')
    plt.legend()
    plt.savefig("plot_log_kahn.png")
    plt.show()

    # Metoda Tarjana
    plt.figure(figsize=(8, 6))
    plt.plot(n_values, res["T_Mat"], 'r-o', label='Macierz Incydencji')
    plt.plot(n_values, res["T_List"], 'b-s', label='Lista Poprzedników')

    plt.yscale('log')  # Skala logarytmiczna tylko dla osi Y
    plt.title('Sortowanie Topologiczne: Metoda Tarjana')
    plt.xlabel('Liczba wierzchołków (n)')
    plt.ylabel('Czas obliczeń [s] (skala logarytmiczna)')
    plt.legend()
    plt.savefig("plot_log_tarjan.png")
    plt.show()