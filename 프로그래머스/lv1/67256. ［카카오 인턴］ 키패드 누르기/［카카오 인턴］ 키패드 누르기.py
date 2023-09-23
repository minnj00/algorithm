def solution(numbers, hand):
    result = ''
    key = [[0 for _ in range(3)] for _ in range(4)]
    # 숫자 별 위치(행, 열)로 된 리스트
    loc_list = [[3, 1], [0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
    left = [3, 0]
    left_d = 0
    right = [3, 2]
    right_d = 0
    for i in numbers:
        # 1, 4, 7일 경우 왼손의 위치를 i의 위치로 변경 후 result 에 L 추가
        if i%3 == 1:
            left = loc_list[i]
            result += 'L'
        # 3, 6, 9일 경우 오른손의 위치를 i의 위치로 변경 후 result 에 R 추가
        elif i%3 == 0 and i != 0:
            right = loc_list[i]
            result += 'R'
        # 2, 4, 6 일 경우 두 손가락으로부터의 거리 비교 행, 열 간격
        elif i == 0 or i%3 == 2:
            left_d = abs(left[0] - loc_list[i][0]) + abs(left[1] - loc_list[i][1])
            right_d = abs(right[0] - loc_list[i][0]) + abs(right[1] - loc_list[i][1])
            print(left, loc_list[i], right)
            print(left_d, right_d)
            # left_d 가 더 작으면 왼손이 이동, result에 L추가
            if left_d < right_d:
                left = loc_list[i]
                result += 'L'
            elif left_d > right_d:
                right = loc_list[i]
                result += 'R'
            else:
                if hand == 'left':
                    left = loc_list[i]
                    result += 'L'
                else: 
                    right = loc_list[i]
                    result += 'R'
    
    return result