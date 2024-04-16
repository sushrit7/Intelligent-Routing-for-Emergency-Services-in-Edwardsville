# Importing necessary files
import sys
sys.path.append('..')
import time
import Dijkstra
import dac
import Bellmanford
import graph_tools

def measuretime(graph, start_node, end_node, num_runs=10):
    dijkstra_times = []
    astar_times = []
    bellmanford_times = []

    for _ in range(num_runs):
        # Dijkstra's algorithm
        start_time = time.perf_counter()
        Dijkstra.dijkstra(graph, start_node, end_node)
        end_time = time.perf_counter()
        dijkstra_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        # A* algorithm
        start_time = time.perf_counter()    
        dac.divide_and_conquer(graph, start_node, end_node)
        end_time = time.perf_counter()
        astar_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        # Bellman-Ford algorithm     
        start_time = time.perf_counter()
        Bellmanford.bellman_ford(graph, start_node, end_node)
        end_time = time.perf_counter()
        bellmanford_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    return (dijkstra_times, astar_times, bellmanford_times)

#Expermient 1
file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)
start_node = input("Enter the starting node: ")
end_node = input("Enter the ending node: ")

dijkstra_times, astar_times, bellmanford_times = measuretime(graph, start_node, end_node)

print()
print(f"Dijkstra's algorithm took average {sum(dijkstra_times) / len(dijkstra_times):.5f} milliseconds")
print(f"Divide and Conquer algorithm took average {sum(astar_times) / len(astar_times):.5f} milliseconds")
print(f"Bellman-Ford algorithm took average {sum(bellmanford_times) / len(bellmanford_times):.5f} milliseconds")
