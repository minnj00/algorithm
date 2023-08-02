import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    # 여기까지의 코드를 자주 쓸 예정이므로 복붙하는 것도 하나의 방법
    N = int(input())
    numbers = list(map(int, input().split()))
    # numbers.sort()
    # 정렬 후 큰 수 작은 수 뽑아서 연산
    # result = numbers[-1]- numbers[0]

    # print(f'#{tc} {result}')
    # min_number = 1000000000 # 이 기본값은 문제에 주어진 기본값을 참고해서 설정하기 
    min_number = numbers[0]
    # max_number = 0
    max_number = numbers[0]

    for number in numbers:
        if min_number > number:
            min_number = number
        
        if max_number < number:
            max_number = number
    
    result = max_number - min_number
        
    print(f'#{tc} {result}')
