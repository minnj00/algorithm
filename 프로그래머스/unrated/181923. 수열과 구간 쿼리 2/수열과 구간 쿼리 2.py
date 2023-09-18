def solution(arr, queries):
    result = []
    for s, e, k in queries:
        mylist = []
        for i in range(s, e+1):
            if arr[i] > k:
                mylist.append(arr[i])
        if len(mylist):
            result.append(min(mylist))
        else:
            result.append(-1)
    return result
            