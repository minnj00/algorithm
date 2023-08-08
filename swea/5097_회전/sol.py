import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    # for _ in range(M):
    #     data = numbers.pop(0)
    #     numbers.append(data)

        # front = numbers[0]
        # numbers.remove(numbers[0])
        # numbers.append(front)
    
    remain = M % N 
    print(numbers[remain])

    

    # print (f'{tc} {numbers[0]}')

# 다른 풀이 
# 숫자가 3개일 때 횟수로 숫자의 개수를 나눈 나머지 만큼만 이동해도 됨. or remain 의 인덱스로 리스트 접근함.
        
