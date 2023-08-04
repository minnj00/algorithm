import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    numbers = list(range(1, 13)) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    N, K = list(map(int, input().split()))

    count = 0 
    for i in range(1 << len(numbers)): # 모든 경우의 수는 2 ** 12 (1<<12)


        for j in range(len(numbers)): 
            temp = []
            if i & (1 << j):
                temp.append(numbers[j])
        
        if len(temp) == N and sum(temp) == K:
            count+= 1

        print(count)



