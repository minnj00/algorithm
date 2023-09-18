def solution(my_string, queries):
    my_list = list(my_string)
    for s, e in queries:
        
        my_list[s:e+1] = my_list[s:e+1][::-1]
        
    my_string = ''.join(my_list)
        
    return my_string
    
        
        