import matplotlib.pyplot as plt
import networkx as nx
import numpy as np



# Adjacency matrix
adj_matrix = np.array([
    [0, 1, 4, 0],
    [1, 0, 2, 5],
    [4, 2, 0, 1],
    [0, 5, 1, 0]
])

salesman = np.array([
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
])

qn1 = np.array([
    # 0 1 2 3 4 5 6 7 8 
     [0,4,0,0,0,0,0,8,0],
     [4,0,8,0,0,0,0,11,0],
     [0,8,0,7,0,4,0,0,2],
     [0,0,7,0,9,14,0,0,0],
     [0,0,0,9,0,10,0,0,0],
     [0,0,4,14,10,0,2,0,0],
     [0,0,0,0,0,2,0,1,6],
     [8,11,0,0,0,0,1,0,7],
     [0,0,2,0,0,0,6,7,0]
])

# Create a graph from the adjacency matrix
G = nx.from_numpy_array(qn1)

# Draw the graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()