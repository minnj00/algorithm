def solution(arr):
    stk = []
    for i in range(len(arr)):
        if len(stk) == 0:
            stk.append(arr[i])
        elif arr[i] == stk[-1]:
            stk.pop(-1)
        else:
            stk.append(arr[i])
    # return [-1] if len(stk) == 0 else stk
    return stk or [-1]
        