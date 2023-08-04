import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())

    matrix = []
    # 원래는 i, j, a 등 반복문을 돌리는 요소를 임시로 저장하는 변수
    # _ => 변수를 활용하지 않을 예정이라서 변수 이름을 비워놓겠다. _가 변수 이름이긴 함. 
    for _ in range(100): # 인풋으로 받은 한 줄을 쪼개고 리스트로 만들어 매트릭스에 저장 -> 100번반복
        row = list(map(int,input().split())) 
        matrix.append(row)

    total = 0

    #가로줄 반복
    for row in range(len(matrix)):
        temp = 0 # 임시변수 (가로줄 한줄의 합) -> 가로줄 한줄이 끝날 때마다 0이 됨. 위치 조심하기 
        for col in range(len(matrix[0])): #2차원 리스트의 한 행에 있는 수의 개수 = 열의 개수 
            temp += matrix[row][col] 
        if total < temp:
            total = temp # 구간합과 동일함. 더한 값이 temp 보다 크면 갈아끼워주기
    #세로줄 반복
    for col in range(100):
        temp = 0
        for row in range(100):
            temp += matrix[row][col]
        if total < temp:
            total = temp
    # 좌 상단 => 우하단 반복
    for i in range(100): # 이 방향 대각선은 행과 열이 같이 늘어남 
        temp = 0
        temp += matrix[i][i]
    if total < temp:
        total = temp
    # 우상단 => 좌하단 
    for i in range(100): #이 방향 대각선은 행은 늘어나고 열은 99에서 -0, -1 ... 가 더해져 줄어듬.
        temp = 0
        temp += matrix[i][99-i]
    if total < temp:
        total = temp
    #규칙이 잘 떠오르지 않을 때는 행열의 위치를 다 적어보고 규칙을 찾기

    print(f'#{tc} {total}')
    
        




# for tc in range(1,11):
#     tc = int(input())
#     matrix = []
#     sum_list = []
#     for i in range(100):
#         numbers = list(map(int, input().split()))
#         matrix.append(numbers)
#     row_sum = []
#     for row in range(100):
#         sum_r = 0
#         for col in range(100):
#             sum_r += matrix[row][col]
#         row_sum.append(sum_r)
#     col_sum = []
#     for col in range(100):
#         sum_c = 0
#         for row in range(100):
#             sum_c += matrix[row][col]
#         col_sum.append(sum_c)
#     dig_sum = []
#     sum_d = 0 #대각선의 합
#     for i in range(100):
#         sum_d += matrix[i][i]
#

#     sum_list.extend(row_sum)
#     sum_list.extend(col_sum)
#     sum_list.append(sum_d)

#     print(f'#{tc} {max(sum_list)}')




         





