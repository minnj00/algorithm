import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

def factorial(n):
    if n <= 1: 
        return 1 
    else:
        return factorial(n-1) * n 

T = int(input())


for tc in range(1, T+1):
    result = 0
    length = int(input())
    for i in range(0, length//20 + 1):
        # i는 가로 구성에서 20의 개수
        result += factorial((length-20*i)/10 + i) / factorial((length-20*i)/10) / factorial(i) * (2 ** i)
        # (20 i 개와 10 들의 구성의 경우의 수) * 
    print(f'#{tc} {int(result)}')


        
        
