# Importing necessary files
import graph_tools
import Dijkstra
import astar
import Bellmanford

#reading the graph from an excel file
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

#Using Dijkstra's algorithm
print()
print("Using Dijkstra's algorithm:")
shortest_distance = Dijkstra.dijkstra(graph, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distance)


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
shortest_distances, shortest_path = Bellmanford.bellman_ford(graph, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distances[end_node])
print("Shortest path:", shortest_path)


# for node, distance in shortest_distances.items():
#     print(f"{node} : {distance}")

