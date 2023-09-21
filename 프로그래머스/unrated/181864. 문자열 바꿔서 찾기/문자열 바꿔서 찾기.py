def solution(my_str, pat):
    my_str = my_str.replace('A', 'b')
    my_str = my_str.replace('B', 'a')
    my_str = my_str.replace('a', 'A')
    my_str = my_str.replace('b', 'B')
    if pat in my_str:
        return 1
    else:
        return 0
        