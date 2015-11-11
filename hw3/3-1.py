import snap

g1 = snap.LoadEdgeList(snap.PUNGraph, './data/g1.edgelist.txt', 0, 1)
g2 = snap.LoadEdgeList(snap.PUNGraph, './data/g2.edgelist.txt', 0, 1)

A, B     = 0, 1
N_DAYS   = 7
N_VOTERS = 10 * 1000

def count_up_friends(curr_state, g, voter):
    num_A_friends = 0
    num_B_friends = 0
    for connection in g.GetNI(voter).GetInEdges():
        if curr_state[connection] == A:      num_A_friends += 1
        if curr_state[connection] == B:      num_B_friends += 1
    return num_A_friends, num_B_friends

def initialize():
    state = (N_VOTERS / 10) * (4 * [B] + 4 * [A] + 2 * [None])
    C = A
    return C, state

def simulation(g):
    C, initial_state = initialize()
    curr_state = list(initial_state)

    for curr_round in range(0, N_DAYS):
        for voter in range(0, N_VOTERS):
            if initial_state[voter] is None:
                num_A_friends, num_B_friends = count_up_friends(curr_state, g, voter)

                if   num_A_friends > num_B_friends:     curr_state[voter] = A
                elif num_A_friends < num_B_friends:     curr_state[voter] = B
                else:
                    curr_state[voter] = C
                    C = 1 - C  # Alternate

    margin = curr_state.count(A) - curr_state.count(B)
    winner = 'A' if margin >= 0 else 'B'

    print 'The election winner is %s, wins by a margin of %d votes' % (winner, abs(margin))

print '\n--- Simulation #1 -------------------------------------------------------------\n'
simulation(g1)
simulation(g2)
print