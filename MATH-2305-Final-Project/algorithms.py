"""This is function that will be implementing Prim's algorithm for a graph (G).

Args: 
    G (Graph): The graph of the spanning tree
    starting_vertex (int): The node that the spanning tree starts on
    show_graph (bool): A flag used to print graph
    show_cost (bool): A flah used to print cost of MST
    
Returns:
    plot: a drawing of the MST
    float: cost of spanning tree
    
"""

from functions import min_prims_edge, prims_initialize, is_spanning, cost, E
from drawing import show_weighted_graph, draw_subtree

#Function for Prim's algorithm
def prims_algorithm(G, starting_vertex, show_graph = False, show_cost = False):
    
    #Draws graph if True
    if show_graph == True:
        show_weighted_graph(G)
    T = prims_initialize(G, starting_vertex)
    
    #Draws subtree if True
    if show_graph == True:
        draw_subtree(G, T)
    
    #Adds the minimum cost edge to the graph
    while is_spanning(G, T) == False:
        e = min_prims_edge(G, T)
        T.add_edge(e[0], e[1])
        
        #Draws the MST
        if show_graph == True: 
            draw_subtree(G, T)
    
    #Returns cost if True       
    if show_cost == True:
        c = sum([cost(G, e) for e in E(T)])
        print(f'The cost of this spanning tree is: {c}')
    return T