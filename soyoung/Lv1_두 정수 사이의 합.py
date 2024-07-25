def solution(a, b):
    if a > b :
        a,b = b,a
    answer = 0
    while a != b :
        answer = answer + a
        a = a+1
    return answer + b