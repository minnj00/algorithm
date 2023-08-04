numbers = [2, 3, 7, 8, 1]

# 부분집합을 구하는 배열의 길이
n = len(numbers)

# 결국 목적은 

# 모든 부분집합의 경우의 수 만큼 반복문을 실행 
for i in range(1<<n): 
    print(i, bin(i)) # bin: 숫자를 2진수로 표현
    temp = []
    for j in range(n):
        print(bin(i), bin(1<<j))
        if i & (1<<j):   # 1, 10, 100, 1000, 10000 과 i 를 비교하며 그 자리에 숫자가 있는지 확인 
            temp.append(numbers[j])
    print(temp) 
    