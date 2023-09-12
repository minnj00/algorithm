def solution(my_string):
    numcal = my_string.split()
    result = int(numcal[0])
    for i in range(1,len(numcal)-1, 2):
        print(numcal[i])
        if numcal[i] == '+':
            result += int(numcal[i+1])
        else:
            result -= int(numcal[i+1])
    return result
            
        