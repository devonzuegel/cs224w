import snap

G = snap.LoadEdgeList(snap.PUNGraph, './data/epinion_signed.txt', 0, 1)
print snap.GetTriads(G)