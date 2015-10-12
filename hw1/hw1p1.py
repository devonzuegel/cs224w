import snap
import random
import numpy as np
from matplotlib import pyplot

TOTAL_N_NODES = 2000
COLORS = ["red", "blue", "green", "purple", "orange", "black"]
LABELS = ["0.0", "0.2", "0.4", "0.6", "0.8", "1.0"]

def set_up_graph():
  G = snap.TUNGraph.New()
  for n in [0,1,2]:                 G.AddNode(n)
  for e in [(0,1), (1,2), (2,0)]:   G.AddEdge(e[0], e[1])
  return G

def rand_nbr_node(node_index):
  node        = G.GetNI(node_index)
  n_neighbors = node.GetDeg()
  rand_nbr_i  = random.randint(0, n_neighbors - 1)
  return node.GetNbrNId(rand_nbr_i)

def build_degrees_dict(G):
  degrees_dict = {}
  for node_i in range(0, TOTAL_N_NODES):
    deg_n = G.GetNI(node_i).GetDeg()
    if deg_n in degrees_dict:   degrees_dict[deg_n] += 1
    else:                       degrees_dict[deg_n] = 1
  return degrees_dict

def n_nodes_per_degree(G):
  degrees_dict = build_degrees_dict(G)
  n_nodes_per_degree = []
  for k in degrees_dict.keys():
    n_nodes_per_degree.append(1.0 * degrees_dict[k] / TOTAL_N_NODES)
  return degrees_dict.keys(), n_nodes_per_degree

def pyplot_options():
  pyplot.legend(title="Probability")
  pyplot.yscale('log')
  pyplot.xscale('log')
  pyplot.grid(True)
  pyplot.xlabel('degree number')
  pyplot.ylabel('number of nodes')
  pyplot.legend()
  pyplot.ylim([0.0001,1])
  pyplot.show()

for i in range(0,6):
  prob = 0.2 * i
  G    = set_up_graph()

  for node_i in range(3, TOTAL_N_NODES):
    random_node_i = random.randint(0, node_i - 1)
    G.AddNode(node_i)

    random_prob = random.uniform(0, 1)
    if random_prob < prob:  G.AddEdge(node_i, random_node_i)
    else:                   G.AddEdge(node_i, rand_nbr_node(random_node_i))

  pyplot.scatter(*n_nodes_per_degree(G), c=COLORS[i], label=LABELS[i], alpha=0.5, edgecolors='none', norm=True)

pyplot_options()