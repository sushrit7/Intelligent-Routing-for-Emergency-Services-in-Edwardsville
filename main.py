#Team Everest
#CS 456
#Final Project


import graph_tools
import Dijkstra
import dac
import Bellmanford
import pandas as pd

#reading the graph from an excel file
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

#Using Dijkstra's algorithm
print()
print("Using Dijkstra's algorithm:")
print("From node", start_node, "to", end_node)
shortest_distance, shortest_path = Dijkstra.dijkstra(graph, start_node, end_node)
print("Shortest path: ", shortest_path)
print("Shortest distance: ", shortest_distance)

# Using Bellman-Ford algorithm
print()
print("Using Bellman-Ford algorithm:")
print("From node", start_node, "to", end_node)
shortest_distances, shortest_path = Bellmanford.bellman_ford(graph, start_node, end_node)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distances[end_node])

#Using Divide and Conquer algorithm
print()
print("Using Divide and Conquer algorithm:")
shortest_path, shortest_distance = dac.divide_and_conquer(graph, start_node, end_node)
print("Shortest path:", shortest_path)
print("Shortest distance:", shortest_distance)
