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
            print "Component containing", node, ": ", mark_component(G, node, marked
#check connectivity
def check_connection(G, v1, v2):
    marked = {}
    mark_component(G, v1, marked)
    return v2 in marked
#find path between two nodes, breadth first
def path(G, v1, v2):
    #distance_from_start = {}
    path_from_start = {} # modification
    open_list = [v1]
    #distance_from_start[v1] = 0
    path_from_start[v1] = [v1] # modification
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            #if neighbor not in distance_from_start:
            if neighbor not in path_from_start: # modification
                #distance_from_start[neighbor] = distance_from_start[current] + 1
                path_from_start[neighbor] = path_from_start[current] 
                                              + [neighbor] # modification
                #if neighbor == v2: return distance_from_start[v2]
                if neighbor == v2: return path_from_start[v2] # modification
                open_list.append(neighbor)
    return False
#centrality
def centrality(G, v):
    distance_from_start = {}
    open_list = [v]
    distance_from_start[v] = 0
    while len(open_list) > 0:
        current = open_list[0]
        del open_list[0]
        for neighbor in G[current].keys():
            if neighbor not in distance_from_start:
                distance_from_start[neighbor] = distance_from_start[current] + 1
                open_list.append(neighbor)
    return float(sum(distance_from_start.values()))/len(distance_from_start)
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
