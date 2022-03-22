import itertools


def solution(num_buns, num_required):
    """Return the distribution of codes keys based on the number of bunnies and numbers requeried

    :param num_buns: An integer ranging from 1 to 9
    :type num_buns: int
    :param num_required: An integer ranging from 0 to 9
    :type num_required: int
    :return: A list of sequence codes for every bunny
    :rtype: list
    """
    result = []
    comb = list(itertools.combinations(range(num_buns),num_required))
    total = len(comb)*num_required
    n_times = (num_buns - num_required) + 1
    new_comb = list(itertools.combinations(range(num_buns),n_times))
    for i in range(num_buns):
        result.append([])
    for i in range(total/n_times):
        for j in new_comb[i]:
            result[j].append(i)
    return result


if __name__ == "__main__":
    print(solution(2,1))
    print(solution(4,4))
    print(solution(5,3))