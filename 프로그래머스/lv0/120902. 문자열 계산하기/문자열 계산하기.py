def solution(my_string):
    numcal = my_string.split() # ['3', '+', '4', '-', '2']
    result = int(numcal[0])
    
    for i in range(1,len(numcal)-1, 2):
        if numcal[i] == '+':
            result += int(numcal[i+1])
        else:
            result -= int(numcal[i+1])
    return result
    
    # nums = map(int, my_string.replace(' - ', ' + -').split(' + '))     
    # result = sum(nums)
    # return result
        