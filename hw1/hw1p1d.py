from myutil import *

color = 'red'
label = '0.1'

graph = snap.TUNGraph.New()
prob = 0.1

for i in range(0, TOTAL_N_NODES):   graph.AddNode(i)

for i in range(0, TOTAL_N_NODES):
    for j in range(i, TOTAL_N_NODES):
        if random.uniform(0, 1) < prob:   graph.AddEdge(i, j)

pyplot.scatter(
    *n_nodes_per_degree(graph),
    c          = color,
    label      = label,
    alpha      = 0.6,
    edgecolors = 'none',
    norm       = True
)

pyplot_options()