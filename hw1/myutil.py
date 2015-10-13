import snap
import random
from matplotlib import pyplot

TOTAL_N_NODES = 2000
COLORS = ['red', 'blue', 'green', 'purple', 'orange', 'black']
LABELS = ['0.0', '0.2',  '0.4',   '0.6',    '0.8',    '1.0']

def set_up_graph():
  graph = snap.TUNGraph.New()
  for n in [0,1,2]:                 graph.AddNode(n)
  for e in [(0,1), (1,2), (2,0)]:   graph.AddEdge(e[0], e[1])
  return graph

def rand_nbr_node(graph, node_index):
  node        = graph.GetNI(node_index)
  n_neighbors = node.GetDeg()
  rand_nbr_i  = random.randint(0, n_neighbors - 1)
  return node.GetNbrNId(rand_nbr_i)

def build_degrees_dict(graph):
  degrees_dict = {}
  for node_i in range(0, TOTAL_N_NODES):
    deg_n = graph.GetNI(node_i).GetDeg()
    if deg_n in degrees_dict:   degrees_dict[deg_n] += 1
    else:                       degrees_dict[deg_n] = 1
  return degrees_dict

def n_nodes_per_degree(graph):
  degrees_dict = build_degrees_dict(graph)
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

