def solution(lines):
    
    s1 = set(i for i in range(lines[0][0], lines[0][1]))
    s2 = set(i for i in range(lines[1][0], lines[1][1]))
    s3 = set(i for i in range(lines[2][0], lines[2][1]))
             
    return len((s1 & s2)|(s1 & s3)|(s2 & s3))
    
    
#     for i in range(len(lines)): 
#         lines[i] = list(range(lines[i][0], lines[i][1]+1))
#     set_1 = set(lines[0]) & set(lines[1])
#     set_2 = set(lines[0]) & set(lines[2])
#     set_3 = set(lines[1]) & set(lines[2])
#     # set_list = list(set_1, set_2, set_3)
#     print(set_1, set_2, set_3)
#     # for j in range(len(set_list)):
#     #     if len(set_list[j]) <= 1:
#     #         set_list[j] = set()
#     if len(set_1) <= 1:
#         set_1 = set()
#     if len(set_2) <= 1:
#         set_2 = set()
#     if len(set_3) <= 1:
#         set_3 = set()
        
#     len_1 = len(set_1)
#     len_2 = len(set_2)
#     len_3 = len(set_3)
    
#     overlap = set_1 & set_2 & set_3
    
#     # result = list((set_1 | set_2) | set_3)
#     result = len_1 + len_2 + len_3 - 3 - 2 * len(overlap) 
    
#     return result - 1 if result else 0











