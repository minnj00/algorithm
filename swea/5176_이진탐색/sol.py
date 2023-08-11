import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def inorder(idx):
    global count 
    if idx <= N: # 인덱스 구해야하는 숫자 범위 안에 있는지 확인 
        # 중위순회의 핵심 
        # 왼쪽자식
        inorder(idx*2)
        # 현재노드
        tree[idx] = count 
        count += 1 
        # 오른쪽 자식
        inorder(idx*2 + 1) 

for tc in range(1, T+1):
    N = int(input())

    tree =[0] * (N+1) # 1번 노드부터 N번 노드의 숫자를 인덱스에 맞춰 저장, 0번째 인덱스는 사용하지 않을 것. 

    count = 1
    
    inorder(1)

    print(tree[1], tree[N//2])

