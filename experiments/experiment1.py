import sys
sys.path.append('..')
import numpy as np
import random
import time
import Dijkstra
import dac
import Bellmanford
import matplotlib.pyplot as plt
import graph_tools
import pandas as pd

def generate_random_adjacency_matrix(num_nodes, max_distance=10):
    # Preallocate the adjacency matrix
    adjacency_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    # Fill the upper triangular part of the matrix (excluding the diagonal)
    for i in range(num_nodes):
        adjacency_matrix[i, i+1:] = np.random.randint(0, max_distance, size=num_nodes-i-1)

    # Fill the lower triangular part of the matrix (excluding the diagonal) by transposing and filling again
    adjacency_matrix += adjacency_matrix.T

    return adjacency_matrix


def adjacency_matrix_to_graph(adjacency_matrix):
    # Convert the adjacency matrix to a graph dictionary
    graph = {}
    num_nodes = len(adjacency_matrix)
    for i in range(num_nodes):
        neighbors = {}
        for j in range(num_nodes):
            if adjacency_matrix[i][j] != 0:
                neighbors[str(j)] = adjacency_matrix[i][j]
        graph[str(i)] = neighbors
    return graph

def measuretime(graph, start_node, end_node, num_runs=10):
    dijkstra_times = []
    dac_times = []
    bellmanford_times = []

    for _ in range(num_runs):
        # Dijkstra's algorithm
        start_time = time.perf_counter()
        Dijkstra.dijkstra(graph, start_node, end_node)
        end_time = time.perf_counter()
        dijkstra_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        # Divide and Conquer algorithm
        start_time = time.perf_counter()    
        dac.divide_and_conquer(graph, start_node, end_node)
        end_time = time.perf_counter()
        dac_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        # Bellman-Ford algorithm     
        start_time = time.perf_counter()
        Bellmanford.bellman_ford(graph, start_node, end_node)
        end_time = time.perf_counter()
        bellmanford_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

    return (dijkstra_times, dac_times, bellmanford_times)

# Generate random graphs for different sizes
sizes = [16, 32, 64, 128, 512, 1024]
random_graphs = {}
matrix_sizes = []

# Lists to store the average time taken for each algorithm
dijkstra_avg_times = []
dac_avg_times = []
bellmanford_avg_times = []

file_path = 'adjmatrix.xlsx'
graph = graph_tools.read_excel_file(file_path)
graph_tools.print_graph(graph)

for size in sizes:
    adjacency_matrix = generate_random_adjacency_matrix(size)
    random_graphs[size] = adjacency_matrix_to_graph(adjacency_matrix)

    # Lists to store time taken for each run for each algorithm
    dijkstra_times_all = []
    dac_times_all = []
    bellmanford_times_all = []

    for _ in range(10):  # 10 runs for each size
        start_node = random.choice(list(random_graphs[size].keys()))
        end_node = random.choice(list(random_graphs[size].keys()))
        dijkstra_times, dac_times, bellmanford_times = measuretime(random_graphs[size], start_node, end_node)
        
        # Calculate the average time for each algorithm
        dijkstra_avg_time = sum(dijkstra_times) / len(dijkstra_times)
        dac_avg_time = sum(dac_times) / len(dac_times)
        bellmanford_avg_time = sum(bellmanford_times) / len(bellmanford_times)

        dijkstra_avg_times.append(dijkstra_avg_time)
        dac_avg_times.append(dac_avg_time)
        bellmanford_avg_times.append(bellmanford_avg_time)
        matrix_sizes.append(size)

    # Print the time taken for each algorithm
    print(f"For graph size {size}:")
    print(f"Dijkstra's algorithm: {dijkstra_avg_time:.5f} milliseconds")
    print(f"Divide and Conquer algorithm: {dac_avg_time:.5f} milliseconds")
    print(f"Bellman-Ford algorithm: {bellmanford_avg_time:.5f} milliseconds")
    print()


# Plotting
plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, dijkstra_avg_times, label="Dijkstra")
plt.plot(matrix_sizes, dac_avg_times, label="Divide and Conquer")
plt.plot(matrix_sizes, bellmanford_avg_times, label="Bellman-Ford")
plt.xlabel('Matrix Size')
plt.ylabel('Average Time (milliseconds)')
plt.title('Algorithm Performance vs. Matrix Size')
plt.legend()
plt.grid(True)
plt.show()