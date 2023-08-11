# 인접행렬방식으로 그래프를 표현
import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

from pprint import pprint

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
    # pprint(nodes)
    # S: 출발노드 / G: 도착노드
    S, G = list(map(int, input().split()))

    # 방문 체크용 리스트 
    check_list = [False] * (V+1)

    #dfs를 구현하기 위한 stack
    stack = []
    
    now = S
    check_list[now] = True #방문처리, 이 문제의 경우에는 check_list가 필요 없지만 간선의 방향이 한방향이더라도 싸이클이 돌게되면 무한히 반복되므로 필요!
    stack.append(now)

    result = 0
    # 스택이 비어있지 않으면 계속 반복. stack 이 비었다는 탐색할 곳 다 했다는 의미
    while len(stack):
        print(stack)
        now = stack.pop() # now 에 stack 의 맨 위에 있는 것이 now 에 할당됨.
        check_list[now] = True # 도달했다는 표시 (방문했다는 표시)
        
        for link in range(V+1): # 한 줄을 잡아서 쭉 봐보기 위한 반복문 
            
            # 연결된 것만 확인
            # now를 기준으로 연결되어 있다면
            if nodes[now][link] == 1: # ex) now = 1인 처음에 행렬에서 1행 의 7개의 열들을 다 돌아보고 nodes[now][link]가 1이라면 연결되어 있음을 의미. 3, 4가 해당.
                # 방문하지 않았다면 
                if not check_list[link]: # ex) now =1, check_list[3] == 0 (방문하지 않았다면) 이라면 stack에 이 값을 추가 
                    if link == G: # 이 부분은 나중에 해도 됨. 그냥 중간에 확인해서 맞다면 바로 result 에 1 넣으려고. 
                        result = 1
                    # 스택에 추가
                    stack.append(link)
                
    print(f'#{tc} {result}')

