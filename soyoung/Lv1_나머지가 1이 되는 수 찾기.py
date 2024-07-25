def solution(n):
    num = 1
    while 1:
        if (n % num) == 1 :
            return num
        num = num + 1
