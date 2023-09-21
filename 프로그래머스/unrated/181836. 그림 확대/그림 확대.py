def solution(picture, k):
    # 스트링 (원소)의 모든 글자를 k배로 늘려주기
    large = []
    for i in picture:
        str = ''
        for j in i:
            str += j*k
        for i in range(k):
            large.append(str)
        
    
        
    return large
        
            
    # k간격으로 인덱스에 있는 원소의 개수를 늘려주기
    