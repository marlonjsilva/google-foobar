from collections import defaultdict

def generate(c1,r1,bitlen):
    """ Generates the view of the next generation
    :param c1: Column of the grid
    :type c1: int
    :param r1: The row of the grid
    :type r1: int
    :param bitlen: The number of the columns
    :type bitlen: int
    :return: Returns the generation
    :rtype: int
    """
    a = c1 & ~(1<<bitlen)
    b = r1 & ~(1<<bitlen)
    c = c1 >> 1
    d = r1 >> 1
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def build_map(n, nums):
    """Maps the grid given a number of columns and sets

    :param n: The number of the column
    :type n: int
    :param nums: The sets of the column
    :type nums: tuple
    :return: The mapped sets of the columns
    :rtype: dict
    """
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(1<<(n+1)):
        for j in range(1<<(n+1)):
            generation = generate(i,j,n)
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping


def solution(g):
    """Given a 2D grid image in the format of array of bools, it will return the number of previous states that could have generated the 
    current image.

    :param g: A matrix representing the 2d grid image of the nebula in the format of array of bools
    :type g: list
    :return: The number of possible previous states that could have result the current image at 1 time step
    :rtype: int
    """
    #Convert the matrix into a list of sets
    g = list(zip(*g))
    ncols = len(g[0])
    nums = [sum([1<<i if col else 0 for i, col in enumerate(row)]) for row in g]
    # Maps the columns with nums and get the sets
    mapping = build_map(ncols, nums)
    preimage = {i: 1 for i in range(1<<(ncols+1))}
    #For every possibility it computes the previous image
    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for r1 in mapping[(row, c1)]:
                next_row[r1] += preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())
    return ret
    



if __name__ == "__main__":
    print(solution([[True, False, True], [False, True, False], [True, False, True]]))