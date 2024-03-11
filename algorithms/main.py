import graph_tools
import Dijkstra
import astar
import Bellmanford

# Rest of the code remains the same
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

#Using Dijkstra's algorithm
print("Using Dijkstra's algorithm:")
print("Shortest distances from node", start_node, "to:")
shortest_distance = Dijkstra.dijkstra(graph, start_node, end_node)
print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distance)


# #Using A* algorithm
# print("Using A* algorithm:")
# print("Shortest distances from node", start_node, "to:")
# # Create an R-tree for spatial indexing
# rtree = astar.create_rtree(graph)

# # Apply divide_and_conquer approach to find the shortest path and distance
# shortest_path, shortest_distance = astar.divide_and_conquer(graph, rtree, rtree.bounds, start_node, end_node)
# print("Shortest path:", shortest_path)
# print("Shortest distance:", shortest_distance)

# Using Bellman-Ford algorithm
print("Using Bellman-Ford algorithm:")
print("Shortest distances from node", start_node, "to:")
shortest_distances = Bellmanford.bellman_ford(graph, start_node)
for node, distance in shortest_distances.items():
    print(f"{node} : {distance}")

