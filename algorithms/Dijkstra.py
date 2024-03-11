import heapq
import pandas as pd

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances[end]  # Return the shortest distance to the end node

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

# file_path = 'adjmatrix.xlsx'  
# graph = read_excel_file(file_path)
# print_graph(graph)

# start_node = input("Enter the starting node: ")
# end_node = input("Enter the ending node: ")

# shortest_distance = dijkstra(graph, start_node, end_node)
# print("Shortest distance from node", start_node, "to node", end_node, "is:", shortest_distance)