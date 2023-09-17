
import math

def solution(n):
    answer = 2
    sqrt_num = math.sqrt(n)
    
    if sqrt_num.is_integer():
        answer = 1
    return answer
