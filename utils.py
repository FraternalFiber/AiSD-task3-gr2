def load_graph(filename):
    """Wczytuje graf z pliku tekstowego."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
            if not lines: return None
            v_count, e_count = map(int, lines[0].split())
            edges = [list(map(int, l.split())) for l in lines[1:] if l.strip()]
            return v_count, edges
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return None