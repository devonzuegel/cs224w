from myutil import *
import plfit

prob  = 0.2
graph = set_up_graph()

for node_i in range(3, TOTAL_N_NODES):
    random_node_i = random.randint(0, node_i - 1)
    graph.AddNode(node_i)

    random_prob   = random.uniform(0, 1)
    if random_prob < prob:  graph.AddEdge(node_i, random_node_i)
    else:                   graph.AddEdge(node_i, rand_nbr_node(graph, random_node_i))

degrees = [graph.GetNI(i).GetDeg() for i in range(0, TOTAL_N_NODES)]
fit     = plfit.plfit(degrees)

print 'xmin  = %s' % fit._xmin
print 'alpha = %s' % fit._alpha