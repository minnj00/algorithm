import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())




for tc in range(1, T+1):
    # E: 간선의 개수
    # N: 부모노드(시작노드)
    E, N = list(map(int, input().split()))

    # nodes = list(map(int, input().split()))
    # 숫자가 
    # left_node = [0] * (E+2) # 노드의 개수가 E+1이므로 left_node[parent] 는 parent노드의 왼쪽 자식 노드 이게 0이면 자식노드 없음. 
    # right_node = [0] * (E+2)
    
    # for i in range(0, 2*E, 2): # 간선의 개수는 E 개 이므로 부모노드 자식노드가 E쌍으로 총 2*E 개의 숫자가 nodes 리스트에 있음 
    #     parent = nodes[i]
    #     child = nodes[i+1]
        
    #     if left_node[parent] == 0:
    #         left_node[parent] = child
    #     else: # 자식노드가 2개인 경우
    #         right_node[parent] = child
    # # print(left_node)
    # # print(right_node)
    # # 이제보니 표를 제공한 게 어떻게 보면 그런식으로 따라하라는 힌트라고 생각이 들었음.
     
    # stack = [N]
    # count = 0 
    
    # # 부모의 자식들을 찾고 그 자식이 부모인 자식을 찾기 자식이 없을 때까지
    # while stack: 
    #     print(stack)
    #     now = stack.pop()
    #     count += 1 

    #     if left_node[now]: #자식노드칸에 0이 있으면 실행이 안됨.
    #         stack.append(left_node[now])
    #     if right_node[now]:
    #         stack.append(right_node[now])

    # print(count)


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#    밑에 방법 질문하기
    
    nodes = [[0 for _ in range(E+2)] for _ in range(E+2)]  # 노드의 번호가 1부터 E+1까지 이므로 
    # print(nodes)
    # 인접행렬방식으로 부모노드의 자식노드의 연결을 저장

    tree = list(map(int, input().split()))
    # print(tree)
    for i in range(0, 2*E, 2):
        parent = tree[i]
        child = tree[i+1]
        nodes[parent][child] = 1  # 부모노드행의 자식노드의 열에 1을 저장 
    
       

    count = 0
    stack = []
    stack.append(N)
    check_list = [False] * (E+2)
    

    # stack 이용하기 
    while len(stack):
        now = stack.pop()
        count += 1
        check_list[now] = True
        # N번 부모노드 행에서 모든 열을 돌면서 자식노드를 확인
        for i in range(E+2):
            # N번 노드의 자식노드라면 
            if nodes[now][i] == 1:
                if not check_list[i]:
                    stack.append(i)

    print(count)

                


