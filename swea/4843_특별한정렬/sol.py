import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

# for tc in range(1, T+1):
#     # 가장 큰수 , 가장 작은 수 , 2번째 큰수, 두번째 작은수 ... 10개
#     # 인덱스로 표현하면 -1, 0, -2, 1, -3, 2, -4, 3, -5, 4
#     n = int(input())
#     numbers = list(map(int, input().split()))
#     numbers.sort()
#     temp = []
#     for i in range(5):
#         temp.append(numbers[-i-1])
#         temp.append(numbers[i])
#     print(f'#{tc} {temp}')

# 선택정렬방법 

for tc in range(1, T+1):
    N= int(input())
    numbers = list(map(int, input().split()))

    result = []
    while len(numbers): # numbers 숫자가 사라질 때까지
        max_num = 0
        for m in range(len(numbers)):
            if max_num < numbers[m]:
                max_num = numbers[m]
        result.append(max_num)
        numbers.remove(max_num)

        min_num = 10000000
        for n in range(len(numbers)):
            if min_num > numbers[n]:
                min_num = numbers[n]
        result.append(min_num)
        numbers.remove(min_num)

        if len(result) == 10:
            break 

    print(result)




            

        
