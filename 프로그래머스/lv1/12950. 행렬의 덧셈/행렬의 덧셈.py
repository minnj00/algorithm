def solution(arr1, arr2):
    matrix = [[0 for i in range(len(arr1[0]))] for j in range(len(arr1))]
    # print(matrix)
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            matrix[i][j] = arr1[i][j] + arr2[i][j]
    return matrix