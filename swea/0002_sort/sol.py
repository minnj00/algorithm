my_list = [1, 2, 4, 5, 5, 3, 8, 7]

#버블정렬 : 실제 리스트를 바꿈 
# 두개씩 비교하므로 한 싸이클에서 길이의 -1 만큼 반복 
for i in range(len(my_list)-1, 0, -1):  # 점점 줄어드는 만큼 반복함. g한
    for j in range(i):
        left = my_list[j]
        right = my_list[j+1]
        if left > right:
            my_list[j], my_list[j+1] = my_list[j+1], my_list[j]

            # temp = my_list[j]
            # my_list[j] = my_list[j+1]
            # my_list[j+1] = temp  
    
print(my_list)


카운팅정렬 : 새로운 리스트에 새로 정렬한 것을 저장
counter = [0 for i in range(10)]
for i in my_list:
    counter[i] += 1
result = []
for value, count in enumerate(counter):  # 각 숫자와 그 개수의 순서쌍이 프린트됨 
    for i in range(count):
        result.append(value)
print(value)


