def solution(board, moves):
    stack = []
    count = 0
    # moves 원소 위치의 열에 맨 위에 있는 인형을 stack 에 쌓음
    for i in moves:
        for j in range(len(board)):
        # 맨 위의 행부터 체크하고 숫자가 있으면 반복문 멈추기
            if board[j][i-1] != 0:
                # print(j, i-1)
                # stack 에 인형을 넣기 전 마지막 인형이 똑같은 인형인지 확인
                if not len(stack) or stack[-1] != board[j][i-1]:
                    # 똑같은 인형위에 쌓는 것이 아니라면 넣기
                    stack.append(board[j][i-1])
                    print(board[j][i-1])
                    board[j][i-1] = 0
                    break
                elif stack[-1] == board[j][i-1]:
                # 똑같은 인형이 맨 위에 있다면 stack에 맨위의 숫자를 삭제후 count에 2더하기
                    board[j][i-1] = 0
                    stack.pop()
                    count += 2
                    break
                # break
    return count