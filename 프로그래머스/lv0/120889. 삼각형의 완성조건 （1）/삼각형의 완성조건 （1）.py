def solution(sides):
    answer = 0
    if 2* max(sides) < sum(sides):
        answer = 1
    else: 
        answer = 2
        
    return answer