from graphs.graph import Graph

def read_graph_from_file(filename):
    """
    Read in data from the specified filename, and create and return a graph
    object corresponding to that data.

    Arguments:
    filename (string): The relative path of the file to be processed

    Returns:
    Graph: A directed or undirected Graph object containing the specified
    vertices and edges
    """
    # Use 'open' to open the file
    # Use the first line (G or D) to determine whether graph is directed 
    # and create a graph object
    f = open(filename).read().split()

    directed = True if f[0] == "D" else False
    graph = Graph(directed)

    # Use the second line to add the vertices to the graph
    verticies = f[1].split(',')

    for vertex in verticies:
        graph.add_vertex(vertex)

    # Use the 3rd+ line to add the edges to the graph
    for edge in f[2:]:
        v1, v2 = edge[1:len(edge) - 1].split(',')
        graph.add_edge(v1, v2)

    return graph
if __name__ == '__main__':

    graph = read_graph_from_file("util/graph_medium_undirected.txt")