def solution(s):
    # 모두 대문자로 바꾸어 갯수 확인
    a = s.upper()
    str_p = a.count('P')
    str_y = a.count('Y')
    if str_p != str_y :
        return False
    else:
        return True

