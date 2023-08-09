import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int,input().split()))
    # N: 화덕의 크기, M: 피자 개수 

    Ci= list(map(int,input().split()))

    # 피자의 번호를 부여하는 과정
    # 구워지기 전 피자
    before = []
    for i in range(M):
        before.append([Ci[i],i])
    

    # 화덕
    queue = [0] * N

    # 완성피자를 저장할 목록, 맨 마지막에 들어오는 피자가 result 피자
    after = []

    # 완성피자가 구워야 하는 피자 갯수랑 같아질 때까지 반복
    while len(after)!= M: 
        # 화덕 입구에 공간이 비어있으면 화덕리스트에서 
        if queue[0] == 0:
            # 넣을 피자가 있으면
            if len(before) != 0:
                # 남은 첫번째 치즈와 번호 
                cheeze, idx = before.pop(0) # 첫번째 피자를 빼오기  cheeze 에 치즈의 양 idx에 피자번호 할당
                # 화덕에 넣기
                queue.append([cheeze, idx]) # 화덕 리스트에서 화덕의 입구는 뒷쪽으로 생각 
                # 화덕 돌리기
                queue.pop(0) # 화덕 입구로 피자를 넣으면 
            else: 
                queue.pop(0) # 0 번째 값 삭제 후
                queue.append(0) # 맨 끝에 0 넣기 
                #-> 한칸씩 이동 
        else: #화덕 입구에 공간이 없으면(이미 구워지고 있는 피자가 있는 경우)
            # 치즈 절반 감소
            queue[0][0] //= 2 
            # 치즈가 다 녹았는지 확인
            if queue[0][0] == 0:
                # 완성된 피자 꺼내기
                pizza = queue.pop(0)
                # 완성목록에 넣기
                after.append(pizza)
                if len(before) != 0:
                    # 남은 첫번째 치즈와 번호 
                    cheeze, idx = before.pop(0) # 첫번째 피자를 빼오기 
                    # 화덕에 넣기
                    queue.append([cheeze, idx])
                    # 넣을 피자가 없으면 비어있는 판 뒤에 추가 
                else: 
                    queue.append(0)
            # 아직 더 돌려야 하는 경우
            else:
                queue.append(queue.pop(0))
    print(after›)

    # after = []   
    # for i in range(N):
    #     fire.append(pizza_idx[0])
    #     pizza_idx.remove(pizza_idx[0])
    # print(pizza_idx)
    # print(fire)
            

    # while len(fire) != 1:
    #     if fire[0][1] == 0:
    #         fire[0] = pizza_idx[0]

    #     for i in range(N):
    #         fire[i][1]=fire[i-1][1]
    #     ffire[i][1] = fire[i][1]//2
        
        




        
        
