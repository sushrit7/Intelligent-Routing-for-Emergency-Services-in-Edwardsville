import heapq
import pandas as pd

def dijkstra(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Distance from start node to itself is 0
    # Priority queue to store nodes with their current distances
    priority_queue = [(0, start)]  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # Ignore nodes that have already been visited with shorter distance
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If new distance is shorter than the previously known distance to neighbor
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def read_excel_file(file_path):
    df = pd.read_excel(file_path, index_col=0)
    graph = df.to_dict(orient='index')
    return graph

def print_graph(graph):
    for node in sorted(graph.keys()):
        print(f"{node}:", end=" ")
        for neighbor, weight in sorted(graph[node].items()):
            print(f"({neighbor}, {weight})", end=" ")
        print()

# Function to create graph 
def create_graph():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    
    for _ in range(num_edges):
        source, dest, weight = input("Enter source, destination, and weight separated by space: ").split()
        weight = int(weight)
        
        if source not in graph:
            graph[source] = {}
        if dest not in graph:
            graph[dest] = {}
        
        graph[source][dest] = weight
        graph[dest][source] = weight  
    
    return graph

file_path = 'adjmatrix.xlsx'  
graph = read_excel_file(file_path)
print_graph(graph)
start_node = input("Enter the starting node: ")

print("Shortest distances from node", start_node, "to:")
shortest_distances = dijkstra(graph, start_node)
for node, distance in shortest_distances.items():
    print(node + ":", distance)
