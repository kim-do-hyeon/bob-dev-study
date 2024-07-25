import math

def solution(n):
    m = int(math.sqrt(n))
    if n == m**2: return (m+1)**2
    else: return -1