def solution(s):
    count = 0
    Dict = {}
    for i in s:
        if not len(Dict.keys()):
            print(i)
            Dict[i] = 1
            
        elif i in Dict:
            Dict[i] += 1
                    
        elif len(Dict.keys()) == 1:
            Dict['oth'] = 1
            if Dict[list(Dict.keys())[0]] == Dict['oth']:
                count += 1
                print(f'{Dict} 1')
                Dict.clear()
                
        elif len(Dict.keys()) == 2:
            Dict['oth'] += 1
            if Dict[list(Dict.keys())[0]] == Dict['oth']:
                count += 1
                print(f'{Dict} 2')
                Dict.clear()
    if len(Dict):
        count += 1
    return count
        
    