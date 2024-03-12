# Importing necessary files
import sys
sys.path.append('..')
import time
import Dijkstra
import astar
import Bellmanford
import graph_tools



def measuretime(graph, start_node, end_node):
    # Dijkstra's algorithm
    start_time = time.time()
    Dijkstra.dijkstra(graph, start_node, end_node)
    end_time = time.time()
    dijkstra_seconds = end_time - start_time
    dijkstra_milliseconds = dijkstra_seconds * 1000

    # A* algorithm
    start_time = time.time()    
    astar.astar(graph, start_node, end_node)
    end_time = time.time()
    astar_seconds = end_time - start_time
    astar_milliseconds = astar_seconds * 1000

    # Bellman-Ford algorithm     
    start_time = time.time()
    Bellmanford.bellman_ford(graph, start_node)
    end_time = time.time()
    bellmanford_seconds = end_time - start_time
    bellmanford_milliseconds = bellmanford_seconds * 1000

    return (dijkstra_seconds, dijkstra_milliseconds), (astar_seconds, astar_milliseconds), (bellmanford_seconds, bellmanford_milliseconds)


#Expermient 1
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

dijkstra_time, astar_time, bellmanford_time = measuretime(graph, start_node, end_node)
dijkstra_seconds, dijkstra_milliseconds = dijkstra_time
astar_seconds, astar_milliseconds = astar_time
bellmanford_seconds, bellmanford_milliseconds = bellmanford_time

print()
print(f"Dijkstra's algorithm took {dijkstra_milliseconds:.5f} milliseconds")
print(f"A* algorithm took {astar_milliseconds:.5f} milliseconds")
print(f"Bellman-Ford algorithm took {bellmanford_milliseconds:.5f} milliseconds")




