def solution(babbling):
    # 발음할 수 있는 단어 리스트 인덱스로 babbling 을 바꿔주기
    able = {'1': "aya", '2': "ye",'3': "woo", '4': "ma"}
    conv = []
    
    for j in babbling:
        temp = j
        for k, v in able.items():
            if v*2 not in temp:
                temp = temp.replace(v, k)
            else:
                break
        # 발음할 수 있는 단어들로 이루어진 것들만
        # for i in ['11', '22', '33', '44']:
        #     if i in temp:
        #         break
        # 연속되는 숫자가 없어서 for 문이 다 돌면
        else:
            try:         
                temp = int(temp)
                conv.append(temp)
            except:
                continue
        
    return len(conv)
    