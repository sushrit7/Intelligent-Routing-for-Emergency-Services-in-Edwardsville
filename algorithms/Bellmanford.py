# import pandas as pd

# def bellman_ford(graph, start):

#     # Initializing distances to all nodes as infinity
#     distances = {node: float('infinity') for node in graph}
#     distances[start] = 0  # As distance from start node to itself is 0
    
#     # Relaxing edges repeatedly
#     for _ in range(len(graph) - 1):
#         for node in graph:
#             for neighbor, weight in graph.get(node, {}).items():
#                 if distances[node] + weight < distances[neighbor]:
#                     distances[neighbor] = distances[node] + weight
    
#     # Checking for negative cycles
#     for node in graph:
#         for neighbor, weight in graph.get(node, {}).items():
#             if distances[node] + weight < distances[neighbor]:
#                 raise ValueError("Graph contains negative cycle")
    
#     return distances


def bellman_ford(graph, start, end):
    # Initializing distances to all nodes as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0  # As distance from start node to itself is 0
    
    # Predecessors to track the shortest path
    predecessors = {node: None for node in graph}
    
    # Relaxing edges repeatedly
    for _ in range(len(graph) - 1):
        for node in graph:
            for neighbor, weight in graph.get(node, {}).items():
                if distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight
                    predecessors[neighbor] = node
    
    # Checking for negative cycles
    for node in graph:
        for neighbor, weight in graph.get(node, {}).items():
            if distances[node] + weight < distances[neighbor]:
                raise ValueError("Graph contains negative cycle")
    
    # Constructing the shortest path
    shortest_path = []
    node = end  # Start from the destination node
    while node is not None:
        shortest_path.insert(0, node)
        node = predecessors[node]
    
    return distances, shortest_path
