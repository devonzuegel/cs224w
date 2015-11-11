import matplotlib.pyplot as plt
import snap, math
import numpy as np

N_NODES = 10 * 1000
Q0      = 1.0 / N_NODES
PROBS   = [(p * math.log10(N_NODES) * 1.0 / N_NODES) for p in [2, 10, 100]]
MAX_K   = 7

def init(prob):
  n_edges = (N_NODES - 1) * N_NODES * prob / 2
  G = snap.GenRndGnm(snap.PUNGraph, int(N_NODES), int(n_edges))
  rioting = [True if x==1 else False for x in np.random.binomial(1, prob, N_NODES)]
  return [], G, rioting

def simulate(prob, q0):
  set_sizes, G, rioting = init(prob)
  for i in range(MAX_K):
    already_rioting = rioting
    for node_id in range(len(rioting)):

      for nbr_id in [_id for _id in G.GetNI(node_id).GetOutEdges()]:
        if already_rioting[nbr_id]:
          rioting[node_id] = True
          break
    set_sizes += [ sum(rioting) ]

  # return snap.IsConnected(G)

  # return snap.GetBfsFullDiam(G, N_NODES / 10)

  growth = []
  for i, val in enumerate(set_sizes):
    growth += [ 0 if (i == MAX_K - 1 or i == 0) else (set_sizes[i] - set_sizes[i - 1])/(N_NODES * 1.0) ]
  return growth

for prob in PROBS:
  # diameters = [simulate(_q0) for _ in range(40)]
  # print diameters

  plt.plot(range(0, MAX_K), simulate(prob, Q0), label = ('p = %s' % prob))
  plt.legend()
  plt.savefig('./images/2iv-plot.png')