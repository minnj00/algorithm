import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

from pprint import pprint

T = int(input())

def dfs(now):
    # now 에 도착을 하면 방문체크함 
    check_list[now] = True 
    # 현재위치를 기준으로 연결된 노드 찾기 
    for link in nodes[now]:
        # 방문하지 않은 노드들은 스택에 추가 => 사실상 재귀함수 실행  
        if not check_list[link]:
            dfs(link)



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

    dfs(S)
# 이부분 print 어떤 값을 해야하는지 질문 
    result = 0
    if check_list[6] == True:
        result = 1
    print(result)