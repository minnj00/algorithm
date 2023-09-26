from string import ascii_lowercase
def solution(s, skip, n):
    result = ''
    apb_list = list(ascii_lowercase)
    for i in skip:
        if i in apb_list:
            apb_list.remove(i)
    
    # s = list(s)
    for j in s:
        result += apb_list[(apb_list.index(j) + n)%(len(apb_list))]

    return result