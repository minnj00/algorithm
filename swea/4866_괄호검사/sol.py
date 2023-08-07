import sys
from pathlib import Path

file_path = Path(__file__).parent
input_path = file_path / 'input.txt'
sys.stdin = open(input_path)

T = int(input())

for tc in range(1, T+1):
    code = input()
    stack = []
    
    for char in code: 
        if char == '(' or char == '{':
            stack.append(char) #stack 에다가 push 함
        # 앞에 있는 친구가 false 면 뒤에 것들은 고려하지도 않음 
        elif len(stack)(# stack 이 비어있지 않으면) and char == ')' and stack[-1] == '(':
            stack.pop()
        elif len(stack) and char == '}' and stack[-1] == '{':
            stack.pop()
        elif char == '}' or char == ')':
            stack.append(char)

    if len(stack) == 0:
        result = 1
    else: 
        result = 0





    # par_list = ['{', '}', '(', ')']
    # my_list = list(input())
    # for i in my_list:
    #     if i == '}':
    #         if '{' in my_list[0:my_list.index[i]]:
    #             my_list.pop('}')
    #             my_list.pop('{')
    #     if i == ')':
    #         if '(' in my_list[0:my_list.index[i]]:
    #             my_list.pop(')')
    #             my_list.pop('(')
    # print(my_list)
            
            