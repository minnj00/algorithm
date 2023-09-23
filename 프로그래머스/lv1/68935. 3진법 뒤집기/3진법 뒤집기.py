def change(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 
def solution(n):
    
    return int(change(n, 3)[::-1], 3)