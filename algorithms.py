import collections
import sys

# Zwiększenie limitu dla głębokiego DFS (Tarjan)
sys.setrecursionlimit(5000)


def kahn_sort(graph):
    """Algorytm Kahna - usuwanie wierzchołków o stopniu wejściowym 0."""
    in_degree = [graph.get_in_degree(i) for i in range(graph.v)]
    queue = collections.deque([i for i, d in enumerate(in_degree) if d == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u + 1)
        for v in graph.get_out_neighbors(u):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(result) != graph.v:
        return None  # Cykl wykryty
    return result


def tarjan_sort(graph, start_node=None):
    """Algorytm Tarjana - DFS z wykrywaniem cykli."""
    visited = [0] * graph.v  # 0: biały, 1: szary (w trakcie), 2: czarny (odwiedzony)
    stack = []
    has_cycle = False

    def visit(u):
        nonlocal has_cycle
        if visited[u] == 1:
            has_cycle = True
            return
        if visited[u] == 2:
            return

        visited[u] = 1
        for v in graph.get_out_neighbors(u):
            visit(v)
            if has_cycle: return

        visited[u] = 2
        stack.append(u + 1)

    # Opcjonalny start z konkretnego wierzchołka (wymaganie projektowe)
    if start_node is not None and 1 <= start_node <= graph.v:
        visit(start_node - 1)

    # Odwiedzenie pozostałych (standardowa procedura)
    for i in range(graph.v):
        if visited[i] == 0:
            visit(i)
        if has_cycle: break

    return None if has_cycle else stack[::-1]