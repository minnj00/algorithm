import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx,visited, SUM):
    global MIN_SUM
    
    if idx == N:
        if SUM < MIN_SUM:
            MIN_SUM = SUM
        return 

    if  SUM > MIN_SUM:
        return
        

    for i in range(N):
        if visited[i] == False: 
            # print(idx, i)
            # result.append(numbers[idx][i])
            SUM += numbers[idx][i]
            visited[i] = True  # 0번째 열을 골랐습니다 를 표시.  
            search(idx+1, visited, SUM) # 다음 행에서 하나 고름 
            # result.pop() 
            SUM -= numbers[idx][i]
            visited[i] = False 
        # 재귀 될 때 pop은 아직 실행이 안됐음. 함수가 끝나는 조건은 return 을 만나거나 함수가 끝까지 실행 되어야만함.
        # search(0) 실행하다가 search(1) 호출 -> s(0)에서 pop이 남아있음.
        # search(1) 실행하다가 search(2) 호출 -> 똑같이 pop() 이 남아있음.
        # search(2) 실행하다가 search(3) 호출 ->
        # search(3) 은 return 을 시행함 -> search(2) 로 돌아감 남아있던 pop() 을 실행 후
        # for i in range(N) 의 반복문이 돌아서 2번째 행의 1, 2번째 열의 값들도 똑같은 시행이 반복됨
        
    


for tc in range(1, T+1):
    N = int(input())
    
    numbers=[]
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)

    result = []
    visited = [False] * N 

    SUM = 0  # 수조합들의 합을 계산하기 위함. 
    MIN_SUM = 10000000000 # 최종 결과물을 비교하기 위해 사용

    search(0, visited, SUM)
    print(MIN_SUM)






# def link_sum(now):
#     global temp 
#     row += 1
#     for next in matrix[row]:
#         if (matrix[row]).index(next) == i # 다음행에서 새로 더해지는 값의 열이 그 전의 더해졌던 값의 열과 같으면 중단
#             min_sum = min_sum
#         else:
#             temp += next
#             if temp > min_sum:
#                 min_sum = min_sum
#             else: def(next)




# for tc in range(1, T+1):
#     N = int(input())
#     matrix = []
#     for _ in range(N):
#         matrix.append(list(map(int, input().split())))
#     for i in range(N):
#         start = matrix[0][i]
#         row = 0
#         temp = += start



# # mas = [[0, 0, 0], [0, 1, 0]] 
# # print((mas[1]).index(1))
