import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # v: 노드 수/ E: 간선 수 
    V, E = list(map(int, input().split()))

    nodes = [ [0] * (V+1) for _ in range(V+1)]
    # pprint(nodes)
    # 인덱스랑 맞추기 위해 V+1까지


    # 인접행렬 방식으로 그래프를 저장 
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))

        nodes[start][end] = 1
        nodes[end][start] = 1 # 양방이므로 

    S, G = list(map(int, input().split()))

      # 방문 체크용 리스트 
    # check_list = [False] * (V+1)

    # bfs를 구현하기 위한 queue  queue 
    queue = []
    
    # now 는 출발노드와 출발노드에서 움직인 거리(처음엔 0으로 설정)
    move = 0
    now = S
    # check_list[now] = True #방문처리 
    queue.append(now)

    # 거리계산을 위한 리스트
    distance = [0] * (V+1)

    # 큐가 비어있지 않으면 계속 반복. 큐가 비었다는 탐색할 곳 다 했다는 의미
    while len(queue):
        # print(check_list)
        print(distance)
        now = queue.pop(0) # queue 의 맨 앞에 있는 것이 삭제되며 now에 할당됨.
        # check_list[now] = True # 도달했다는 표시 (방문했다는 표시)
        
        for link in range(V+1): # 한 줄을 잡아서 쭉 봐보기 위한 반복문 
            # 연결된 것만 확인
            # now를 기준으로 연결되어 있다면
            if nodes[now][link] == 1: # ex) now = 1인 처음에 행렬에서 1행 의 7개의 열들을 다 돌아보고 nodes[now][link]가 1이라면 연결되어 있음을 의미. 3, 4가 해당.
                # 방문하지 않았다면 
                if not distance[link]: # distance 가 0이라면 방문을 안했다는 것 뭐라도 있으면 한번은 방문했다는 뜻
                # if not check_list[link]: # ex) now =1, check_list[3] == 0 (방문하지 않았다면) 이라면 stack에 이 값을 추가 
                    # 큐에 추가
                    queue.append(link)
                    # 이전 노드의 거리 + 1
                    distance[link] = distance[now] + 1
    print(f'{tc} {distance[G]}')
                     
    






#   # now 는 출발노드와 출발노드에서 움직인 거리(처음엔 0으로 설정)
#     move = 0
#     now = [S, move]
#     check_list[now[0]] = True #방문처리 
#     queue.append(now)

    # #움직인 거리 
    # result = 0

    # # 큐가 비어있지 않으면 계속 반복. 큐가 비었다는 탐색할 곳 다 했다는 의미
    # while len(queue):
    #     # print(queue)
    #     now = queue.pop(0) # queue 의 맨 앞에 있는 것이 삭제되며 now에 할당됨.
    #     check_list[now[0]] = True # 도달했다는 표시 (방문했다는 표시)
        
    #     for link in range(V+1): # 한 줄을 잡아서 쭉 봐보기 위한 반복문 
    #         # 연결된 것만 확인
    #         # now를 기준으로 연결되어 있다면
    #         if nodes[now[0]][link] == 1: # ex) now = 1인 처음에 행렬에서 1행 의 7개의 열들을 다 돌아보고 nodes[now][link]가 1이라면 연결되어 있음을 의미. 3, 4가 해당.
    #             # 방문하지 않았다면 
    #             if not check_list[link]: # ex) now =1, check_list[3] == 0 (방문하지 않았다면) 이라면 stack에 이 값을 추가 
    #                 if link == G:
    #                     result = now[1]+1
    #                 # 큐에 추가
    #                 queue.append([link, now[1]+1]) # now 가 pop 되면서 추가되는 값들은 now와 간선 하나로 연결된 것이므로 now까지 이동 거리에 1추가한 것이 queue 에 새로 추가된 노드의 이동거리 
    # print(f'{tc} {result}')