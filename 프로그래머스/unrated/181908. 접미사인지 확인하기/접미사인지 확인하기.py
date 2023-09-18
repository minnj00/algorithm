def solution(my_string, is_suffix):
    str_idx = len(my_string)-1
    # is_suffix의 글자수만큼 my_string 뒤에서부터 슬라이싱했을 때 같으면 1
    # print(my_string[str_idx-len(is_suffix)+1:])
    return int(my_string[str_idx-len(is_suffix)+1:] == is_suffix)