from collections import Counter
from copy import deepcopy
from fractions import Fraction,gcd



def solution(m):
    """Calculates the probabilities of terminating at abosrbing states

    :param m: A square matrix of nxn
    :type m: matrix nxn
    """

    def minor(matrix, i, j):
        """Calculates the minor of a matrix at a particular cell

        :param matrix: A nxn matrix
        :type matrix: matrix nxn
        :param i: The id of a cell in the row
        :type i: int
        :param j: The column of the cell
        :type j: int
        :return: A (n-1)x(n-1) matrix representing the minor of the matrix at matrix[i][j]
        :rtype: A matrix nxn
        """
        return [row[:j] + row[j+1:] for k, row in enumerate(matrix) if k != i]

    def determinant(matrix):
        """Calculates the determinant of a matrix through a recursive process

        :param matrix: A nxn matrix
        :type matrix: matrix nxn
        :return: An integer denoting the determinant of the matrix
        :rtype: int
        """
        if len(matrix) == 2:
            return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])

        return sum(((-1) ** j) * matrix[0][j] * determinant(minor(matrix, 0, j))
                   for j in range(len(matrix[0])))

    def adjoint(matrix):
        """Calculates the adjoint also known as the adjucate of the matrix.
        It is a matrix of cofactors for each element in the matrix

        :param matrix: A nxn matrix
        :type matrix: matrix nxn
        :return: A nxn matrix of cofactors for each element in the matrix
        :rtype: matrix nxn
        """
        if len(matrix) == 2:
            return [[matrix[1][1], -matrix[1][0]], [-matrix[0][1], matrix[0][0]]]
        return [[((-1) ** (i+j)) * determinant(minor(matrix, i, j))
                 for j in range(len(matrix[0]))] for i in range(len(matrix))]

    def transpose(matrix):
        """Produces the transpose of a matrix

        :param matrix: A nxn matrix
        :type matrix: matrix nxn
        :return: A nxn matrix that is the transpose of the given matrix
        :rtype: matrix nxn
        """
        return list(zip(*matrix))

    def inverse(matrix):
        """Caclulates the inverse of a matrix with the formula,
        Inverse(matrix) = (1 / determinant(matrix)) * adjoint(matrix)

        :param matrix: A nxn invertible matrix
        :type matrix: matrix nxn
        :return: A nxn matrrix that is the inverse of the given matrix.
        :rtype: matrix nxn
        """
        det = determinant(matrix)
        adj = adjoint(matrix)
        adj_transpose = transpose(adj)
        return [[adj_transpose[i][j] / det
                 for j in range(len(adj_transpose[0]))] for i in range(len(adj_transpose))]

    def matrix_multiply(A, B):
        """Multiplies two matrices. The two matrices need to be valid for
        multiplication.

        :param A: A mxn matrix
        :type A: matrix mxn
        :param B: A nxp matrix.
        :type B: matrix mxp
        :return: A mxp matrix.
        :rtype: matrix mxp
        """
        result = [[0] * len(B[0]) for _ in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j]
        return result

    def get_lcm(arr):
        """Calculates the least common multiple of a list of integers.

        :param arr: A List of integers.
        :type arr: list
        :return: An integer representing the lcm of a list of integers.
        :rtype: int
        """
        lcm = arr[0].denominator
        for frac in arr:
            lcm *= frac.denominator // gcd(frac.denominator, lcm)
        return lcm

    m_fractions = deepcopy(m)
    absorbing_states = []
    transient_states = []

    # Separating transient and absorbing states
    for i, row in enumerate(m):
        row_sum = sum(row)
        row_count = Counter(row)
        for j in range(len(m[0])):
            m_fractions[i][j] = Fraction(
                m[i][j], row_sum) if row_sum > 0 else Fraction(0)
        if row_count[0] == len(row) or (row_count[0] == len(row) - 1 and row[i] != 0):
            absorbing_states.append(i)
        else:
            transient_states.append(i)

    R = [[0] * len(absorbing_states)
         for _ in range(len(m_fractions) - len(absorbing_states))]
    Q = [[0] * len(transient_states) for _ in range(len(transient_states))]

    i = 0
    for tr1 in transient_states:
        j = 0
        for ab1 in absorbing_states:
            R[i][j] = m_fractions[tr1][ab1]
            j += 1

        j = 0
        for tr2 in transient_states:
            # Calculates I - Q directly
            Q[i][j] = 1 - m_fractions[tr1][tr2] if i == j else - \
                m_fractions[tr1][tr2]
            j += 1
        i += 1

    F = inverse(Q)
    prob_of_termination = matrix_multiply(F, R)

    lcm = get_lcm(prob_of_termination[0])
    result = [(prob_of_termination[0][j] *
               lcm).numerator for j in range(len(prob_of_termination[0]))]
    result.append(lcm)

    return result


if __name__ == "__main__":
    print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
    print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))