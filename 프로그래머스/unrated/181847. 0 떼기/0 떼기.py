def solution(n_str):
    # 0인 부분을 다 공백으로 바꾸기
    # .lstrip() 으로 왼쪽 공백 삭제한 후 다시 공백을 0으로 바꾸기
    n_str = n_str.replace('0', ' ')
    n_str = n_str.lstrip()
    n_str = n_str.replace(' ', '0')
    return n_str