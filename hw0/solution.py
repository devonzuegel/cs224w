from snap import *

print "###### PROBLEM 1 #######"
G = LoadEdgeList(PNGraph, "ingredient_substitutes.txt", 0, 1)
SCC = GetMxScc(G)
print "1.a"
print "Size of largest SCC:",SCC.GetNodes()
print "% of nodes in largest SCC:",SCC.GetNodes() * 100.0/G.GetNodes()

print "\n1.b"
id_to_ingredients = {}
ingredients_to_id = {}
with open("ingredient_key.txt") as f:
  rows = [l.strip().split("\t") for l in f]
  rows = rows[1:]

  id_to_ingredients = {int(r[0]):r[1] for r in rows}
  ingredients_to_id = {r[1]:int(r[0]) for r in rows}

cocoa_id = ingredients_to_id["cocoa powder"]
distance = 0
distant_nodes = None
nodes = TIntV()

while True:
  num_nodes = GetNodesAtHop(G, cocoa_id, distance, nodes, False)
  if num_nodes == 0:
    break
  distant_nodes = [i for i in nodes]
  distance += 1
print "Ingredients most distant from cocoa powder: ",[id_to_ingredients[i] for i in distant_nodes]
print "Distance:",distance - 1

print "\n1.c"
PRankH = TIntFltH()
#G = LoadEdgeList(PUNGraph, "ingredient_substitutes.txt", 0, 1)
GetPageRank(G, PRankH)
pagerank = [(key, PRankH[key]) for key in PRankH]
pagerank = sorted(pagerank, key=lambda x:-x[1])
print "Node with highest pagerank"
print id_to_ingredients[pagerank[0][0]],":",pagerank[0][1]
print "node id:",pagerank[0][0]


print "\n\n###### PROBLEM 2 #######"
G = LoadEdgeList(PNEANet, "fish_trade_edges.txt", 0, 1)
with open("fish_trade_countries_key.txt") as f:
  rows = [l.strip().split('\t') for l in f]
  rows = rows[1:]
  country_map = {int(t[0]):t[1][1:-1] for t in rows}

print "2.a"
reciprocal = [G.IsEdge(E.GetDstNId(), E.GetSrcNId()) for E in G.Edges()]
print "Percentage reciprocal:",sum(reciprocal) * 100.0 / len(reciprocal)

print "\n2.b"
in_degrees = [(n.GetId(), n.GetInDeg()) for n in G.Nodes()]
in_degrees = sorted(in_degrees, key=lambda x:-x[1])
print "Top 10 countries by in-degree:"
print [country_map[nid] for (nid, indegree) in in_degrees[:10]]

print "\n2.c"
with open("fish_trade_edges.txt") as f:
  rows = [l.strip().split() for l in f]
  rows = rows[1:]
  weights = {(int(t[0]), int(t[1])): float(t[2]) for t in rows}
sum_weights = [(node.GetId(), sum([weights[(node.GetId(), node.GetOutNId(i))] for i in range(node.GetOutDeg())])) for node in G.Nodes()]
sum_weights = sorted(sum_weights, key=lambda x:-x[-1])
print "Top countries (by export weight)"
for nid, weight in sum_weights[:6]:
  print "\t",country_map[nid], weight

print "\n2.d"
out_degrees = {n.GetId():n.GetOutDeg() for n in G.Nodes()}
in_degrees = {key:value for (key, value) in in_degrees}
differences = [(key, abs(in_degrees[key] - out_degrees[key])) for key in out_degrees]
differences = sorted(differences, key=lambda x:-x[1])
print "Country with greatest difference:",country_map[differences[0][0]]