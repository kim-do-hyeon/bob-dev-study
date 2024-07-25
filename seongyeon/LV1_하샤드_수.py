def solution(x):
    num_list = str(x)
    nums = sum(list(map(int, num_list)))
    if x%nums == 0: return True
    else: return False