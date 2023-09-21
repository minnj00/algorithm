def solution(my_str, parts):
    answer = ''
    for i in range(len(my_str)):
        answer += my_str[i][parts[i][0]:parts[i][1]+1]
    return answer