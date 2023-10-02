def solution(n, lost, reserve):
    stu = [1 for i in range(n+2)]
    for i in reserve:
        stu[i] = 2
    for i in lost:
        stu[i] -= 1
    # print(stu)
    
    for i in range(1, n+1):
        if stu[i] == 0:
        # print(stu)
            if stu[i-1] == 2: 
                stu[i] = 1
                stu[i-1] = 1
                

            elif stu[i+1] == 2:
                stu[i] = 1
                stu[i+1] = 1
                
    count = 0     
    for i in stu:
        if i >= 1:
            count += 1
    return count - 2
    
        