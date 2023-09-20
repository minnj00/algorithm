def solution(str_list, ex):
    result = ''
    for i in str_list:
        if not ex in i:
            result += i
    return result