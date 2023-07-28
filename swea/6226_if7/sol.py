# numbers = range(1,201)
# numbers_7=[]
# for number in numbers:
#     if number % 7 == 0:
#         if number % 5 != 0:
#             numbers_7.append(number)
# print(*numbers_7, sep=',')

#선생님 답변
result = []
for i in range(1,201):
    if i % 7 == 0 and i % 5 != 0:
        result.append(i)

result = map(str,result)
print(','.join(result))

