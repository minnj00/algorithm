import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))
    # print(N, numbers)
    # import heapq
    # heapq.heapify(numbers)
    # print(numbers) 내장된 라이브러리

    heap = [0] * (N+1)
    heap_size = 0
    for i in range(N):
        heap_size += 1 # 1번노드부터 넣기시작하려고
        # 맨 마지막 노드애 삽입하려는 데이터를 할당
        heap[heap_size] = numbers[i]
        child_idx = heap_size # 부모 인덱스와 비교하기 위함
        parent_idx = child_idx//2 

        # 힙의 조건에 맞도록 교환 반복 
        while parent_idx and heap[parent_idx] > heap[child_idx] != 0: # 부모 인덱스가 0이 아니고, 부모 인덱스보다 자식이 더 작은 경우 
            heap[parent_idx], heap[child_idx] = heap[child_idx], heap[parent_idx] # 바꾸기 

            child_idx = parent_idx  # 또 부모의 부모와 비교하기 위해 
            parent_idx = child_idx // 2 

    node = N//2
    total = 0
    # 조상의 조상의 조상을 찾다가 루트를 찾을 때까지
    while node:
        total += heap[node]
        node //= 2 
    print(total)

 # 노드의 합은 개인적으로 한번 풀어보기 












        
