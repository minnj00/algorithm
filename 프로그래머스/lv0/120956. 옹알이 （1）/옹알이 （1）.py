def solution(babbling):
    answer = 0
    able = ['aya','ye','woo','ma']
    able_combo = []
    able_combo += able
    # 1개조합 able[0], able[1], able[2], able[3] => able 
    # 2개조합 4 * 3 => 01 02 03 10 12 13 20 21 23 30 31 32 33
    # 3개조합 4 * 3 * 2 => 2개 조합의 2배 
    # 4개조합 3개조합에 단어 하나를 더 붙이면 됨.
    for i in range(4):
        for j in range(4):
            if i != j:
                able_combo.append(able[i] + able[j])
                for k in range(4):
                    if k != j:
                        able_combo.append(able[i]+able[j]+able[k])
                        for l in range(4):
                            if k != j:
                                able_combo.append(able[i]+able[j]+able[k]+able[l])
    for word in babbling:
        if word in able_combo:
            answer += 1
    return answer
                        
                    
        
    # for word in babbling:
    #     word.join()
    #     for a in able:
    #         if a in word:
    #             answer += 1
