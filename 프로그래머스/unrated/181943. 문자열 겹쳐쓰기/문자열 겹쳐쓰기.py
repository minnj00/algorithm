def solution(my_str, over, s):
    answer = my_str[:s] + over + my_str[s+len(over):]
    return answer