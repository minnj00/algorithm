def solution(my_string):
    cont = ['a', 'e', 'i', 'o', 'u']
    answer = ''
    # for i in my_string:
    #     if i in cont:
    #         answer = my_string.replace(i, "")
    for i in my_string:
        if i not in cont:
            answer = answer + i
    return answer