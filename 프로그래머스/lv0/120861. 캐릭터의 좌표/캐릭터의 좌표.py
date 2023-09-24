def solution(keyinput, board):
    direc = ['up', 'down', 'left', 'right']
    move = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    max_lim = [board[0]//2, board[1]//2]
    min_lim = [-(board[0]//2), -(board[1]//2)]
    # print(max_lim, min_lim)
    now = [0, 0]
    for i in keyinput:
        # # board의 바깥으로 나가는 이동을 한다면 그것은 무시하기 
        # # 1. now의 세로방향 위치가 이미 한계에 있는 경우
        # # 가로방향의 위치에만 영향을 주기
        # if now[0] == max_lim[0] or now[0] == min_lim[0]:
        #     if now[1] == max_lim[1] or now[1] == min_lim[1]:
        #         continue
        #     else:
        #         now[1] += move[direc.index(i)][1]
        # # 2. now의 가로방향 위치가 이미 한계에 있는 경우
        # # 세로방향의 위치에만 변화
        # elif now[1] == max_lim[1] or now[1] == min_lim[1]:
        #     if now[0] == max_lim[0] or now[0] == min_lim[0]:
        #         continue
        #     else:
        #         now[1] += move[direc.index(i)][0]
        # else:
        now[0] += move[direc.index(i)][0]
        now[1] += move[direc.index(i)][1]
        if now[0] > max_lim[0] or now[0] < min_lim[0]:
            now[0] -= move[direc.index(i)][0]
    # 2. now의 가로방향 위치가 이미 한계에 있는 경우
    # 세로방향의 위치에만 변화
        elif now[1] > max_lim[1] or now[1] < min_lim[1]:
            now[1] -= move[direc.index(i)][1]
        
        # print(now)
        
    return now