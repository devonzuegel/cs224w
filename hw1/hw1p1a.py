from myutil import *

for i in range(0,6):
  prob  = 0.2 * i
  graph = set_up_graph()

  for node_i in range(3, TOTAL_N_NODES):
    random_node_i = random.randint(0, node_i - 1)
    graph.AddNode(node_i)

    random_prob = random.uniform(0, 1)
    if random_prob < prob:  graph.AddEdge(node_i, random_node_i)
    else:                   graph.AddEdge(node_i, rand_nbr_node(graph, random_node_i))

  pyplot.scatter(*n_nodes_per_degree(graph), c=COLORS[i], label=LABELS[i], alpha=0.5, edgecolors='none', norm=True)

pyplot_options()