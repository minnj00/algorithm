
def solution(dart):
    num_list = [str(i) for i in range(0,11)]
    lst = []
    for i in range(len(dart)):
        if dart[i] == '0' and dart[i-1] in num_list: # 0이 나오면 10일 수도 있고 0일수도
            lst.pop()
            lst.append(dart[i-1]+dart[i])
        else:
            lst.append(dart[i]) # dart 문자열을 나눠서 처리하기
    cal = []
    for j in range(len(lst)):
        if lst[j] in num_list:
            if lst[j+1] == 'S':
                cal.append(int(lst[j])**1)
                try:
                    if lst[j+2] == '*':
                        if j == 0: # 맨 처음 숫자라면
                            cal[-1] *= 2
                        else:
                            cal[-1] *= 2
                            cal[-2] *= 2
                    if lst[j+2] == '#':
                        cal[-1] *= -1
                except:
                    continue
            if lst[j+1] == 'D':
                cal.append(int(lst[j])**2)
                try:
                    if lst[j+2] == '*':
                        if j == 0: # 맨 처음 숫자라면
                            cal[-1] *= 2
                        else:
                            cal[-1] *= 2
                            cal[-2] *= 2
                    if lst[j+2] == '#':
                        cal[-1] *= -1
                except:
                    continue
            if lst[j+1] == 'T':
                cal.append(int(lst[j])**3)
                try:
                    if lst[j+2] == '*':
                        if j == 0: # 맨 처음 숫자라면
                            cal[-1] *= 2
                        else:
                            cal[-1] *= 2
                            cal[-2] *= 2
                    if lst[j+2] == '#':
                        cal[-1] *= -1
                except:
                    continue
        else:
            continue
    return sum(cal)
    
#     cal = ['S', 'D', 'T', '*', '#']
#     dic = {}
#     for i in range(len(dart)):
#         if dart[i] in num_list: # 10 도 고려해야함
#             # # if dart[i+1] in num_list:
#             #     dic[dart[i]+dart[i+1]] = []
#             # elif dart[i-1] in num_list:
#             #     continue
#             # else:
#             #     dic[dart[i]] = []
#             if i == 0:
#                 if dart[i+1] in num_list:
#                     dic[dart[i]+dart[i+1]] = []
#                 else:
#                     dic[dart[i]] = []
#             else:
#                 if dart[i+1] in num_list:
#                     dic[dart[i]+dart[i+1]] = []
#                 elif dart[i-1] in num_list:
#                     continue
#                 else:
#                     dic[dart[i]] = []
#         if dart[i] in cal:
#             dic[list(dic.keys())[-1]].append(dart[i])
#     print(dic)
#     # * 이 있으면 그 전 키 밸류값에도 * 넣어주기
#     for i in [1, 2]:
#         if '*' in dic[list(dic.keys())[i]]:
#             dic[list(dic.keys())[i-1]].append('*')
#         else:
#             dic[list(dic.keys())[i-1]].append('1')
#     print(dic)
    
    
    
#     count = 0
#     for i in dic:
#         # print(dic[i].count('*'),dic[i].count('#'))
#         if dic[i][0] == 'S':
#             count += int(i)*2**dic[i].count('*')*(-1)**dic[i].count('#')
#         if dic[i][0] == 'D':
#             count += (int(i)**2)*2**dic[i].count('*')*(-1)**dic[i].count('#')
#         if dic[i][0] == 'T':
#              count += (int(i)**3)*2**dic[i].count('*')*(-1)**dic[i].count('#')
#     return count
# #     count = 0
# #     for i in dic:
# #         if dic[i][0] == 'S':
# #             if len(dic[i]) == 2:
# #                 if dic[1] == '#':
# #                     count += -int(i)**1
# #                 else:
# #                     count += int(i)**1*2
# #                     try: 
# #                         count
# #         elif dic[i][0] == 'D':
# #             count += int(i)**2
# #         else:
# #             count += int(i)**3
# #     for i in dic:
# #         if len(dic[i]) == 2: 
            
            
            