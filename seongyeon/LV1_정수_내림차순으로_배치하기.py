def solution(n):
    n_list = list(str(n))
    n_list.sort(reverse=True)
    n_str = ''.join(n_list)
    return int(n_str)