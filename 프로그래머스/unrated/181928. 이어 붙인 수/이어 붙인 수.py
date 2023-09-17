def solution(num_list):
    odd = []
    even = []
    for i in num_list:
        if i % 2:
            even.append(i)
        else: 
            odd.append(i)
    # print(','.join(map(str, even)))
    return int(''.join(map(str, even))) + int(''.join(map(str, odd)))