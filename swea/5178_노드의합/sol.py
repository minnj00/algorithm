import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # N: 노드의 개수
    # M: 리프노드의 개수
    # L: 값을 출력할 노드 번호 
    N, M, L = list(map(int, input().split()))
    
    
    tree = [0] * (N+1)
    
    for _ in range(M):
        a, b = list(map(int, input().split()))
        tree[a] = b


    if N % 2: # N 이 홀수면
        for i in range(N, 3, -2):
            child_right = i
            child_left = i-1
            tree[i//2] = tree[i] + tree[i-1]
    else:
        tree[N//2] = tree[N]
        for i in range(N-1, 3, -2):
            child_right = i
            child_left = i-1
            tree[i//2] = tree[i] + tree[i-1]
    print(tree[L])
