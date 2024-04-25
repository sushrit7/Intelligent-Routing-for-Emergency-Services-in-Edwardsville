def find_midpoint(graph, start, goal):
    # Initialize variables to store the shortest distance and the label of the midpoint node
    shortest_distance = float('inf')
    midpoint_label = None

    for node_label in graph.keys():
        distance_from_start = graph[start].get(node_label, float('inf'))
        distance_to_goal = graph[node_label].get(goal, float('inf'))
        total_distance = distance_from_start + distance_to_goal

        if total_distance < shortest_distance:
            shortest_distance = total_distance
            midpoint_label = node_label

    # Return the label of the midpoint node
    return midpoint_label

def divide_and_conquerr(graph, start, goal):
    visited = set()
    stack = [(start, [start], 0)]
    shortest_path = None
    shortest_distance = float('inf')
    while stack:
        current_node, path, distance = stack.pop()

        # If the current node is the goal node
        if current_node == goal:
            if distance < shortest_distance:
                shortest_path = path
                shortest_distance = distance
        elif current_node not in visited:
            visited.add(current_node)
            for neighbor, weight in graph[current_node].items():
                stack.append((neighbor, path + [neighbor], distance + weight))

    # Return the shortest path and its distance
    return shortest_path, shortest_distance

def divide_and_conquer(graph, start, goal):
    # Find the midpoint between the start and goal nodes
    midpoint = find_midpoint(graph, start, goal)
    # Find the shortest path from the start node to the midpoint
    path_from_start, distance_from_start = divide_and_conquerr(graph, start, midpoint)
    # Find the shortest path from the midpoint to the goal node
    path_to_goal, distance_to_goal = divide_and_conquerr(graph, midpoint, goal)

    if path_from_start is None or path_to_goal is None:
        shortest_path = None
        shortest_distance = float('inf')
    else:
        # Concatenate the paths from the start node to the midpoint and from the midpoint to the goal node
        shortest_path = path_from_start[:-1] + path_to_goal  # Exclude the common node at the midpoint
        # Calculate the total distance of the shortest path
        shortest_distance = distance_from_start + distance_to_goal

    # Return the shortest path and its distance
    return shortest_path, shortest_distance
