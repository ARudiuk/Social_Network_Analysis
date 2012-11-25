# represent links in graph
import math
#make links
def make_link(G,node1,node2):
	if node1 not in G:
		G[node1] = {}
	(G[node1])[node2]=1
	if node2 not in G:
		G[node2] = {}
	(G[node2])[node1] = 1
	return G
# find clustering coefficient
def clustering_coefficient(G,v):
	neighbors = G[v].keys()
    if len(neighbors) == 1: return -1.0
    links = 0
    for w in neighbors:
        for u in neighbors:
            if u in G[w]: links += 0.5
    return 2.0*links/(len(neighbors)*(len(neighbors)-1))
#checking connectivity/finding components of graph
def mark_component(G, node, marked):
    marked[node] = True
    total_marked = 1
    for neighbor in G[node]:
        if neighbor not in marked:
            total_marked += mark_component(G, neighbor, marked)
    return total_marked

def list_component_sizes(G):
    marked = {}
    for node in G.keys():
        if node not in marked:
            print "Component containing", node, ": ", mark_component(G, node, marked)
# Make an empty graph
a_ring ={}
G={}

n=256
side=int(math.sqrt(n))

# Add in the edges
# ring
# for i in range(n):
# 	a_ring=make_link(a_ring,i,(i+1)%n)
# grid
for i in range(side):
	for j in range(side):
		if i<side-1: make_link(G,(i,j),(i+1,j))
		if j<side-1: make_link(G,(i,j),(i,j+1))

# How many nodes?
print len(G)

# How many edges?
print sum([len(G[node]) for node in G.keys()])/2

# print G
