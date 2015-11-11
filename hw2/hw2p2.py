import operator
from collections import defaultdict


## PART A

from collections import defaultdict

def node(n):    return n[0]
def degree(n):  return n[1]

def get_triads(ordered_nodes, adjacencies):
  A         = defaultdict(list)
  triads    = []
  # The following code was inspired by the following paper:
  #   "i11www.iti.uni-karlsruhe.de/extra/publications/sw-fclt-05_wea.pdf".
  for s in ordered_nodes:
    for t in adjacencies[node(s)]:
      if node(s) == node(t):   continue    # ignore if self
      if degree(s) > len(adjacencies[node(t)]):
        intersection = set( A[node(t)] ).intersection( A[node(s)] )
        for v in intersection:
          triad = (node(s), node(t), v)
          triads += [triad]
        A[node(t)] += [node(s)]

  return triads

def get_adjacencies(filename):
  adjacencies = defaultdict(list)
  with open(filename) as f:
    for line in f:
      tokens = line.split()
      if not tokens[0].isdigit():   continue
      src, dst, sign = tokens
      adjacencies[src] += [(dst, sign)]
      adjacencies[dst] += [(src, sign)]
  return adjacencies

def get_ordered_nodes(adjacencies):
  ordered_nodes = [(a, len(adjacencies[a])) for a in adjacencies]
  ordered_nodes.sort(key = lambda tup: degree(tup), reverse = True)
  return ordered_nodes

adjacencies   = get_adjacencies('data/epinion_signed.txt')
ordered_nodes = get_ordered_nodes(adjacencies)
triads        = get_triads(ordered_nodes, adjacencies)
print '# of triads = %s' % len(triads)


print 'Calculating triad type counts...'

#  6 = all positive;  2 = two positive one negative
# -6 = all negative; -2 = two negative one positive
triad_types = { 6:0, 2:0, -2:0, -6:0 }

for triad in triads:
  triad_type = 0
  for node in triad:
    for node_j in triad:
      if node == node_j: continue
      sign = dict(adjacencies[node])[node_j]
      triad_type += int(sign)
  triad_types[triad_type] += 1

print triad_types

## PART B

num_pos, num_neg = 0, 0

with open('./data/epinion_signed.txt') as f:
  for line in f:
    tokens = line.split()
    if not tokens[0].isdigit():    continue
    _, _, sign = tokens
    if int(sign) > 0:     num_pos += 1
    elif int(sign) < 0:   num_neg += 1

print num_pos
print num_neg