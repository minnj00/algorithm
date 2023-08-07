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

    nodes = [ [0] for _ in range(V+1)]
    # pprint(nodes)


    # 인접 리스트 방식으로 그래프를 저장 
    # 간선의 갯수만큼 반복을 진행
    for line in range(E):
        start, end = list(map(int, input().split()))
        nodes[start].append(end)

    # pprint(nodes)
    # S: 출발노드 / G: 도착노드
    S, G = list(map(int, input().split()))

    check_list = [False] * (V+1)

    stack = []

    now = S
    check_list[now] = True
    stack.append(now)

    result = 0 
    while len(stack):  # stack 길이가 0이 될때까지 반복
        print(stack)  #과정을 이해하고 싶으면 프린트해보며 확인 
        now = stack.pop()
        check_list[now] = True
        
        # 인접리스트를 기준으로 now 와 연결된 link의 노드들을 반복 
        for link in nodes[now]:
            # 방문하지 않았다면
            if not check_list[link]:
                # 목적지가 연결되어 있다면
                if link == G:
                    result = 1
                # 스택에 추가
                stack.append(link)
# 직접 그려가며 이해하기
    print(f'#{tc} {result}')
