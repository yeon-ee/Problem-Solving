from itertools import permutations
from math import sqrt


def if_prime(n):
    if n == 1 or n == 0:
        return False
    elif n == 2:
        return True
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def solution(numbers):
    answer = 0
    L = []
    p = []
    for i in range(1, len(numbers)+1):
        p += list(permutations(numbers, i))
    p = set(p)
    for nums in p:
        n = ''
        for num in nums:
            n += num
        L.append(int(n))
    S = set(L)
    for k in S:
        if if_prime(k):
            answer += 1
    return answer
