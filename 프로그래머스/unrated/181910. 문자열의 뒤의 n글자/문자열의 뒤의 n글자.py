def solution(my_string, n):
# 0부터 len(my_string)-1까지 len(my_string)글자로 되어있을 때 
# k부터 len(my_string)-1인덱스까지가 n글자가 되어야 한다. len(my_string)-k = n
    # return(my_string[len(my_string)-n:])
    return(my_string[-n:])

