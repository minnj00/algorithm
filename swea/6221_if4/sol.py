import sys
sys.stdin = open('input.txt')

# a = input()
# b = input()


# if a == '바위':
#     if b == '보':
#         print('Result : Man1 Lose!')
#     elif b == '가위':
#         print('Result : Man1 Win!')
#     else:
#         print(print('Result : Draw'))

#선생님 답변

# 1. 모든 경우를 다 적는 경우 
# man1 = input()
# man2 = input()

# if man1 == '가위' and man2 == '가위':
#     print('Result : Draw')
# elif man1 == '가위' and man2 == '바위':
#     print('Result : Man2 Win!')
# elif man1 == '가위' and man2 == '보':
#     print('Result : Man1 Win!')







# 가위, 바위, 보 
# 0, 1, 2 [가위, 바위, 보] 리스트의 인덱스 

#비긴 경우 제외 경우의 수
#보, (가위) 2win 2-0 2
#(바위), 가위 1win 1-0 1
#(보), 바위 1win 2-1 1
#가위, (바위) 2win 0-1 -1
#바위, (보) 2win 1-2 -1
#(가위), 보 1win 0-2 -2


man1 = input()
man2 = input()

rcp = ['가위', '바위', '보']

man1_idx = rcp.index(man1)
man2_idx = rcp.index(man2)


result = man1_idx - man2_idx

if result == 0: 
    print('Result : Draw')
elif result > 0:
    print(f'Result : Man{result} Win!')
else:
    if result == -1:
        print('Result : Man2 Win!')
    else: 
        print('Result : Man1 Win!')
