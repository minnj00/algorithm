def solution(n):
    answer = []
    for i in range(int(n/2)):
        answer.append(2*i + 1)
    if n % 2 == 1:
        answer.append(n)
    return answer