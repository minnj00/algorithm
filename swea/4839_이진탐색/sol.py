import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    # P: 책의 장수
    # A: A가 찾아야 하는 목적 페이지
    # B: B가 찾아야 하는 목적 페이지
    P, A, B= list(map(int,input().split()))
    
    count_a = 0 
    left = 1 
    right = P 

    while True: # 무한하게 반복하다가 목적 페이지에 도착을 하면 break 로 종료 
        middle = int((left+right)/2) # 반을 찾고 해당하지 않는 범위를 버려야 하니깐 left나 right 값을 변경해줌
    
        # 목적페이지가 가운데보다 왼쪽에 있는 경우
        if A < middle:
            right = middle 
        # 목적페이지가 가운데보다 오른쪽에 있는 경우
        elif A > middle: 
            left = middle 
        # 둘다 아니라면 목적 페이지에 도착 !!! break 로 while 문을 종료시켜줌
        else: 
            break 

        count_a += 1 

    count_b = 0
    left = 1 
    right = P 

    while True: # 무한하게 반복하다가 목적 페이지에 도착을 하면 break 로 종료 
        middle = int((left+right)/2) # 반을 찾고 해당하지 않는 범위를 버려야 하니깐 left나 right 값을 변경해줌
    
        # 목적페이지가 가운데보다 왼쪽에 있는 경우
        if B < middle:
            right = middle 
        # 목적페이지가 가운데보다 오른쪽에 있는 경우
        elif B > middle: 
            left = middle 
        # 둘다 아니라면 목적 페이지에 도착 !!! break 로 while 문을 종료시켜줌
        else: 
            break 

        count_b += 1 
    print(count_a, count_b)