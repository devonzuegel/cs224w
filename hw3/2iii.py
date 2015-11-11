import matplotlib.pyplot as plt
import snap
import numpy as np

N_NODES = 10 * 1000
PROB    = 2.0 / N_NODES
N_EDGES = (N_NODES - 1) * N_NODES * PROB / 2
Q0_VALS = [ (10**i) * (1.0 / N_NODES) for i in xrange(0, 4) ]
MAX_K   = 30

def init():
  G = snap.GenRndGnm(snap.PUNGraph, int(N_NODES), int(N_EDGES))
  rioting = [True if x==1 else False for x in np.random.binomial(1, PROB, N_NODES)]
  return [], G, rioting

def simulate(q0):
  set_sizes, G, rioting = init()
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

for _q0 in Q0_VALS:
  # diameters = [simulate(_q0) for _ in range(40)]
  # print diameters

  # connected = [simulate(_q0) for _ in range(40)]
  # print sum(connected), 'of the 40 graphs with q_0 =', _q0, 'were connected'

  averages = np.zeros(MAX_K)
  for _ in range(40):    averages += simulate(_q0)
  averages /= 1.0 * MAX_K

  plt.plot(range(0, MAX_K), averages, label = _q0)
  plt.legend()
  plt.savefig('./images/2iii-plot.png')