blood_type = ['A','A','A','O','B','B','O','AB','AB','O']

num_a = 0
num_b = 0
num_ab = 0
num_o = 0

for i in range(0,len(blood_type)):
    
    if blood_type[i] == 'A':
        num_a += 1
    elif blood_type[i] == 'B':
        num_b += 1
    elif blood_type[i] == 'AB':
        num_ab += 1
    else: 
        num_o += 1

blood_dict = {
    'A': num_a,
    'O': num_o,
    'B': num_b,
    'AB': num_ab
}

print(blood_dict)

# 파일 디렉토리 이동할 떄 .. 은 그 상위폴더로 이동할 떄 사용함
# vscode 열 때도 algorithm 폴더에서 여는 걸 추천

# blood_list = ['A','A','A','O','B','B','O','AB','AB','O']
# blood_dict = {
#     'A': 0,
#     'O': 0,
#     'B': 0,
#     'AB': 0,
# }

# for blood in blood_list:
#     blood_dict[blood] += 1 #key 에 따른 value를 바로 증가시킴
# print(blood_dict)

location_list = ['서울','부산','서울','서울','대전','제주','광주','부산']

location_dict = {}

for location in location_list:
    #이미 기록은 한 경우
    if location in location_dict.keys():
        location_dict[location] += 1
    #처음 등장한 경우
    else: 
        location_dict[location] = 1 # ex) location_dict['서울'] = 1
print(location_dict)
