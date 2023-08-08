import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

def search(idx,visited):
    
    if idx == N:
        print(result)
        return  # return을 만나면 함수가 종료됨

    for i in range(N):
        if visited[i] == False: 
            # print(idx, i, '=', numbers[idx][i]
            result.append(numbers[idx][i])
            visited[i] = True  # 0번째 열을 골랐습니다 를 표시.  
                            
            search(idx+1, visited) # 그 다음 행에서 하나 고름 
            result.pop() 
            visited[i] = False 
        # 재귀 될 때 pop은 아직 실행이 안됐음. 함수가 끝나는 조건은 return 을 만나거나 함수가 끝까지 실행 되어야만함.
        # search(0) 실행하다가 search(1) 호출 -> s(0)에서 pop이 남아있음.
        # search(1) 실행하다가 search(2) 호출 -> 똑같이 pop() 이 남아있음.
        # search(2) 실행하다가 search(3) 호출 ->
        # search(3) 은 return 을 시행함 -> search(2) 로 돌아감 남아있던 pop() 을 실행 후
        # for i in range(N) 의 반복문이 돌아서 2번째 행의 1, 2번째 열의 값들도 똑같은 시행이 반복됨
        
    


for tc in range(1, T+1):
    N = int(input())
    
    numbers = []
    for _ in range(N):
        number = list(map(int, input().split()))
        numbers.append(number)
    
    result = []
    visited = [False] * N 

    search(0, visited)