memo = [1, 1] # f(0), f(1)을 저장해놓고 f(2), f(3) ... 을 순차대로 저장함

def fibo(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

print(memo)
print(fibo(100))
print(fibo(2))

# 원래라면 f(6) 을 실행했을 때 f(4) f(5) 호출 ...계속 호출 
# 불필요한 계산 중복을 줄여줌. 

# fibo(0) -> memo[0]
# fibo(1) -> memo[1]
# fibo(2) -> n>=2 이고 len(memo) <= 2 이므로 memo.append(fibo(0) + fibo(1)) 실행.
# 이에 따라 f(0) -> return memo[0] 다음 f(1) -> return memo[1] 후 실행하던 f(2) 마저 실행하면 return 새로생긴 memo[2](memo[0]+memo[1]) 가 출력됨
fibo(4)의 경우
fibo(4) 시행 memo.append(fibo(3)+fibo(2))에 따라
fibo(3)를 시행 하면 memo.append(fibo(2)+fibo(1)) 에 따라
fibo(2)를 시행하면 memo.append(fibo(1)+fibo(0))에 따라
fibo(1)->return memo[1]
fibo(0)->return memo[0]
fibo(2)를 시행하던 것으로 마저 돌아가면 memo.append(memo[1]+memo[0])하고 return(memo[2]) fibo(3) 의 fibo(1) 시행하면 바로 return 
# 이렇게 f(2), f(3) ... 의 값을 저장해놓기 때문에 fibo(100) 과 같이 피보나치 수열의 큰 값을 계산할 때도 속도가 더 빨라짐 
