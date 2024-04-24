# Importing necessary files
import sys
sys.path.append('..')
import time
import Dijkstra
import dac
import Bellmanford
import graph_tools
import random
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

def update_weights(graph, weights): 
    for edge, weight in weights.items():
        node1, node2 = edge
        if node1 in graph and node2 in graph[node1]:
            graph[node1][node2] = weight
            graph[node2][node1] = weight  
    return graph

if __name__ == "__main__":
    #reading the graph from an excel file
    file_path = 'adjmatrix.xlsx'
    graph = graph_tools.read_excel_file(file_path)
    graph_tools.print_graph(graph)

    print()

    updated_graph = graph
    num = 5
    congestion_level =[20, 40, 60, 80, 100]
    
    for n in range(num):
    # List of edges
    # Randomly choose a pair of nodes
        edges = ["EB", "EFI", "EFII", "EFIII", "EPD", "MPD", "SPD", "AH", "CVA", "RA", "PA", "SA", "EA"]
        edge = random.sample(edges, 2)
        print("Randomly chosen pair of nodes:", edge)

        weights = {}
        # edge = input("Enter node pair (e.g: EB EFI): ").split()
        # if len(edge) != 2:
        #     raise ValueError("Invalid input")
        for e in edge:
            print(f"Edge: {e}")
        # congestion_level = float(input(f"Enter Congestion Level for edge {edge} )(Between 1 - 10)): "))
        # if 1 <= congestion_level <= 10:
        #     pass
        # else:
        #     print("Congestion level must be between 1 and 10. Please try again.")
        #     raise ValueError("Invalid input")

        new_weight = 0.5 * congestion_level[n] + graph[edge[0]][edge[1]]
        print(f"New weight for edge {edge}: {new_weight}")

        weights[(edge[0], edge[1])] = new_weight
        weights[(edge[1], edge[0])] = new_weight  

        updated_graph = update_weights(graph, weights)

    print()
    graph_tools.print_graph(updated_graph)
    print()
    residential_areas = ["EB", "AH", "CVA", "RA", "PA", "SA", "EA"]
    emergency_services = ["EFI", "EFII", "EFIII", "EPD", "MPD", "SPD"]

    # Create empty lists to store results
    results = []

    # Assuming you have the results stored in lists like below
    # where shortest_distances_dijkstra, shortest_distances_dac, and shortest_distances_bellmanford
    # contain tuples (from_node, to_node, shortest_distance) for each algorithm

    for area in residential_areas:
        for emergency_service in emergency_services:
            # Assuming you have calculated shortest distances for each algorithm
            shortest_distance_dijkstra, shortest_path_dijkstra = Dijkstra.dijkstra(updated_graph, emergency_service, area)
            shortest_path_dac, shortest_distance_dac = dac.divide_and_conquer(updated_graph, emergency_service, area)
            shortest_distances_bellmanford, shortest_path_bellmanford = Bellmanford.bellman_ford(updated_graph, emergency_service, area)

            # Append the results to the list
            results.append((area, emergency_service, shortest_distance_dijkstra, shortest_distance_dac, shortest_distances_bellmanford[area], shortest_path_dijkstra, shortest_path_dac, shortest_path_bellmanford))

    # Convert the list of results into a DataFrame
    df = pd.DataFrame(results, columns=["From Node", "To Node", "Dijkstra_distance", "Divide_and_Conquer_distance", "Bellman-Ford_distance","Dijkstra_path","Divide_and_Conquer_path","Bellman-Ford_path"])

    # Save the DataFrame to an Excel file
    df.to_excel("shortest_distances.xlsx", index=False)


    # start_node = input("Enter the starting node: ")
    # end_node = input("Enter the ending node: ")

    #Using Dijkstra's algorithm
    # print()
    # print("Using Dijkstra's algorithm:")
    # print("From node", start_node, "to", end_node)
    # shortest_distance, shortest_path = Dijkstra.dijkstra(graph, start_node, end_node)
    # print("Shortest path: ", shortest_path)
    # print("Shortest distance: ", shortest_distance)


    # # #Using Divide and Conquer algorithm
    # print()
    # print("Using Divide and Conquer algorithm:")
    # print("From node", start_node, "to", end_node)
    # shortest_path, shortest_distance = dac.divide_and_conquer(graph, start_node, end_node)
    # print("Shortest path:", shortest_path)
    # print("Shortest distance:", shortest_distance)

    # # Using Bellman-Ford algorithm
    # print()
    # print("Using Bellman-Ford algorithm:")
    # print("Shortest distances from node", start_node, "to:")
    # shortest_distances,shortest_path = Bellmanford.bellman_ford(graph, start_node, end_node)
    # print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distances[end_node])
    # print("Shortest path:", shortest_path)