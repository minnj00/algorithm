import sys
from pathlib import Path
from pprint import pprint

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)


T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))

    string_map = []
    for string in range(N): 
        string_map.append(input()) # => 'GOFFAKWFSM' 이게 코드량이 좀 더 적어짐 
        # string_map.append(list(input()))  # => ['G', 'O', ...]   # 중간에 띄어쓰기가 없기 때문에 string을 그냥 list 로 바꿈 (string, list 는 둘다 sequence 데이터이기 때문)
    # print(string_map)

    result = []

    # 가로 기준점을(회문의 시작점) 잡기 위한 코드
    for row in range(N): # 행은 모두 돌려보며 검토
        for col in range(N-M+1): # N-M 만큼 검토
            # print(string_map[row][col])
            for i in range(M//2): # 홀수가 나올 수도 있기 때문에 //2
                # front: 앞 글자
                f = string_map[row][col+i] # i 는 0, 1, 2, 3, 4... 이렇게 증가
                # back: 뒷 글자
                b = string_map[row][col+M-1-i]
                # 앞뒤가 똑같다면
                if f == b:
                    continue # 똑같으면 계속 반복문 진행
                else: 
                    break  # 다르다면 반복문 중단 
            else: # 중간에 break를 만나지 않았을 때, for 문을 끝까지 도는 경우 => 회문을 찾은 경우!!
                for a in range(M):
                    result.append(string_map[row][col+a])
    
    #세로 기준점/ 회문의 시작점을 잡기 위한 코드 
    for col in range(N):
        for row in range(N-M+1):

            for i in range(M//2):
                # front: 앞 글자
                f = string_map[row+i][col] # i 는 0, 1, 2, 3, 4... 이렇게 증가
                # back: 뒷 글자
                b = string_map[row+M-1-i][col]
                # 앞뒤가 똑같다면
                if f == b:
                    continue # 똑같으면 계속 반복문 진행
                else: 
                    break  # 다르다면 반복문 중단 
            else: # 중간에 break를 만나지 않았을 때, for 문을 끝까지 도는 경우 => 회문을 찾은 경우!!
                for a in range(M):
                    result.append(string_map[row+a][col])

    print(''.join(result))
                
# 현재 데이터가 어떻게 출력이 되는지 출력을 해보면서 진행하기 
# 회문 문제로 답변 코드로 프린트해보며 연습하고 밑에 내가 짠 것도 다시 그 방식으로 짜보기 





 



    # matrix = []
    # words =[]
    # for _ in range(N):
    #     matrix.append(list((input())))
    # for i in range(N - M + 1):   #나의 실수: 기준 인덱스의 가로 세로 범위가 다름 
    #     for j in range(N - M + 1):
    #         # 비교해야할 쌍은 회문의 길이의 1/2
    #         temp = [0 for _ in range(M)]
    #         for col in range(int(M / 2)): #홀수이면 뒤에소수점 없앤 만큼만 비교해도 됨 가운데 짝이 없는 중심 이외의 것만 비교하면 되므로
    #             if matrix[i][j+col] == matrix[i][j+M-col-1]:
    #                 temp[col]= matrix[i][j+col]
    #                 temp[M-col-1] = matrix[i][j+M-col-1]
    #             a = []
    #             if i in range(len(temp)):
    #                 if temp[i] != 0:
    #                     a.append(temp[i])
    #             if len(a) == M:
    #                 a = ','.join(a)
    #                 words.append(a)

    #         temp = [0 for _ in range(M)]
    #         for row in range(int(M / 2)):
    #             if matrix[i+row][j] == matrix[i+M-row-1][j]:
    #                 temp[row],temp[M-row-1] = matrix[i+col][j], matrix[i+M-row-1][j]
    #             a = []
    #             if i in range(len(temp)):
    #                 if temp[i] != 0:
    #                     a.append(temp[i])
    #             if len(a) == M:
    #                 a = ','.join(a)
    #                 words.append(a)

    # print(f'#{tc} {words}')
                    
