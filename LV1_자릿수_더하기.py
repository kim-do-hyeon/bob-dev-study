def solution(n):
    nlist = list(str(n))
    sum = 0
    for i in nlist:
        sum += int(i)
    return sum