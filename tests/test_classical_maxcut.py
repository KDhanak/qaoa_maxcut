import itertools

EDGES = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 2)]

def cut_value(bits, edges):
    return sum(int(bits[u] != bits[v]) for u, v in edges)

def brute_force_max_cut(num_nodes, edges):
    best_value = -1
    best_assignments = []
    for bits in itertools.product([0, 1], repeat=num_nodes):
        value = cut_value(bits, edges)
        if value > best_value:
            best_value = value
            best_assignments = [bits]
        elif value == best_value:
            best_assignments.append(bits)
    return best_value, best_assignments

def test_cut_value_known_optimum():
    assert cut_value((0, 1, 0, 1), EDGES) == 4

def test_bruteforce_returns_expected_optimum():
    best_value, _ = brute_force_max_cut(4, EDGES)
    assert best_value == 4
