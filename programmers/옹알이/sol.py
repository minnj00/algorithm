def solution(babbling):
    answer = 0
    input = babbling
    able = ["aya","y","woo","ma"]
    for a in able:
        for i in range(0, len(input)):
            while a in input[i]:
                answer += 1 
                del input[i]
    return answer

print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
