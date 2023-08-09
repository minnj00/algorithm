import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze  = []
    for _ in range(N):
        maze.append(list(map(int, input()))) # 숫자가 붙어있으니깐 split 안됨
    for j in range(N):
        for i in range(N):
            if maze[i][j] == 2:
                start = (i, j)
                maze[i][j] = -1
        

    
    # # bfs를 동작하기 위한 queue
    queue = []
    queue.append(start)

    # # 상하 좌우 델타 값
    dx = [0, 0, -1 ,1]
    dy = [-1, 1, 0, 0]

    result = 0
    distance =[[0 for _ in range(N)] for _ in range(N)]
    
    while len(queue):

        now = queue.pop(0)
        x, y= now[0], now[1]
        # 한번 그 위치를 지나갈 때마다
        maze[x][y] = 1
    
    #이동한 거리를 -1 -2 -3 으로 표시하는 경우
        # 상하좌우를 바라보는 코드 
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N: 
                # 길이라면
                if maze[nx][ny] == 0:
                    queue.append((nx, ny))
                    maze[nx][ny] = maze[x][y] -1
                # 도착지점이라면
                elif maze[nx][ny] == 3:
                    # 거리 계산 결과를 저장
                    result = abs(maze[x][y])-1
                    break
            
    print(result)

                # 앞에 maze[i][j] = -1 도 삭제해서 실행해야함

                # if maze[nx][ny] == 0:
                #     queue.append((nx, ny))
                #     distance[nx][ny] = distance[x][y] + 1
                # # 도착지점이라면
                # elif maze[nx][ny] == 3:
                #     distance[nx][ny] = distance[x][y]
                #     result = distance[nx][ny]
                #     break