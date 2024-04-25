import pandas as pd

# Reading an Excel file and converting it into a graph structure
def read_excel_file(file_path):
    df = pd.read_excel(file_path, index_col=0)
    graph = df.to_dict(orient='index')
    return graph

# Printing the graph structure
def print_graph(graph):
    for node in sorted(graph.keys()):
        print(f"{node}:", end=" ")
        for neighbor, weight in sorted(graph[node].items()):
            print(f"({neighbor}, {weight})", end=" ")
        print()
