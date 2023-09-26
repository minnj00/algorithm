def solution(keymap, targets):
    result = []
    for k in range(len(keymap)):
        keymap[k] = list(keymap[k])
    # [[A, B, A, C, D], [B, C, E, F, D]]
    for i in targets:
        temp = 0
        for j in i:
        # target의 텍스트의 알파벳마다 반복
            min_idx = 101
            for n in keymap:
                try:
                # keymap에 있는 key에서 그 알파벳이 해당하는 최소 인덱스를 추출하기 
                    if n.index(j) < min_idx:
                        min_idx = n.index(j)
                except:
                    continue
            if min_idx == 101:
                # result.append(-1)
                temp = -1
                break
            else:
                temp += min_idx + 1 # 눌러야 하는 횟수를 temp에 반복해서 더하기
        result.append(temp)
    return result
            