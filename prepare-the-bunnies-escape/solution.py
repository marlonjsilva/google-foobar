from collections import deque


class Point:
    def __init__(self, x, y, skip, map):
        """
        :param x: The x coordinate of the node on our grid.
        :param y: The y coordinate of the node on our grid.
        :param skip: The number of walls we can skip.
        :param map: The grid itself. All nodes know of the original matrix.
        """
        self.x = x
        self.y = y
        self.skip = skip
        self.map = map

    def __eq__(self, point):
        """
        Overloading the equals operator
        :param point: A node to compare to.
        :return: Whether or not the two nodes have identical contents. True or False.
        """
        return self.x == point.x and self.y == point.y and self.skip == point.skip

    def __hash__(self):
        """
        This will uniquely identify each node based on its coordinate
        by numbering nodes left to right, top to bottom.
        This hash function allows us to store nodes in our queue in our solution.
        :return: A unique identifier for this node.
        """
        return self.x + len(self.map) * self.y

    def get_vertices(self):
        """
        This function returns all the possible paths from our node.
        When we initialize each vertex, we keep track of if we've passed
        a wall up to this point. We don't treat any walls as vertices if we have.
        :return: A list of nodes that are passable from this node. May return an empty set.
        """
        v = list()
        x = self.x
        y = self.y
        skip = self.skip
        map = self.map
        width = len(map[0])
        height = len(map)

        if x > 0:
            if map[y][x - 1] == 1:
                if skip > 0:
                    v.append(Point(x - 1, y, skip - 1, map))
                else:
                    pass
            else:
                v.append(Point(x - 1, y, skip, map))

        if x < width - 1:
            if map[y][x + 1] == 1:
                if skip > 0:
                    v.append(Point(x + 1, y, skip - 1, map))
                else:
                    pass
            else:
                v.append(Point(x + 1, y, skip, map))

        if y > 0:
            if map[y - 1][x] == 1:
                if skip > 0:
                    v.append(Point(x, y - 1, skip - 1, map))
                else:
                    pass
            else:
                v.append(Point(x, y - 1, skip, map))

        if y < height - 1:
            if map[y + 1][x]:
                if skip > 0:
                    v.append(Point(x, y + 1, skip - 1, map))
                else:
                    pass
            else:
                v.append(Point(x, y + 1, skip, map))
        return v


class Router:
    def __init__(self, map, bypasses):
        """
        :param grid: The matrix resembling our maze.
        :param bypasses: The number of walls that we can pass on this iteration of the algorithm.
        """
        self.map = map
        self.height = len(map)
        self.width = len(map[0])
        self.bypasses = bypasses

    def get_path(self):
        """
        We employ breadth-first search to find the shortest path to the exit of the maze.
        To do this, we add each node to a queue if it hasn't been visited yet, while tracking
        the distance that's been traveled by our current node.
        :return: An integer describing the length of the shortest path to the maze's bottom-right
                 square (its exit).
        """
        source = Point(0, 0, self.bypasses, self.map)
        queue = deque([source])
        distance_map = {source: 1}

        while queue:
            # Grab the left-most element (the 'head' of our queue).
            curr = queue.popleft()

            # We're at the exit. This is our solution.
            if curr.x == self.width - 1 and curr.y == self.height - 1:
                return distance_map[curr]

            # If we're not at the end of the maze, then it's time to append its neighbours
            # to our queue so they'll be traversed later.
            for neighbor in curr.get_vertices():
                # This is where that hash function comes into play.
                if neighbor not in distance_map.keys():
                    distance_map[neighbor] = distance_map[curr] + 1
                    queue.append(neighbor)


def solution(maze):
    router = Router(maze, 1)
    return router.get_path()
