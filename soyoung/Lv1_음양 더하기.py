def solution(absolutes, signs):
    answer = 0
    for i in range(len(absolutes)):
        if signs[i] == 1:
            answer = answer + absolutes[i]
        else:
            answer = answer - absolutes[i]

    return answer