# importing packages
import heapq
import pandas as pd

# main function finding the shortest path
def dijkstra(graph, start, end):
    # initializing the dictionary with every element as infinity
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    # creating an empty tuple to keep track of previously visited node
    previous_nodes = {}
    priority_queue = [(0, start)]

    # mina loop responsible for inserting and creating distances 
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # comparing the distance with the distance from the current node 
        if current_distance > distances[current_node]:
            continue

        # iterating through every current node and updating the distance 
        for neighbor, weight in graph.get(current_node, {}).items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(priority_queue, (distance, neighbor))

    # initializing the empty list to get the path stored between nodes
    shortest_path = []
    node = end
    while node is not None:
        shortest_path.append(node)
        node = previous_nodes.get(node)
    shortest_path.reverse()

    # returning the shortest path from teh list and distance between the node
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

