import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

# 터미널 창을 굳이 이 폴더로 옯기지 않아도 실행가능 

T = int(input())

for tc in range(1, T+1):
    # N: 전체 보드의 길이
    # M: 파리채의 길이
    N, M = list(map(int, input().split()))
    matrix = []
    for _ in range(N): 
        row = list(map(int, input().split()))
        matrix.append(row)
    # pprint(matrix)
    total = 0
    
    #파리채를 그리기 위한 기준점을 잡기 위한 반복문 

    for i in range(N - M + 1):
        for j in range(N - M + 1): 
            # 파리채를 그리는 시작점
            # print(matrix[i][j])
            temp_total = 0
            for row in range(M):
                for col in range(M):
                    temp_total += matrix[i+row][j+col]
            if total < temp_total:
                total = temp_total
    print(total)


    # 모양과 범위가 달라지기 때문에 index out of range를 조심하는 연습