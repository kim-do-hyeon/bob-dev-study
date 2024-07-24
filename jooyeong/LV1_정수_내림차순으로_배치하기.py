def solution(n):
    listn = sorted(list(str(n)), reverse = True)
    answer = int("".join(listn))
    return answer