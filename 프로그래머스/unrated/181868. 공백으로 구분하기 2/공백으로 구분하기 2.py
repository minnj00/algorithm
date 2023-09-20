def solution(my_str):
    my_str = my_str.strip()
    my_str = my_str.replace(' ', ',')
    my_str = my_str.split(',')
    my_str = [i for i in my_str if i]
    return my_str