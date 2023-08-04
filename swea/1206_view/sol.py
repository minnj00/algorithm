import sys
sys.stdin = open('input.txt')

for TC in range(1,11):
    building_num = int(input())
    buildings = list(map(int,input().split()))
    # # print(building_num, buildings, len(buildings))
    # count = 0
    # for i in range(2, building_num-2): # 처음에 내 코드 오류났던 이유: range 설정을 잘못함 -> 계속 그림으로 그려가며 연습하기 
    #     gap_1 = buildings[i] - buildings[i-1]
    #     gap_2 = buildings[i] - buildings[i-2]
    #     gap_3 = buildings[i] - buildings[i+1]
    #     gap_4 = buildings[i] - buildings[i+2]
    #     gaps=[gap_1, gap_2, gap_3, gap_4]
    #     if min(gaps) <= 0:
    #         count = count
    #     else:
    #         count += min(gaps)
    # print(f'#{TC} {count}')

    total = 0 
    #선생님
    for i in range(building_num): # 건물 개수만큼 반복 
        now = buildings[i] # 기준으로 생각할 빌딩
        if now == 0: #현재 위치에 건물이 없다면 다음 건물로 이동 
            continue
        else:
            # 양옆 * 2 건물의 높이를 비교 
            dx = [-2, -1, 1, 2] # delta x list를 이용하여 나를 기준으로 변화를 줘야 할 부분을 반복문으로 풀어냄 (나중에 이 부분이 가변적일 수 있으므로 유용)
            max_tall = 0
            for j in range(4):
                # i: 현재위치
                # dx[j]: 기준건물 중심으로 좌우 인덱스 
                comp = buildings[i+dx[j]] # j 에는 -2, -1, 1, 2 가 들어올것 
                
                if max_tall < comp:
                    max_tall = comp
            #나머지 4개의 건물보다 내가 더 크다면 조망권 확보 
            if now > max_tall: 
                view = now - max_tall
                total += view 

    print(f'#{TC} {total}')

