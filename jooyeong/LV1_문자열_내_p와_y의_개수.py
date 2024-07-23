def solution(s):
    p = 0
    y = 0
    for i in s:
        if i == 'p':
            p = p + 1
        elif i == 'y':
            y = y + 1
    if p - y == 0:
        answer = True
    else:
        answer = False
    
    
    return answer