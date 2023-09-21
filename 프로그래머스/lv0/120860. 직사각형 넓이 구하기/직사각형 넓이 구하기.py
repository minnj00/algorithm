def solution(dots):
    # x 좌표중 max와 min을 빼고
    # y 좌표중 max와 min을 빼고
    x = [j[0] for j in dots]
    y = [j[1] for j in dots]
    return (max(x)-min(x)) * (max(y)-min(y))

    