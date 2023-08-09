import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
    # maze  = []
    # for _ in range(N):
    #     maze.append(list(map(int, input()))) # 숫자가 붙어있으니깐 split 안됨
    # for j in range(N):
    #     for i in range(N):
    #         if maze[i][j] == 2:
    #             start = (i, j)
        
    # # print(miro)
    # # print(start)
    # # print(end)
    
    # # dfs를 동작하기 위한 스택
    # stack = []
    # stack.append(start)

    # # 상하 좌우 델타 값
    # dx = [0, 0, -1 ,1]
    # dy = [-1, 1, 0, 0]

    # result = 0
    # while len(stack):

    #     now = stack.pop()
    #     x, y= now[0], now[1]
    #     # 한번 그 위치를 지나갈 때마다
    #     maze[x][y] = 1 

    #     # 상하좌우를 바라보는 코드 
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #         if 0 <= nx < N and 0 <= ny < N: 
    #             # 길이라면
    #             if maze[nx][ny] == 0:
    #                 stack.append((nx, ny))
    #             # 도착지점이라면
    #             elif maze[nx][ny] == 3:
    #                 result = 1
    #                 break
            
    # print(result)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(map(int, input()))) # 숫자가 붙어있으니깐 split 안됨
    for j in range(N):
        for i in range(N):
            if miro[i][j] == 2:
                start = [i, j]
            if miro[i][j] == 3:
                end = [i, j]
    # print(miro)
    # print(start)
    # print(end)



    check_list = [[False for _ in range(N)] for _ in range(N)] # False 에 [] 씌워서 오류남.
    stack = []
    now = [] # 위치를 행과 열로 이루어진 리스트로 나타냄
    now = start 
    stack.append(start)

    result = 0 
    
    while len(stack): # 더이상 갈 곳이 없을 때 까지
        # print(stack)
        now = stack.pop()
        check_list[now[0]][now[1]] = True

       # 한 위치에서 4방향으로 갈 수 있음. 
        a = [now[0]+1,now[1]]
        b = [now[0]-1,now[1]]
        l = [now[0],now[1]-1]
        r = [now[0],now[1]+1]
        directions = [a, b, l, r]
        # print(directions)
        for direc in directions: # 그 방향들의 행과 열이 N 이하이고 이동했을 때 값이 0이여야 이동이 가능하다.
            if 0 <= direc[0] < N and 0 <= direc[1] < N:
                if miro[direc[0]][direc[1]] == 0: # 왜 인덱스 아웃오브 에러가 났었지만 위의 범위를 N 미만으로 고쳐 사라짐.
                    # print(direc)
                    # print(check_list[direc[0]][direc[1]])
                    if not check_list[direc[0]][direc[1]]:
                        stack.append(direc)
                        # print(stack)
                elif direc == end:
                    result = 1
                    break

    
    print(result)

            




