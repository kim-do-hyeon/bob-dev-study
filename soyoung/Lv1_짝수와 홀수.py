def solution(num):
    if num%2 == 0 : 
        # 2로 나눈 나머지가 없으면 짝수
        return "Even" 
    else :
        # 나머지가 존재하면 홀수
        return "Odd"
