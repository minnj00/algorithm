def solution(X, Y):
    # 여기서 int로 변환해서 시간너무 복잡하게 하지 않기
#     X = list(X)
#     Y = list(Y)
#     # print(X, Y)
#     my_list = []
#     # X의 각각의 원소에 대하여 Y 에 짝꿍이 있으면 Y에서 삭제하고 중복 원소 리스트에 넣기
#     for i in X:
#         if i in Y:
#             my_list.append(i)
#             Y.remove(i)
#     # string(sorted(my_list))
    
#     if not len(my_list):
#         return '-1'
#     elif set(my_list) == {'0'}:
#     # int로 변환할 때 자릿수가 너무 크면 시간이 너무 오래걸림.
#         return '0'
#     else:
#         return ''.join(sorted(my_list, reverse=True))
    X_nums = [0 for i in range(10)]
    Y_nums = [0 for i in range(10)]
    for i in X:
        X_nums[int(i)] += 1
    for i in Y:
        Y_nums[int(i)] += 1
    print(X_nums, Y_nums)
    answer = ''
    for i in range(9, -1 , -1):
        answer += min(X_nums[i], Y_nums[i]) * str(i)
    if not answer:
        return '-1'
    elif set(answer) == {'0'}:
        return '0'
    else:
        return answer
    
    