import snap
from util import *

#### PART A ##########################################################################
# For the (undirected) graph in foodie.txt in edge-list format, and the parameters p = 0.5,
# q = (1.2, 1.1, 1.2, 1.1, 1.2, 0.9, 1.2, 0.9), report the rankings for k = 1, 2, 3, inf as rows of a matrix
# R, where Rki denotes the index of the i-th top node after k rounds. Hint: for this problem you
# will have to work with the adjacency matrix A of the graph. You are free to use any software
# to perform the necessary calculations e.g. Matlab, Numpy, R.

print 'Loading edge list...'
G      = snap.LoadEdgeList(snap.PUNGraph, 'foodie.txt', 0, 1)
labels = { n.GetId():n.GetId() for n in G.Nodes() }

# print 'Drawing graph...'
# snap.DrawGViz(G, snap.gvlDot, 'foodie.png', 'Chef graph', labels)


def scores_after_finite_rounds(Q0, A, p, d, k):

  def inner(j):
    scalar = (1.0 - p) / d
    return (A*scalar)**j

  initial_plates = p*Q0
  shared_plates  = Q0 * sum( map(lambda x: inner(x), range(1, k)) )

  return initial_plates + shared_plates


# NOTE: physicsforums.com/threads/infinite-sum-of-matrices.288325/
def scores_after_infinite_rounds(Q0, A, p, d):

  scalar =  (1.0 - p) / d
  def myfunc(a):
    x      = a * scalar
    return 1.0 / (1 - x)

  vecfunc = numpy.vectorize(myfunc)
  return Q0*vecfunc(A) + p*Q0
  # return Q0 * (1 - A * scalar)**(-1) + p*Q0

############################################################################################

A  = build_adjacency_matrix(G)
Q0 = numpy.matrix([1.2, 1.1, 1.2, 1.1, 1.2, 0.9, 1.2, 0.9])
p  = 0.5
d  = numpy.sum(A[:,0])

for i in [1, 2, 3]:
  print 'Scores after k = %d rounds:' % i
  print scores_after_finite_rounds(Q0, A, p, d, k = i)

print 'Scores after k = infinity rounds:'
print scores_after_infinite_rounds(Q0, A, p, d)

