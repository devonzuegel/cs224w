import snap, operator
from util import *

EDGES_FILE = 'imdb_actor_edges.tsv'
KEY_FILE   = 'imdb_actors_key.tsv'

def valuefn(tokens):  return tokens[1]

#### INITIALIZATION ##################################################################

MaxWCC, legend, full_lines = max_wcc_info(EDGES_FILE, KEY_FILE, valuefn)

#### PART A ##########################################################################
# Degree centrality for all actors in the LWCC and list the 20 actors with highest
# degree. Referring to the number of movies of made by these actors vs. others, how
# do you explain their high degree?

def partA():
  print "\nCalculating nodes' degree centrality..."
  degrees        = get_node_centralities(MaxWCC, snap.GetDegreeCentr)
  sorted_degrees = sorted(degrees.items(), key=operator.itemgetter(1))

  print '\n20 ACTORS WITH THE HIGHEST DEGREE CENTRALITY:'
  for i, keyval in enumerate(reversed(sorted_degrees[-20:])):
    actor_id, degree = keyval
    actor_name       = legend[actor_id]
    number_of_films  = full_lines[actor_id][1]
    main_genre       = full_lines[actor_id][2]
    print ' #%d - %s:   %s    %s    %s' % (i+1, actor_name, degree, number_of_films, main_genre)

# partA()    # Commented out because this a little while to run

#### PART B ##########################################################################
# Betweenness centrality for all actors in the LWCC and list the 20 actors with the
# highest betweenness centrality. Only a couple of actors with top degree centrality
# remain on this list. Referring to the distribution of genres these actors acted in,
# explain the discrepancy between degree- and betweenness centrality for these actors.

def partB():
  print "\nCalculating nodes' betweenness centrality..."
  Nodes = snap.TIntFltH()
  Edges = snap.TIntPrFltH()
  snap.GetBetweennessCentr(MaxWCC, Nodes, Edges, 1.0)

  print '\n20 ACTORS WITH THE HIGHEST BETWEENNESS CENTRALITY:'
  betweennesses        = { node_id: Nodes[node_id] for node_id in Nodes }
  sorted_betweennesses = sorted(betweennesses.items(), key=operator.itemgetter(1))
  for i, keyval in enumerate(reversed(sorted_betweennesses[-20:])):
    actor_id, betweenness  = keyval
    actor_name           = legend[actor_id]
    number_of_films      = full_lines[actor_id][1]
    print ' #%d - %s:   %s    %s' % (i+1, actor_name, betweenness, number_of_films)

# partB()  # Commented out because this takes forever to run...!

#### PART C ##########################################################################
# Closeness centrality for all actors in the LWCC and list the 20 actors with the highest
# closeness. Referring to the figure 1 explain why the actors with top closeness tend to
# overlap so little with the two previous lists. Note that the figure shows a large pink
# "documentary" clump where many of the high closeness actors are located. It's a bit
# puzzling, but many of these high- closeness actors do seem to have been involved in
# documentary serials or "the making-of" documentaries. We've excluded "Documentary" and
# "Short" from being candidates for an actor's main genre, but have used them to color the
# figure (e.g. Tom Hanks and Whoopi Goldberg are somehow in over 30 documentaries during
# the time span of the dataset).

def partC():
  print "\nCalculating nodes' closeness centrality..."
  closenesses        = get_node_centralities(MaxWCC, snap.GetClosenessCentr)
  sorted_closenesses = sorted(closenesses.items(), key=operator.itemgetter(1))

  print '\n20 ACTORS WITH THE HIGHEST CLOSENESS CENTRALITY:'
  for i, keyval in enumerate(reversed(sorted_closenesses[-20:])):
    actor_id, closeness = keyval
    actor_name          = legend[actor_id]
    number_of_films     = full_lines[actor_id][1]
    main_genre          = full_lines[actor_id][2]
    print ' #%d - %s:   %s    %s    %s' % (i+1, actor_name, closeness, number_of_films, main_genre)

# partC()
