memo = [0, 1] # f(0), f(1)을 저장해놓고 f(2), f(3) ... 을 순차대로 저장함

def fibo(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

print(memo)
print(fibo(100))

# 원래라면 f(6) 을 실행했을 때 f(4) f(5) 호출 ...계속 호출 
# 불필요한 계산 중복을 줄여줌. 

