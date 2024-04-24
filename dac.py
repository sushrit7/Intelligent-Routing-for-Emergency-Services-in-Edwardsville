def find_midpoint(graph, start, goal):
    # Initialize variables to store the shortest distance and the label of the midpoint node
    shortest_distance = float('inf')
    midpoint_label = None

    # Iterate over each node in the graph
    for node_label in graph.keys():
        # Calculate the distance from the start node to the current node
        distance_from_start = graph[start].get(node_label, float('inf'))
        # Calculate the distance from the current node to the goal node
        distance_to_goal = graph[node_label].get(goal, float('inf'))
        # Calculate the total distance from the start node to the goal node passing through the current node
        total_distance = distance_from_start + distance_to_goal

        # If the total distance is shorter than the current shortest distance, update the shortest distance
        # and the label of the midpoint node
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            midpoint_label = node_label

    # Return the label of the midpoint node
    return midpoint_label

def divide_and_conquer_recursive(graph, start, goal):
    # Initialize a set to keep track of visited nodes
    visited = set()
    # Initialize a stack to perform depth-first traversal
    stack = [(start, [start], 0)]
    # Initialize variables to store the shortest path and its distance
    shortest_path = None
    shortest_distance = float('inf')

    # Perform depth-first traversal
    while stack:
        # Pop the top node from the stack
        current_node, path, distance = stack.pop()

        # If the current node is the goal node
        if current_node == goal:
            # If the distance to the goal node is shorter than the current shortest distance,
            # update the shortest path and its distance
            if distance < shortest_distance:
                shortest_path = path
                shortest_distance = distance
        # If the current node has not been visited
        elif current_node not in visited:
            # Mark the current node as visited
            visited.add(current_node)
            # Iterate over the neighbors of the current node
            for neighbor, weight in graph[current_node].items():
                # Push the neighbor node, the updated path, and the updated distance onto the stack
                stack.append((neighbor, path + [neighbor], distance + weight))

    # Return the shortest path and its distance
    return shortest_path, shortest_distance

def divide_and_conquer(graph, start, goal):
    # Find the midpoint between the start and goal nodes
    midpoint = find_midpoint(graph, start, goal)
    # Find the shortest path from the start node to the midpoint
    path_from_start, distance_from_start = divide_and_conquer_recursive(graph, start, midpoint)
    # Find the shortest path from the midpoint to the goal node
    path_to_goal, distance_to_goal = divide_and_conquer_recursive(graph, midpoint, goal)

    # If either of the paths is None, indicating that there is no path between the start and goal nodes
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
