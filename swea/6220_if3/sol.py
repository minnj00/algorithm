import sys
sys.stdin = open('input.txt')
#윗 두줄은 항상 쓰기 

char = input()

if char.isupper():
    print(f'{char} 는 대문자 입니다.')
else:
    print(f'{char} 는 소문자 입니다.')

#항상 주의할 것 내가 실행하고 있는 폴더로 이동 (cd ../6220_if3/) 하고 python sol.py 로 실행 