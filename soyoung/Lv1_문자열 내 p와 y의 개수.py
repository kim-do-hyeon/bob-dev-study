def solution(s):
    a = s.upper()
    str_p = a.count('P')
    str_y = a.count('Y')
    if str_p != str_y :
        return False
    else:
        return True

