import math

def solution(n):
    sqrtsum = 0
    if n % 2:
        return sum(range(1, n+1, 2))
    else:
        for i in range(2 , n+1, 2):
            sqrtsum += i**2
        return sqrtsum