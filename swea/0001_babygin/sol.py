# babygin 이면 true 아니면 false 
import sys
sys.stdin = open('input.txt')

# txt 첫번째 4 는 4번 수가 들어올 거야 ! 에 이용
T = int(input())

for tc in range(1, T+1):
    numbers = (input())
    counter = [0 for i in range(10)] # comprehension  i 대신 _ 를 쓰면 변수는 반복문만을 위한거다라는 의미 담음.

    for number in numbers: 
        counter[int(number)] += 1
    
    idx = 0 
    is_babygin = 0 
    while idx < len(counter):
        # 1. triplet 인지 검증
        if counter[idx] >= 3:
            counter[idx] -= 3
            is_babygin += 1 
        
        # 2. run 인지 검증 
        if idx < len(counter)-2:
            if counter[idx] and counter[idx+1] and counter [idx+2]: # 모두가 숫자가 있을 때: 
                is_babygin+=1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
        idx += 1


    if is_babygin == 2:
        print(f'#{tc} True')
    else:
        print(f'#{tc} False')

    

    
    

# 어떤 식으로 접근하면 좋을지 생각해보는 것 먼저 해보기
# 리스트로 변환 후 sort 해보기
# #1 667767 -> [666777] 
# 만약 numbers의 


# 설명 
# 일단 순서대로 정렬 
# 같은 숫자가 몇개 있는지 
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# [0, 0, 0, 0, 0, 0, 3, 3, 0, 0] 이런식으로 6이 3장 7이 3장이면 