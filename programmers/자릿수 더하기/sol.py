# def solution(n):
#     answer = 0
#     numbers = list(str(n))
#     numbers_int= map(int, numbers)
#     answer = sum(numbers_int)
#     return answer


#또 다른 파이썬 방법
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer 
print(solution(1234))


# 몫과 나머지를 이용하는 경우 ... 10으로 나눌 때마다 나오는 나머지를 더하기
# def solution(n):
#     answer = 0
#     while n > 0:
#         a, b = divmod(n, 10) #더 이상 10으로 나눌 수 없을 때까지 반복
#         n = a 
#         answer += b 
#     return answer 