# Importing necessary files
import sys
sys.path.append('..')
import time
import Dijkstra
import astar
import Bellmanford
import graph_tools

def update_weights(graph, weights): 
    for edge, weight in weights.items():
        node1, node2 = edge
        if node1 in graph and node2 in graph[node1]:
            graph[node1][node2] = weight
            graph[node2][node1] = weight  
    return graph



#reading the graph from an excel file
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)

print()

weights = {}
edge = input("Enter node pair (e.g: EB EFI): ").split()
if len(edge) != 2:
    raise ValueError("Invalid input")

congestion_level = float(input(f"Enter Congestion Level for edge {edge} )(Between 1 - 10)): "))
if 1 <= congestion_level <= 10:
    pass
else:
    print("Congestion level must be between 1 and 10. Please try again.")
    raise ValueError("Invalid input")

new_weight = 0.5 * congestion_level + graph[edge[0]][edge[1]]
print(f"New weight for edge {edge}: {new_weight}")

weights[(edge[0], edge[1])] = new_weight
weights[(edge[1], edge[0])] = new_weight  

updated_graph = update_weights(graph, weights)
print()
graph_tools.print_graph(updated_graph)
print()
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

#Using Dijkstra's algorithm
print()
print("Using Dijkstra's algorithm:")
print("From node", start_node, "to", end_node)
shortest_distance, shortest_path = Dijkstra.dijkstra(graph, start_node, end_node)
print("Shortest path: ", shortest_path)
print("Shortest distance: ", shortest_distance)


# #Using A* algorithm
print()
print("Using A* algorithm:")
print("From node", start_node, "to", end_node)
shortest_path, shortest_distance = astar.astar(graph, start_node, end_node)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)

# Using Bellman-Ford algorithm
print()
print("Using Bellman-Ford algorithm:")
print("Shortest distances from node", start_node, "to:")
shortest_distances,shortest_path = Bellmanford.bellman_ford(graph, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distances[end_node])
print("Shortest path:", shortest_path)