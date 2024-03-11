# Importing the pandas library and defining it "pd"
import pandas as pd

# Reading an Excel file and converting it into a graph structure
def read_excel_file(file_path):
    # Input:
        # The given path to the Excel file
    # Output (Returns):
        # The returned graph strucutre
    df = pd.read_excel(file_path, index_col=0)
    graph = df.to_dict(orient='index')
    return graph

# Printing the graph structure
def print_graph(graph):
    # Input:
        # The previously returned graph structure
    # Output (Prints):
        # The printed graph structure
    for node in sorted(graph.keys()):
        print(f"{node}:", end=" ")
        for neighbor, weight in sorted(graph[node].items()):
            print(f"({neighbor}, {weight})", end=" ")
        print()
