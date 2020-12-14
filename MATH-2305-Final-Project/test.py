"""Purpose of this file is to test if the algorithms/functions work properly

Args: 
    'test-graphs/G1.txt' (file name): The name of the folder/file
    that will be read
    graph_data (file): The txt file that will be used to create graph
    nodetype (bool): Used to set the nodetype to int
    G (Graph): The graph of the spanning tree
    show_graph (bool): A flag used to print MST plot
    show_cost (bool): A flag used to print cost of MST
        
return: 
    plot: a drawing of the MST if show_graph = True
    float: total cost of the MST if show_cost = True 
    
"""

import networkx as nx
from functions import *
from algorithms import prims_algorithm
from drawing import *

#Opens the file named G1.txt in read mode
graph_data = open('test-graphs/G1.txt', 'r')

#Reads the txt and creates a weighted graph, G 
G = nx.read_weighted_edgelist(graph_data, nodetype = int)

#Calls the prims_algorithm function and returns plot/cost if True
T = prims_algorithm(G, 0, show_graph = True, show_cost = True)