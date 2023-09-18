def solution(arr1, arr2):
    if len(arr1) == len(arr2):
        if sum(arr1) == sum(arr2):
            return 0
    elif len(arr1) > len(arr2):
        return 1
    else: 
        return -1

    # 앞의 경우가 아닌 경우 맨 밑 return 실행
    if sum(arr1) > sum(arr2):
        return 1
    else: 
        return -1