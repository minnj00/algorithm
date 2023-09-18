def solution(s):
    if len(s) == 4 or len(s) == 6:
        # 숫자로만 되어있으면 True
        # 현재 모든 s
        try:
            num = int(s)
            return True
        except:
            isinstance(s,int)

    return False