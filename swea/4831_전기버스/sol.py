import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    K, N, M = map(int,input().split())
    bus_stop = list(map(int, input().split()))
    #K: 최대로 이동 가능한 정류장 수
    #N: 종점
    #M: 충전기가 설치된 정류장 수 
    count = 0
    now = 0 #현재 버스의 위치
    #충전할 필요가 없이 바로 도착하는 경우
    if K >= N:
        count = 0 
    # 충전을 하면서 지나가야 할 때 
    else: 
        # 버스가 아직 종점에 도착하지 않았다면 계속해서 반복
        while now < N: 
            # 현재 위치에서 최대로 갈 수 있는 범위를 찾는다.
            # 최대로 갈 수 있는 범위 부터 현재위치까지 반복
            for i in range(now + K, now, -1):
                # 1. 최대범위가 종점을 넘는 경우 
                if i >= N:
                    now = N
                    break

                # 2. 최대범위가 종점을 아직 넘지 않은 경우
                if i in bus_stop:
                    # 가장 뒤에 있는 충전소로 이동 
                    now = i
                    # 충전을 하고 이동을 했으니 카운트 증가
                    count += 1
                    # 마지막 충전소를 찾았으니 더이상 후진할 필요 없음 
                    break 
            # 현재 위치에서 최대 거리를 찾았는데, 충전소가 없다면? => 도착 불가능  
            else: # for 문과 연결되는 else 문 for 문을 다 돌고 브레이트가 걸리지 않았을 때
                count = 0
                now = N 
                

    print(f'#{tc} {count}')

# 인덱스를 활용해서 코드를 짤 수 있는가만 집중하기
# 한 문제에 너무 매몰되지 않기!


    

    # info = list(map(int, input().split()))
    # K = info[0]
    # N = info[1]
    # M = info[2]
    # chargers = list(map(int,input().split()))
    # # print(K)
    # # print(N)
    # # print(M)
    # # print(chargers)

    # # for i in range(len(chargers)-1):
    # #     if chargers[i+1] - chargers[i] > K:
    # #         print(f'#{tc} 0')
    # #         break
    # power = K
    # loc = 0
    # charge = 0
    # while loc != N:
    #     power -= 1
    #     loc += 1 
    #     if loc == N:
    #         result = charge
    #         break
    #     elif loc in chargers:
    #         if chargers.index(loc) != M-1:
    #             if chargers[chargers.index(loc)+1] - loc > power:
    #                 charge += 1
    #                 power = K            
    #     elif power == 0: 
    #         result = charge

    # print(f'#{tc} {result}')

    
    
        


    
