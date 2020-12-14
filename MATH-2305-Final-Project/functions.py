"""Creates multiple helper functions that will later be called to help execute
   Prim's algorithm
   
Args: 
    graph (Graph): The graph of the spanning tree
    v (int): Used to initiate a specific vertex
    subgraph (subgraph): used to return subgraph of the graph
    G (Graph): Used to read data from the Graph
    e (edges): Used to give edge coordinates for the cost function
    T (node): The node that the MST begins with

Returns: 
    set: graph nodes
    set: graph edges
    string: to indicate 'Error vertex not found'
    node: starting node
    bool: compares value to V(graph) and V(subgraph)
    float: weight of the edge according to the vertices
    edges: all the possible edges
    vertices: the vertices of the minimum cost edge
    
"""

import networkx as nx

#Creates a set of all vertices
def V(graph):
    return set(graph.nodes())

#Creates a set of all the edges
def E(graph):
    return set(graph.edges())

#Initialize the node that the tree will begin at
def prims_initialize(graph, v):
    if v not in V(graph):
        return 'Error vertex not found'
    else:  
        T = nx.Graph()
        T.add_node(v)
        return T

#Determines is the tree is spanning    
def is_spanning(graph, subgraph):
    return V(graph) == V(subgraph)

#Determines the weight of each edge
def cost(G, e):
    return G[e[0]][e[1]]['weight']

#Determines all the valid edges for each vertex
def possible_edges(G, T):
    temp_edges = list(G.edges(V(T)))
    return [e for e in temp_edges if e[0] not in V(T) or e[1] not in V(T)]

#Determines the minimum edge weight for all possible edges
def min_prims_edge(G, T):     
    possible = possible_edges(G, T)
    minimum = possible[0]
    for a in possible:
        if cost(G, a) < cost(G, minimum):
            minimum = a
    return minimum