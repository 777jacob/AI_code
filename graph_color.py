class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def is_safe(self, vertex, colors, color):
        for i in range(self.num_vertices):
            if self.adjacency_matrix[vertex][i] == 1 and colors[i] == color:
                return False
        return True

    def graph_coloring_util(self, num_colors, colors, vertex):
        if vertex == self.num_vertices:
            return True

        for color in range(1, num_colors + 1):
            if self.is_safe(vertex, colors, color):
                colors[vertex] = color
                if self.graph_coloring_util(num_colors, colors, vertex + 1):
                    return True
                colors[vertex] = 0

    def graph_coloring(self, num_colors):
        colors = [0] * self.num_vertices
        if not self.graph_coloring_util(num_colors, colors, 0):
            print("Solution does not exist")
            return False

        print("Solution exists and following are the assigned colors:")
        for color in colors:
            print(color, end=" ")

        return True

# Example usage:
graph_instance = Graph(4)
graph_instance.adjacency_matrix = [[0, 1, 1, 1],
                                   [1, 0, 1, 0],
                                   [1, 1, 0, 1],
                                   [1, 0, 1, 0]]

num_colors = 3  # Number of colors
graph_instance.graph_coloring(num_colors)

