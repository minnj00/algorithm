def solution(sides):
    count = 0
    # sides 이외의 변의 길이가 1부터 sides의 max보다 짧은 
    for i in range(1, max(sides)):
        if max(sides) < sum(sides) - max(sides) + i:
            count += 1
    
    # sides 외의 변의 길이가 max(sides) 보다 크거나 같아서 sum(sides)보다 작아야 하는 경우 
    for i in range(max(sides), sum(sides)):
        count += 1
    return count