def solution(n):
    answer = 0 
    for i in range(1,n+1):
        if i % 2 == 0:
            answer += i
        else: 
            continue
    return answer 


def solution(n):
    answer = []
    for i in range(n+1):
        if i%2==0:
            answer.append(i)
    return sum(answer)

 def solution(n):
    answer = []

    a = range(2, n+1, 2)
    print(sum(a))
    
    return sum(answer)

    