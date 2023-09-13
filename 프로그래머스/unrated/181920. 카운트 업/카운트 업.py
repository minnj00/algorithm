def solution(start_num, end_num):
    list = []
    for i in range(end_num-start_num+1):
        list.append(start_num)
        start_num += 1
    return list