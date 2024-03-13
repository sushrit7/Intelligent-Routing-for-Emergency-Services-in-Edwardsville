import heapq
import pandas as pd
from rtree import index

def a_star(graph, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    while open_list:
        current_f, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], g_score[goal]
        
        for neighbor, weight in graph[current_node].items():
            tentative_g = g_score[current_node] + weight
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score[neighbor], neighbor))
    
    return None, float('inf')  # No path found

def heuristic(node, goal):
    if isinstance(node, str):  # Check if the node is a label
        return abs(len(node) - len(goal))  # Calculate the difference in label lengths
    else:  # If the node is an integer index
        return abs(node - goal)  # Calculate the absolute difference between node indices


def read_excel_file(file_path):
    df = pd.read_excel(file_path, index_col=0)
    return df.to_dict()

def create_rtree(graph):
    p = index.Property()
    rtree = index.Index(properties=p)
    # Insert nodes into the R-tree
    for node, _ in graph.items():
        rtree.insert(node, (node, node))  # Insert node with its label directly
    return rtree


def divide_and_conquer(graph, rtree, region, start, goal):
    # Base case: If the region contains a limited number of locations,
    # or if the region size is small enough, apply A* algorithm
    if len(region) < 10:  # Define the condition based on the number of locations
        return a_star(graph, start, goal)
    
    # Otherwise, recursively divide the region into subregions
    # and apply divide_and_conquer to each subregion
    
    # Subdivide the region using the R-tree
    subregions = rtree.intersection(region, objects=True)
    shortest_path = None
    shortest_distance = float('inf')  # Initialize shortest distance to infinity
    
    # Apply divide_and_conquer to each subregion
    for subregion in subregions:
        subregion_coords = subregion.bbox  # Pass the bounding box of the subregion
        path, distance = divide_and_conquer(graph, rtree, subregion_coords, start, goal)
        if distance < shortest_distance:
            shortest_path = path
            shortest_distance = distance
    
    return shortest_path, shortest_distance



def combine_results(shortest_paths):
    combined_shortest_path = shortest_paths[0] 
    for path in shortest_paths[1:]:
        if path is not None and (combined_shortest_path is None or len(path) < len(combined_shortest_path)):
            combined_shortest_path = path
    return combined_shortest_path

def astar(graph, start_label, goal_label):
    label_to_int = {label: i+1 for i, label in enumerate(['EB', 'EFI', 'EFII', 'EFIII', 'EPD', 'MPD', 'SPD', 'AH'])}
    int_to_label = {v: k for k, v in label_to_int.items()}  # Create a reverse mapping
    
    graph = {label_to_int[k]: {label_to_int[k2]: v2 for k2, v2 in v.items()} for k, v in graph.items()}

    # Convert labels to integers for internal processing
    start_node = label_to_int[start_label]
    goal_node = label_to_int[goal_label]

    # Create an R-tree for spatial indexing
    rtree = create_rtree(graph)

    # Apply divide_and_conquer approach to find the shortest path and distance
    shortest_path, shortest_distance = divide_and_conquer(graph, rtree, rtree.bounds, start_node, goal_node)
    
    # Convert integer node representations back to labels in the shortest path
    shortest_path_labels = [int_to_label[node] for node in shortest_path]

    return shortest_path_labels, shortest_distance
