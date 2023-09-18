def solution(spell, dic):
    for i in range(len(dic)):
        mylist = []
        for j in dic[i]:
            if j in spell:
                mylist.append(j)
            count = 0
            myset = set(mylist)
            # 각 단어별로 spell 에 해당하는 철자를 저장한 mylist
            # mylist의 원소들을 중복된 값들을 제거한 후 myset에 저장한 후
            # myset과 spell의 겹치는 원소만큼 count 해줌
            for l in list(myset):
                if l in spell:
                    count += 1
            if count == len(spell):
            # 겹치는 원소의 개수가 spell 원소의 개수랑 같아야만 spell의 원소가 한번씩은 사용된 것
                return 1
        print(mylist)

    return 2