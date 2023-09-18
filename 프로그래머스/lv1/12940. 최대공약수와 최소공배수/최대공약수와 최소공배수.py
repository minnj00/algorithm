def solution(n, m):
    list_a = []
    num = 0
    min_num = min(n, m) 
    max_num = max(n, m) 
    print(max_num % min_num)
    for i in range(1, m+1):
    # 1부터 m까지의 정수 중 n과 m의 약수를 list에 넣기
        if n%i == 0 and m%i == 0:
            list_a.append(i)
    if max_num % min_num  == 0:
        num = max_num
    else:
        for i in range(max_num, n*m+1):
            if n*m % i == 0 and i%n == 0 and i%m == 0:
                num = i
                return [max(list_a), num]
    return [max(list_a), num]
    