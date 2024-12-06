from copy import deepcopy

def live_neighbors(board, row, col):
    neighbors = 0
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i < 0 or i > len(board) - 1:
                continue
            if j < 0 or j > len(board[i]) - 1:
                continue
            if i == row and j == col:
                continue
            if board[i][j]:
                neighbors += 1

    return neighbors


def solution(board: list[list[int]]) -> None:
    new_board = deepcopy(board)
    for row in range(len(board)):
        for col in range(len(board[row])):
            ln = live_neighbors(board, row, col)
            match ln:
                case 0 | 1:
                    if board[row][col] == 1:
                        new_board[row][col] = 0
                case 2:
                    if board[row][col] == 1:
                        new_board[row][col] = 1
                case 3:
                    new_board[row][col] = 1
                case ln if ln > 3:
                    if board[row][col] == 1:
                        new_board[row][col] = 0
    
    board = new_board

    print(board)



solution([[0, 1, 0], 
          [0, 0, 1], 
          [1, 1, 1], 
          [0, 0, 0]])