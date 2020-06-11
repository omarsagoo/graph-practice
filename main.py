from graphs.graph import Graph
from util.file_reader import read_graph_from_file
# from graphs.weighted_graph import WeightedGraph

def print_graph(graph):
    # Output the vertices & edges
        # Print vertices
        vertices = graph.get_vertices()
        print(f'The vertices are: {vertices} \n')

        v1, v2 = vertices[0].get_id(), vertices[len(vertices) - 1].get_id()

        # Print edges
        print('The edges are:')
        for vertex_obj in vertices:
            for neighbor_obj in vertex_obj.get_neighbors():
                print(f'({vertex_obj.get_id()} , {neighbor_obj.get_id()})')

        # Search the graph
        print('Performing BFS traversal...')
        graph.bfs_traversal(v1)

        # Find shortest path
        print(f'Finding shortest path from vertex {v1} to vertex {v2}...')
        shortest_path = graph.find_shortest_path(v1, v2)
        print(shortest_path)

        # Find all vertices N distance away
        print('Finding all vertices distance 2 away...')
        vertices_2_away = graph.find_vertices_n_away(v1, 2)
        print(vertices_2_away)

# Driver code
if __name__ == '__main__':

    import sys

    if len(sys.argv) == 1:
        # Create the graph
        graph = Graph(is_directed=True)

        # Add some vertices
        graph.add_vertex('A')
        graph.add_vertex('E')
        graph.add_vertex('B')
        graph.add_vertex('C')
        graph.add_vertex('D')
        graph.add_vertex('H')
        graph.add_vertex('G')
        graph.add_vertex('F')


        # Add connections
        graph.add_edge('A', 'B')
        graph.add_edge('B', 'C')
        graph.add_edge('B', 'D')
        graph.add_edge('D', 'E')
        graph.add_edge('E', 'F')
        graph.add_edge('H', 'G')

        # print graph to stdout
        print_graph(graph)
    else:
        filename = sys.argv[1]

        # Create graph from file
        graph = read_graph_from_file(filename)

        # print graph to stdout
        print_graph(graph)