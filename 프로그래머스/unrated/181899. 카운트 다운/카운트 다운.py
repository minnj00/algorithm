def solution(start, end_num):
    result = []
    for i in range(start, end_num-1, -1):
        result.append(i)
    return result