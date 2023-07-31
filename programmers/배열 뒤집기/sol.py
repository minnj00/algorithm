# 간단한 풀이
# def solution(num_list):
#     answer = num_list[::-1]
#     return answer

# der solution(num_list):
#     answer = []
#     num_list.reverse()
#     answer = num_list
#     return answer

# # 다른 풀이 (append)
# def solution(num_list):
#     # 리스트 원소의 길이가 n일 때 n-1 번째 값을 새로운 리스트에 더함

#     answer= []
#     for i in range(len(num_list)):
#         answer.append(num_list[len(num_list)-i])
#     return answer


#insert
# def solution(num_list):
#     # 리스트 원소의 길이가 n일 때 n-1 번째 값을 새로운 리스트에 더함

#     answer= []
#     for i in num_list:
#         answer.insert(0, i) 순서대로 자꾸 앞에 껴놓기 
#     return answer

#지금까지는 데이터 자체를 활용하고 있었음
def solution(num_list):
    answer = []

    for i in range(len(num_list)):
        print(i)
        answer.append(num_list[len(num_list)-i])
    return answer