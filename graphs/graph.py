from collections import deque
from random import choice

class Vertex(object):
    """
    Defines a single vertex and its neighbors.
    """

    def __init__(self, vertex_id):
        """
        Initialize a vertex and its neighbors dictionary.
        
        Parameters:
        vertex_id (string): A unique identifier to identify this vertex.
        """
        self.__id = vertex_id
        self.__neighbors_dict = {} # id -> object

    def add_neighbor(self, vertex_obj):
        """
        Add a neighbor by storing it in the neighbors dictionary.

        Parameters:
        vertex_obj (Vertex): An instance of Vertex to be stored as a neighbor.
        """
        self.__neighbors_dict[vertex_obj.__id] = vertex_obj

    def __str__(self):
        """Output the list of neighbors of this vertex."""
        neighbor_ids = list(self.__neighbors_dict.keys())
        return f'{self.__id} adjacent to {neighbor_ids}'

    def __repr__(self):
        """Output the list of neighbors of this vertex."""
        return self.__str__()

    def get_neighbors(self):
        """Return the neighbors of this vertex."""
        return list(self.__neighbors_dict.values())

    def get_id(self):
        """Return the id of this vertex."""
        return self.__id


class Graph:
    """ Graph Class
    Represents a directed or undirected graph.
    """
    def __init__(self, is_directed=True):
        """
        Initialize a graph object with an empty vertex dictionary.

        Parameters:
        is_directed (boolean): Whether the graph is directed (edges go in only one direction).
        """
        self.__vertex_dict = {} # id -> object
        self.__is_directed = is_directed

    def add_vertex(self, vertex_id):
        """
        Add a new vertex object to the graph with the given key and return the vertex.
        
        Parameters:
        vertex_id (string): The unique identifier for the new vertex.

        Returns:
        Vertex: The new vertex object.
        """
        vertex = Vertex(vertex_id)
        self.__vertex_dict[vertex_id] = vertex

        return vertex
        

    def get_vertex(self, vertex_id):
        """Return the vertex if it exists."""
        if vertex_id not in self.__vertex_dict:
            return None

        vertex_obj = self.__vertex_dict[vertex_id]
        return vertex_obj

    def add_edge(self, vertex_id1, vertex_id2):
        """
        Add an edge from vertex with id `vertex_id1` to vertex with id `vertex_id2`.

        Parameters:
        vertex_id1 (string): The unique identifier of the first vertex.
        vertex_id2 (string): The unique identifier of the second vertex.
        """
        vertex = self.get_vertex(vertex_id1)
        vertex2 = self.get_vertex(vertex_id2)
        vertex.add_neighbor(vertex2)

        if self.__is_directed == False:
            vertex2.add_neighbor(vertex)
        
    def get_vertices(self):
        """
        Return all vertices in the graph.
        
        Returns:
        List<Vertex>: The vertex objects contained in the graph.
        """
        return list(self.__vertex_dict.values())

    def contains_id(self, vertex_id):
        return vertex_id in self.__vertex_dict

    def __str__(self):
        """Return a string representation of the graph."""
        return f'Graph with vertices: {self.get_vertices()}'

    def __repr__(self):
        """Return a string representation of the graph."""
        return self.__str__()

    def bfs_traversal(self, start_id):
        """
        Traverse the graph using breadth-first search.
        """
        if not self.contains_id(start_id):
            raise KeyError("One or both vertices are not in the graph!")

        # Keep a set to denote which vertices we've seen before
        seen = set()
        seen.add(start_id)

        # Keep a queue so that we visit vertices in the appropriate order
        queue = deque()
        queue.append(self.get_vertex(start_id))

        while queue:
            current_vertex_obj = queue.pop()
            current_vertex_id = current_vertex_obj.get_id()

            # Process current node
            print('Processing vertex {}'.format(current_vertex_id))

            # Add its neighbors to the queue
            for neighbor in current_vertex_obj.get_neighbors():
                if neighbor.get_id() not in seen:
                    seen.add(neighbor.get_id())
                    queue.append(neighbor)

        return # everything has been processed

    def find_shortest_path(self, start_id, target_id):
        """
        Find and return the shortest path from start_id to target_id.

        Parameters:
        start_id (string): The id of the start vertex.
        target_id (string): The id of the target (end) vertex.

        Returns:
        list<string>: A list of all vertex ids in the shortest path, from start to end.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("One or both vertices are not in the graph!")

        # vertex keys we've seen before and their paths from the start vertex
        vertex_id_to_path = {
            start_id: [start_id] # only one thing in the path
        }

        # queue of vertices to visit next
        queue = deque() 
        queue.append(self.get_vertex(start_id))

        # while queue is not empty
        while queue:
            current_vertex_obj = queue.pop() # vertex obj to visit next
            current_vertex_id = current_vertex_obj.get_id()

            # found target, can stop the loop early
            if current_vertex_id == target_id:
                break

            neighbors = current_vertex_obj.get_neighbors()
            for neighbor in neighbors:
                if neighbor.get_id() not in vertex_id_to_path:
                    current_path = vertex_id_to_path[current_vertex_id]
                    # extend the path by 1 vertex
                    next_path = current_path + [neighbor.get_id()]
                    vertex_id_to_path[neighbor.get_id()] = next_path
                    queue.append(neighbor)
                    # print(vertex_id_to_path)

        if target_id not in vertex_id_to_path: # path not found
            return None

        return vertex_id_to_path[target_id]

    def find_vertices_n_away(self, start_id, target_distance):
        """
        Find and return all vertices n distance away.
        
        Arguments:
        start_id (string): The id of the start vertex.
        target_distance (integer): The distance from the start vertex we are looking for

        Returns:
        list<string>: All vertex ids that are `target_distance` away from the start vertex
        """
        queue = deque()
        visited = set()

        queue.append(self.get_vertex(start_id))

        for _ in range(target_distance):
            for _ in range(len(queue)):
                vertex = queue.pop()
                if vertex not in visited:
                    for neighbor in vertex.get_neighbors():
                        queue.appendleft(neighbor)
                    visited.add(vertex)

        found = []
        for vertex in queue:
            if vertex not in visited and vertex.get_id() not in found:
                found.append(vertex.get_id())

        return found

    def is_bipartite(self, vertex_id):
        """
        Checks if the graph is Bipartite
        
        Arguments:
        vertex_id (string): The ID of the start Vertex
        
        Returns:
        bool (bool): True or False, if bipartite or not
        """
        # get the vertex object with the given ID
        vertex = self.get_vertex(vertex_id)

        # instantiate queue and add the first vertex obj
        queue = deque()
        queue.append(vertex)

        # instantiate visited set, so we do not check the same vertex twice.
        visited = set()

        # instatiate a red set and blue set, to check if the graph is bipartite. 
        # red and blue are arbitrary names, colors are normaly used to display a bipartite graph
        red = set()
        blue = set()

        # create a counter
        i = 0

        # add the initial vertex to the red set
        red.add(vertex)

        # check while the queue is not empty
        while queue:

            # depending on the counter, set the appropriate sets to be used.
            color_set, opp_set = (red, blue) if i % 2 == 0 else (blue, red)

            # iterate the number of times that there are items in the queue
            for _ in range(len(queue)):
                # grab the next vertex off the queue
                vertex = queue.popleft()

                # add it to the visited set, so we do not check this vertex again if cyclical.
                visited.add(vertex)
                
                # go through each neighbor from the vertex and add it into the corresponding set.
                for neighbor in vertex.get_neighbors():

                    # only add the neighboring vertex if it has not been visited
                    if neighbor not in visited:
                        queue.append(neighbor)
                    
                    # check if the neighbor is in the same color set as the current vertex. if it is, return False
                    if neighbor in color_set:
                        return False

                    # add the neighboring vertexes into the opposite color set
                    opp_set.add(neighbor)

            # increment the counter
            i += 1

        # if the program reaches this point, then the graph is bipartite, return True
        return True

    def get_connected_components(self):
        """
        Return a list of all connected components, with each connected component
        represented as a list of vertex ids.
        """
        # start at a random vertex in the graph
        start_id = choice(self.get_vertices())

        # create a set of all the vertices in the graph and remove the starting vertex
        remaining = set(self.get_vertices())
        remaining.remove(start_id)

        # create a set of all the vertices we visited
        visited = set(start_id)
        
        # create a queue to keep track of the next vertex to visit
        queue = deque(self.get_vertex(start_id))

        # create two lists. one for all of the components, and one for the local connected components
        all_components = list()
        component = list()

        # while the queue is not empty
        while queue:
            # pop from the queue and get the ID of the vertex, then add it to the local components list
            vertex = queue.popleft()
            vertex_id = vertex.get_id()
            component.append(vertex_id)

            # get all the neighbors of the vertex
            neighbors = vertex.get_neighbors()

            # for each neighbor, if it wasnt seen, iteratively add them to the queue and remove them from the remaining set
            for neighbor in neighbors:
                neighbor_id = neighbor.get_id()
                if neighbor_id not in visited:
                    visited.add(neighbor_id)
                    remaining.remove(neighbor_id)

                    queue.append(neighbor)

            # if the queue is empty, append the local components to list of all components.
            if len(queue) == 0:
                all_components.append(component)
                component = list()

                if len(remaining) == 0:
                    break
                # get a new vertex from the remaining set and add it to the queue.
                next_vertex = choice(tuple(remaining))
                queue.append(self.get_vertex(next_vertex))
                visited.add(next_vertex)
                remaining.remove(next_vertex)

        # return all the connected components
        return all_components

    def find_path_dfs_iter(self, start_id, target_id):
        """
        Use DFS with a stack to find a path from start_id to target_id.
        """
        if not self.contains_id(start_id) or not self.contains_id(target_id):
            raise KeyError("Vertex not in graph")

        stack = deque(self.get_vertex(start_id))

        while stack:
            vertex = stack.pop()
            vertex_id = vertex.get_id()

            neighbors = vertex.get_neighbors()

            for neighbor in neighbors:
                pass

    def dfs_traversal(self, start_id):
        """Visit each vertex, starting with start_id, in DFS order."""

        visited = set() # set of vertices we've visited so far

        def dfs_traversal_recursive(start_vertex):
            print(f'Visiting vertex {start_vertex.get_id()}')

            # recurse for each vertex in neighbors
            for neighbor in start_vertex.get_neighbors():
                if neighbor.get_id() not in visited:
                    visited.add(neighbor.get_id())
                    dfs_traversal_recursive(neighbor)
            return

        visited.add(start_id)
        start_vertex = self.get_vertex(start_id)
        dfs_traversal_recursive(start_vertex)