import snap


def print_nodes(G):
  for node in G.Nodes():
    print "node id %d, out-degree %d, in-degree %d" % (node.GetId(), node.GetOutDeg(), node.GetInDeg())

def build_legend(filename):
  legend = snap.TIntStrH()
  with open(filename) as f:
    for line in f:
      tokens = line.split()
      if not tokens[0].isdigit():  continue   # Ignore the first line
      key = int(tokens[0])
      legend[key] = ' '.join(tokens[1:])
  return legend

print 'Loading edge list...'
G = snap.LoadEdgeList(snap.PNGraph, 'ingredient_substitutes.txt', 0, 1)
print_nodes(G)

print 'Building legend...'
legend = build_legend('ingredient_key.txt')
print len(legend)

print 'Drawing graph...'
snap.DrawGViz(G, snap.gvlDot, 'G.png', 'G', legend)

# # snap.PlotInDegDistr(G, 'BLAH', 'BLAH in degree')