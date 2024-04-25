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

# Function to update the weights of the graph
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
    num = 50
    congestion_level =[20, 40, 60, 80, 100]
    
    for n in range(num):
        # List of edges
        edges = ["EB", "EFI", "EFII", "EFIII", "EPD", "MPD", "SPD", "AH", "CVA", "RA", "PA", "SA", "EA"]
        # Randomly choosing a pair of nodes
        edge = random.sample(edges, 2)
        print("Randomly chosen pair of nodes:", edge)

        weights = {}
        for e in edge:
            print(f"Edge: {e}")

        new_weight = float("infinity")
        print(f"New weight for edge {edge}: {new_weight}")
        # Update the weights of the graph
        weights[(edge[0], edge[1])] = new_weight
        weights[(edge[1], edge[0])] = new_weight  
        # Update the weights of the graph
        updated_graph = update_weights(graph, weights)

    print()
    graph_tools.print_graph(updated_graph)
    print()
    residential_areas = ["EB", "AH", "CVA", "RA", "PA", "SA", "EA"]
    emergency_services = ["EFI", "EFII", "EFIII", "EPD", "MPD", "SPD"]
    results = []

    # Loop through all the residential areas and emergency services
    for area in residential_areas:
        for emergency_service in emergency_services:
            shortest_distance_dijkstra, shortest_path_dijkstra = Dijkstra.dijkstra(updated_graph, emergency_service, area)
            shortest_path_dac, shortest_distance_dac = dac.divide_and_conquer(updated_graph, emergency_service, area)
            shortest_distances_bellmanford, shortest_path_bellmanford = Bellmanford.bellman_ford(updated_graph, emergency_service, area)

            # Appending the results to the list
            results.append((area, emergency_service, shortest_distance_dijkstra, shortest_distance_dac, shortest_distances_bellmanford[area], shortest_path_dijkstra, shortest_path_dac, shortest_path_bellmanford))

    df = pd.DataFrame(results, columns=["From Node", "To Node", "Dijkstra_distance", "Divide_and_Conquer_distance", "Bellman-Ford_distance","Dijkstra_path","Divide_and_Conquer_path","Bellman-Ford_path"])
    df.to_excel("exp3.xlsx", index=False)
