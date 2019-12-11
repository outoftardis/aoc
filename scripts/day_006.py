# day 6
import os
import networkx as nx

def parse_data(datafile):
    pairs = []
    with open(datafile, 'r') as f:
        for pair in f.readlines():
            orbit = pair.strip().split(')')
            pairs.append(tuple(orbit))
    return pairs

def make_graph(pairs):
    G = nx.Graph()
    G.add_edges_from(pairs)
    return G

def count_orbites(G):
    planets = [i for i in G.nodes() if i != "COM"]
    print(len(planets))
    total = 0
    for planet in planets:
        for path in nx.all_simple_paths(G, 'COM', planet):
            total += len(path) - 1
    return total


script_path = os.path.dirname(__file__)
input_file = os.path.relpath('..//input//006.txt', script_path)

pairs = parse_data(input_file)
system = make_graph(pairs)

# task 1
total = count_orbites(system)
print(total)

# task 2
transfer_path = nx.shortest_path(system, "YOU", "SAN")
print(len(transfer_path)-3)