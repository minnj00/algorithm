import sys
sys.stdin = open('input.txt')
from pprint import pprint # 예쁘게 프린트 하는 라이브러리 

TC = int(input())

# for tc in range(1,TC+1): # 테스트 케이스 TC개 반복
#     matrix = []
#     for i in range(10): #행 생성 반복
#         row = []
#         for j in range(10):
#             row.append(0)
#         matrix.append(row)
#     n = int(input())
#     for _ in range(n): # n개의 영역에 색칠 반복 
#         area = list(map(int,input().split()))
#         r1 = area[0]
#         c1 = area[1]
#         r2 = area[2]
#         c2 = area[3]
#         color = area[4]
#         for i in range(r2-r1+1):
#             for j in range(c2-c1+1): 
#                 matrix[r1+i][c1+j] += color
#     total = 0
#     for i in range(10):
#         for j in range(10):
#             if matrix[i][j] == 3:
#                 total += 1
#     print(f'#{tc} {total}')

                
        
for tc in range(1, T+1):
    
    N = int(input())
    board = [[[0 for _ in ragne(10)]] for _ in range(10)]
    
    board = []
    for _ in range(10):
        temp = []
        for _ in range(10):
            for _ in range(10):
                temp.append(0)
            board.append(temp)

    # 카운팅 정렬 활용 
    for i in range(N):
        color_data = list(map(int, input().split()))
        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]
        color = color_data[4]

        # 색칠시작
        for x in range(left_top_x, right_bottom_x+1):
            for y in range(left_top_y, right_bottom_y+1):
                board[x][y] += color 
    count = 0


    for x in range(board):
        for y in range(board[0]):
            if board[x][y] == 3:
                count += 1


