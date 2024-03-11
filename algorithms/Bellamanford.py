import pandas as pd

def bellman_ford(graph, start):
    # Initialize distances to all nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # Distance from start node to itself is 0
    
    # Relax edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph.get(node, {}).items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
    
    # Check for negative cycles
    for node in graph:
        for neighbor, weight in graph.get(node, {}).items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")
    
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

# Rest of the code remains the same
file_path = 'adjmatrix.xlsx'
graph = read_excel_file(file_path)
print_graph(graph)
start_node = input("Enter the starting node: ")

print("Shortest distances from node", start_node, "to:")
shortest_distances = bellman_ford(graph, start_node)
for node, distance in shortest_distances.items():
    print(f"{node} : {distance}")
