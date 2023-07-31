def solution(strlist):
    answer = []
    for i in range(0,len(strlist)):   # in strlist 이렇게 해도 됨
        answer.append(len(strlist[i]))
    return answer