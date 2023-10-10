def solution(lottos, win_nums):
    answer = []
    # 최저순위는 내 번호와 당첨번호 집합의 교집합 원소
    minscore = len(set(lottos) & set(win_nums))
    if not minscore:
        minrank = 6
    else:
        minrank = 7 - minscore

    maxscore = minscore + lottos.count(0)
    if not maxscore:
        maxrank = 6
    else:
        maxrank = 7 - maxscore
    return [maxrank, minrank]
    
    
    