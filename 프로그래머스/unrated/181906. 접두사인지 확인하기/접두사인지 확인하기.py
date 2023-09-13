def solution(my_string, is_prefix):
# is_prefix의 길이에 만큼 my_string에서 슬라이싱 했을 때 둘이 같다면 1
# 스트링 슬라이싱 가능
    return 1 if my_string[:len(is_prefix)]==is_prefix else 0