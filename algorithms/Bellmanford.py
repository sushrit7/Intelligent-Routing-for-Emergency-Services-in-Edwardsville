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


