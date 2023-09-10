def solution(numbers):
    answer = []
    now = 0 # 숫자단어의 첫글자 위치를 now로 두고 숫자를 더할 때마다 now가 단어글자 수만큼 이동
    while now != len(numbers): 
    # 두번째 numbers로 예시를 들어보면 
    # numbers의 index는 0 부터 lent(numbers)-1 까지 
    # now가 len(numbers)가 되면 반복문 멈추기
        if numbers[now] == 'z':
            answer.append(0)
            now += 4
        elif numbers[now] == 'o':
            answer.append(1)
            now += 3
        elif numbers[now] == 't':
            if numbers[now + 1] == 'w':
                answer.append(2)
                now += 3
            elif numbers[now + 1] == 'h':
                answer.append(3)
                now += 5
        elif numbers[now] == 'f':
            if numbers[now + 1] == 'o':
                answer.append(4)
                now += 4
            elif numbers[now + 1] == 'i':
                answer.append(5)
                now += 4
        elif numbers[now] == 's':
            if numbers[now + 1] == 'i':
                answer.append(6)
                now += 3
            elif numbers[now + 1] == 'e':
                answer.append(7)
                now += 5
        elif numbers[now] == 'e':
            answer.append(8)
            now += 5
        else:
            answer.append(9)
            now += 4
        
    return int(''.join(map(str,answer)))



    # 두번쨰 방법
    # number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # 숫자단어 첫 글자를 기준으로 판단
    # z -> 0
    # o -> 1
    # t -> w 2, h 3
    # f -> o 4, i 5
    # s -> i 6, e 7
    # e -> 8
    # n -> 9
    
# 다른 분들은 dictionary로 영어단어와 숫자를 연결해주고 
# numbers 에서 replace 하는 방법으로
    
    