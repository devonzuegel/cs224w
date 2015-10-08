import snap, operator

def build_legends(filename, valuefn, delim=None):
  legend     = snap.TIntStrH()
  full_lines = { }
  with open(filename) as f:
    for line in f:
      tokens = line.split(delim)
      if not tokens[0].isdigit():  continue  # Ignore the first line
      key = int(tokens[0])
      legend[key]     = valuefn(tokens)
      full_lines[key] = tokens[1:]
  return (legend, full_lines)


def print_nodes(G):
  for node in G.Nodes():
    print "node id %d, out-degree %d, in-degree %d" % (node.GetId(), node.GetOutDeg(), node.GetInDeg())

def get_node_centralities(graph, centrality_measure):
  degrees = { }
  for node in graph.Nodes():
    actor_id          = node.GetId()
    degrees[actor_id] = centrality_measure(graph, actor_id)
  return degrees

def max_wcc_info(edges_file, key_file, valuefn):
  print '\nLoading edge list...'
  G      = snap.LoadEdgeList(snap.PUNGraph, edges_file, 0, 1)
  MaxWCC = snap.GetMxWcc(G)

  print '\nBuilding legend...'
  legend, full_lines = build_legends(key_file, valuefn, '\t')

  return MaxWCC, legend, full_lines
