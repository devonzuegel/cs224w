from collections import defaultdict

def node(n):    return n[0]
def degree(n):  return n[1]

adjacencies = defaultdict(dict)
with open('data/epinion_signed.txt') as f:
  for line in f:
    tokens = line.split()
    if not tokens[0].isdigit():   continue
    src, dst, sign = tokens
    adjacencies[src][dst] = sign
    adjacencies[dst][src] = sign

ordered_nodes = [(a, len(adjacencies[a])) for a in adjacencies]
ordered_nodes.sort(key = lambda tup: degree(tup), reverse = True)

A         = defaultdict(list)
triads    = []

# def get_triads():
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
      A[t[0]] += [node(s)]

print len(triads)