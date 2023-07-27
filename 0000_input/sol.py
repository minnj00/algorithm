import sys
sys.stdin = open('input.txt') #txt 파일을 가져와서 저장

# N = int(input()) # 이 input함수를 만날때마다 stdin에서 한줄씩 꺼내옴

# print(N)

# if N % 2 == 1:
#     print('홀수')
# else: 
#     print('짝수')


# N = int(input())

# print(N)

# if N % 2 == 1:
#     print('홀수')
# else: 
#     print('짝수')

TC = int(input()) #9가 불러와짐

for i in range(TC): #1, 2, 3, 4, 5, ... 이 불러와짐 (총9번)
    N = int(input())
    if N % 2 == 1:
        print('홀수')
    else:
        print('짝수')
    

# numbers = input().split()
# print(numbers)
# for number in numbers:
#     int_num = int(number)

#     if int_num % 2 ==1:
#         print (f'{int_num}은 홀수 입니다.')


numbers = list(map(int,input().split())) #스플릿 한 것들을 int 씌움 
print(numbers)

for number in numbers:
    if number % 2 ==1:
         print (f'{number}은 홀수 입니다.')

# 2차원 리스트 input 받기 
N = int(input())
matrix = []

for i in range(N):
    numbers = list(map(int,input().split()))
    matrix.append(numbers)
    
print(matrix)

#2중 반복문으로
for row in matrix:
    # print(row)
    for item in row:
        if item == 5:
            print('5가 있습니다')
        