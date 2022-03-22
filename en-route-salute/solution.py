def solution(s):
    """This method calculates how many saluts will happen in a hall, given
    a string representing the employees in the hall.
    :param s: The string representing the employee in the hall
    :type s: str
    :return: The number of saluts
    :rtype: int
    """
    ans = count = 0
    for c in s:
        if c == '>':
            count += 1
        elif c == '<':
            ans += count
    return ans * 2

if __name__ == "__main__":
    print(solution(">----<"))
    print(solution("<<>><"))
    print(solution("--->-><-><-->-"))