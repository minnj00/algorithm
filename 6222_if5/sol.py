import sys
sys.stdin = open('input.txt')

char = input()

# if char.isupper():
#     print(f'{char}(ASCII: {ord(char)}) => {char.lower()}(ASCII: {ord(char.lowerr())})')
# else:
#     print(f'{char}(ASCII: {ord(char)}) => {char.upper()}(ASCII: {ord(char.upper())})')


#선생님 답변 (다른 거 있으면 적음)
if char.isupper(): 
    result = char.lower()
else:
    result = char.upper()
print(char, result)
print(ord(char), ord(result))



