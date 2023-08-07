import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    list1 = []
    for i in str1:
        if i in list1:
            pass
        else: 
            list1.append(i)
    my_dict = {}
    for i in list1:
        for j in str2:
            if i == j:
                if i in my_dict.keys():
                    my_dict[i] += 1
                else: 
                    my_dict[i] = 1
    max_num =max(my_dict.values())
    # print(max_num)
    print (f'#{tc} {max_num}')

    
    # print(list1)


        
        
