from pprint import pprint
def solution(board):
    for i in range(len(board)):
        board[i] = [0] + board[i] + [0]
    board = [[0 for _ in range(len(board[0]))]] + board + [[0 for _ in range(len(board[0]))]]
    
    
    lst = [] # 지뢰가 있는 좌표
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                lst.append([i, j])
    for i in lst:
        for l in [-1, 0, 1]:
            for k in [-1, 0, 1]:
                board[i[0] +l][i[1]+k] = -1
                # print(i[0] +l, i[1]+k)
    board[0] = [-1 for _ in range(len(board[0]))]
    board[len(board)-1] = [-1 for _ in range(len(board[0]))]
    for row in board:
        row[0] = -1
        row[-1] = -1
        
        
    num = 0
    for row in board:
        num += row.count(0)
    return num
    pprint(board)

