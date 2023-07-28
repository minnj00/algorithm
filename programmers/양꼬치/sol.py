def solution(n, k):
    # n => 양꼬치 n인분
    # k => 음료수 k개 
    answer = 0
    answer= 12000 * n + 2000 * k - 2000 * (n//10)
    return answer