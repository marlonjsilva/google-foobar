def convert_coord(src):
    """Convert a position number to a x,y coordinate in the in the board

    :param src: A number between 0 and 63
    :type src: int
    :return: A x,y coordinate
    :rtype: tuple
    """
    return src / 8, src % 8

def calculate_moves(sx, sy, board):
    """This method will calculate the moves from a sorce position
    to all other position in the board

    :param sx: The x axis
    :type sx: int
    :param sy: The y axis
    :type sy: int
    :param board: The chess board
    :type board: matrix
    """
    knight_moves = [[1,2],[-1,2],[1,-2],[-1,-2],[2,1],[-2,1],[2,-1],[-2,-1]]
    moves = [(sx, sy)]
    while moves:
        x, y = moves.pop(0)
        # Calculate a possible move based on knight's movements
        for i in knight_moves:
          nx, ny = x + i[0], y + i[1]
          # Verify if the position is inside the board
          if 0 <= nx <= 7 and 0 <= ny <= 7:
              if board[nx][ny] is None:
                  board[nx][ny] = board[x][y] + 1
                  moves.append((nx, ny)) 

def solution(src, dest):
    # Create a empty board
    board = [[None for i in range(8)] for i in range(8)]
    # Convert the source and destination position
    sx, sy = convert_coord(src)
    dx, dy = convert_coord(dest)
    # Initialize the position
    board[sx][sy] = 0
    #Compute the path
    calculate_moves(sx, sy, board)
    return board[dx][dy]

if __name__ == "__main__":
    print(solution(19,36))
    print(solution(0,1))
    print(solution(19,19))