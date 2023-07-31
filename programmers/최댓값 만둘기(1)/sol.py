# def solution(numbers):
#     answer = 0
#     max_1 = 0
#     max_1 = (max(numbers))
#     numbers.remove(max_1)
#     max_2 = max(numbers)
#     answer = max_1 * max_2
#     return answer

#선생님: 두 수의 곱의 모든 경우를 비교 

def solution(numbers):  ## 이부분다시이히해보고 선생님 필기랑 비교확인
    answer = 0
    #0번째 숫자 -> 1, 2, 3, 4 번째 숫자랑 곱해보기
    #1-> 2, 3, 4 번째 숫자랑 곱
    #2-> 3, 4번째 숫자랑 곱
    #3 -> 4번째 숫자랑 곱
    for i in range(len(numbers)):
        for j in range(i,len(numbers)-1):
            result = numbers[i] * numbers[j]
            if answer < result: 
                answer = result

    return answer 
         
        
# 숫자 리스트를 정렬하고 젤 큰 숫자 두개를 뽑으면 됨 
def solution(numbers):
    answer = 0
    numbers.sort(reverse=True)
    answer = numbers [1] * numbers[0]

    return answer 

