from utils import load_graph
from structures import GraphPredecessors
from algorithms import kahn_sort, tarjan_sort
from benchmarks import run_tests, plot_all


def menu():
    print("\n--- PROJEKT: ALGORYTMY GRAFOWE ---")
    print("1. Wczytaj graf z pliku i posortuj")
    print("2. Uruchom testy wydajnościowe (wykresy)")
    print("3. Wyjście")
    return input("Wybór: ")


if __name__ == "__main__":
    while True:
        choice = menu()
        if choice == "1":
            path = input("Podaj nazwę pliku: ")
            data = load_graph(path)
            if data:
                v, edges = data
                print(v)
                graph = GraphPredecessors(v)
                for u, e_v in edges: graph.add_edge(u, e_v)

                kahn_sorted = kahn_sort(graph)

                if kahn_sorted:
                    print("Wynik Kahn:", kahn_sorted)
                else:
                    print("Wykryto cykl! Graf nie może zostać posortowany.")
                    continue

                start_v = input("Wierzchołek startowy dla Tarjana (Enter = domyślny): ")
                sv = int(start_v) if start_v.isdigit() else None

                tarjan_sorted = tarjan_sort(graph)

                if tarjan_sorted:
                    print("Wynik Tarjan:", tarjan_sort(graph, sv))
                else:
                    print("Wykryto cykl! Graf nie może zostać posortowany.")

        elif choice == "2":
            n_vals, results = run_tests()
            plot_all(n_vals, results)
        elif choice == "3":
            break