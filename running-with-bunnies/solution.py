import itertools

def convert_to_path(perm):
    """convert_to_path _summary_

    :param perm: Possible path in maze
    :type perm: tuple
    :return: The path
    :rtype: list
    """
    perm = list(perm)
    perm = [0] + perm + [-1]
    path = list()
    for i in range(1, len(perm)):
        path.append((perm[i - 1], perm[i]))
    return path

def solution(times, time_limit):
    """
    This method will apply the Floyd-Warshall algorithm
    to get the nearest path inside the maze to get the 
    bunnies in ascending order

    :param times: the maze 
    :type times: list
    :param times_limit: the amount of times available
    :type times_limit: int
    :return: sorted id's of the bunnies
    :rtype: list
    """
    rows = len(times)
    bunnies = rows - 2

    if rows == 2:
        return []
    
    # The Floyd-Warshall Algorithm
    for k in range(rows):
        for i in range(rows):
            for j in range(rows):
                if times[i][j] > times[i][k] + times[k][j]:
                    times[i][j] = times[i][k] + times[k][j]

    for r in range(rows):
        if times[r][r] < 0:
            return [i for i in range(bunnies)]
    
    
    # Get the bunnies in sorted order 
    for i in reversed(range(bunnies + 1)):
        for perm in itertools.permutations(range(1, bunnies + 1), i):
            total_times = 0
            path = convert_to_path(perm)
            for start, end in path:
                total_times += times[start][end]
            if total_times <= time_limit:
                return sorted(list(i - 1 for i in perm))
    return None


if __name__ == "__main__":
    print(solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))