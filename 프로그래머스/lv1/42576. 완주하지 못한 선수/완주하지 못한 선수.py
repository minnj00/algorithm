def solution(participant, completion):
    sumHash = 0
    hashDict = {}
    
    for part in participant:
        hashDict[hash(part)] = part
        sumHash += hash(part)
    for comp in completion:
        sumHash -= hash(comp)
    
    print(sumHash)
    return hashDict[sumHash]
    