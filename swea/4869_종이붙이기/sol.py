import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)



# def factorial(n):
#     if n <= 1: 
#         return 1 
#     else:
#         return factorial(n-1) * n 

# T = int(input())


# for tc in range(1, T+1):
#     result = 0
#     length = int(input())
#     for i in range(0, length//20 + 1):
#         # i는 가로 구성에서 20의 개수
#         result += factorial((length-20*i)/10 + i) / factorial((length-20*i)/10) / factorial(i) * (2 ** i)
#         # (20 i 개와 10 들의 구성의 경우의 수) * 
#     print(f'#{tc} {int(result)}')

# 점화식(앞선 값들을 가지고 뒤의 값들을 구한다.)
# n = (n-1) + (n-2) * 2
# ex) 
        
T = int(input())

memo = [0, 1, 3]

for tc in range(1, T+1):
    N = int(input()) // 10
    # memo 배열의 출력시킬 값이 없으면 추가
    while N >= len(memo):
        # n-2 배열에 가로로 작은 사각형 두개 쌓거나 큰 사각형 쌓는 방법 (*2) 
        # n-1 배열에 세로로 작은 사각형 쌓는 방법 하나. 
        # 두 경우는 같은 배열일 경우가 없음.
        temp = 2*memo[len(memo)-2]  + memo[len(memo)-1]
        memo.append(temp)

    print(memo[N])

# 피보나치랑 비슷한 방식
# DP(동적계획법)은 규칙성 찾는 문제여서 여러문제 풀어보며 연습

# 그림 그려가며 규칙성 찾고 점화식 찾기

# 다시 복습하면서 피보나치랑 어떤 게 비슷한지 이해해보기

