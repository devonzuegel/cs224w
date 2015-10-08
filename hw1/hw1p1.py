import snap

#### PART A ##########################################################################
# Generate an undirected graph with N = 20000 nodes, using the following iterative
# procedure:
#  - Begin with three nodes 0, 1, 2, with edges (0, 1), (1, 2), (2, 0).
#  - For each additional node n:
#     + Select an existing node o uniformly at random
#     + With probability p, add edge (n, o); otherwise, select uniformly at random
#       one of o’s neighbors, o′, and add edge (n,o′).
# Plot the normalized degree distributions for p = [0.0,0.2,0.4,0.5,0.8,1.0], all
# superimposed onto the same log-log graph. Include a legend.

def partA():
  raise Exception


#### PART B ##########################################################################
# (In the writeup)


#### PART C ##########################################################################
# Using the plfit library, compute the estimated xmin and α parameters using the
# plfit command for the graph described in (a) for p = 0.2. Plfit uses
# maximum-likelihood estimation (MLE) to compute the parameters. What are the
# results? What results would you expect, and what factors may contribute to any
# differences?

def partC():
  raise Exception


#### PART D ##########################################################################
# Generate (without using existing one-line library methods) a Erdos-Renyi random
# graph with N = 2000 nodes, with probability p = 0.1 of an edge existing between any
# two nodes, and plot the resulting normalized degree distribution. What type of
# distribution is the degree distribution? Briefly explain why the distribution differs
# from the graphs generated in part (a).
#
#  1. Graph has n nodes
#  2. For each pair of possible nodes (a,b) (b, c), (d, e) etc, for example, we do a
#     coin toss with probability p.
#  3. If the coin toss is 1, we connect those two edges, if not, we don't.

def partD():
  raise Exception