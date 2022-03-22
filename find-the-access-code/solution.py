def answer(l):
    """
    This method will calculate how many lucky triplets are in the given list l

    Params
    ---
    l [list] : List of numbers

    Returns
    ---
    int : How many lucky triplets are in the given list
    """
    # Initialize a list to keep track of how many times a number has been multiple of a previous number
    counts = [0] * len(l)
    result = 0
    # Iterates over the given list
    for product in range(0, len(l)):
        for f in range(0, product):
            # Check if product if a multiple of f
            if l[product] % l[f] == 0:
                counts[product] += 1
                result += counts[f]
    return result


if __name__ == "__main__":
    case0 = [1, 1, 1]
    print("\nCase 0:\n", case0, "\n\n  Expected: 1\nCalculated:", str(answer(case0)))

    case1 = [1, 2, 3, 4, 5, 6]
    print("\nCase 1:\n", case1, "\n\n  Expected: 3\nCalculated:", str(answer(case1)))

    case2 = [1, 2, 4, 8]
    print("\nCase 2:\n", case2, "\n\n  Expected: 4\nCalculated:", str(answer(case2)))
