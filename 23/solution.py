from itertools import combinations
import networkx as nx

# Create an empty graph
network_graph = nx.Graph()

# Read the network connections from the file and add edges to the graph
with open("23/data.txt", "rt") as file:
    network_graph.add_edges_from((line[0:2], line[3:5]) for line in file)

# Initialize variables to store cliques and the largest clique
three_computer_cliques, largest_clique, largest_clique_size = set(), None, 0

# Find all cliques in the graph
for clique in nx.find_cliques(network_graph):
    if len(clique) >= 3:
        # Add cliques of size 3 or more that contain at least one computer starting with 't'
        three_computer_cliques |= set(
            tuple(sorted(c))
            for c in combinations(clique, 3)
            if c[0][0] == "t" or c[1][0] == "t" or c[2][0] == "t"
        )

# * Part 1
res = len(three_computer_cliques)
print(res)
