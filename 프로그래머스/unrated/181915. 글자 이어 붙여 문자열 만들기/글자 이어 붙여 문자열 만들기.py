def solution(my_string, index_list):
    words = []
    for i in index_list:
        words.append(my_string[i])
    result = ''.join(words)
    return result