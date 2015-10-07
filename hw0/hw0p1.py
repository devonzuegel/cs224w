import snap


def build_legend():
  legend = snap.TIntStrH()
  with open('ingredient_key.txt') as f:
    for line in f:
      tokens = line.split()
      if tokens[0] == '#':  continue   # Ignore the first line
      key = int(tokens[0])
      legend[key] = ' '.join(tokens[1:])
  return legend

print 'Loading edge list...'
G = snap.LoadEdgeList(snap.PNGraph, 'ingredient_substitutes.txt', 0, 1)

print 'Building legend...'
legend = build_legend()

print 'Drawing graph...'
snap.DrawGViz(G, snap.gvlDot, 'G.png', 'G', legend)

# snap.PlotInDegDistr(G, 'BLAH', 'BLAH in degree')