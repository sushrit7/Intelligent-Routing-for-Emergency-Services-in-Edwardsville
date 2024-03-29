import heapq
import pandas as pd

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {}
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))
    
    shortest_path = []
    node = end
    while node is not None:
        shortest_path.append(node)
        node = previous_nodes.get(node)
    shortest_path.reverse()

    return distances[end], shortest_path  # Return the shortest distance and path to the end node


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

