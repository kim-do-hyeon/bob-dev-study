def solution(n):
    answer = 0
    number = list(str(n))
    for i in number:
        answer += int(i)
    return answer