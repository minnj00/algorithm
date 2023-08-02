import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # N: 정수의 개수
    # M: 구간의 개수
    N, M = map(int, input().split())
    numbers = list(map(int, input(()).split()))
   
    min_total = 1000000 #(N최댓값 * M 최댓값)
    max_total = 0
    # 구간함을 구하기 위한 i => 뒤의 M개의 데이터를 더하기 위한 시작점 
    # index out of range 에러를 발생시키지 않기 위해
    for i in range(N-M+1): # 이때 i 는 합들의 시작 인덱스 
        total = 0
        for j in range(M): # 시작점을 기준으로 오른쪽 M개를 구하기 위한 반복
            total = total + numbers[i+j]
            # total += numbers[i]
            # i += 1
            
        if min_total > total:
            min_total = total

        if max_total < total:
            max_total = total
    result = max_total - min_total

    print(f'#{tc} {result}')