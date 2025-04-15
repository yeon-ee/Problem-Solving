"""
2
5
aaba
ba
ababa
bbaa
baaba
3
abc
bcd
cde
"""




from itertools import permutations
from collections import deque


def is_pelin(s):
    dq = deque(s)
    while len(dq) != 0:
        left = dq.popleft()
        if len(dq) != 0:
            right = dq.pop()
            if left != right:
                return False
    return True


T = int(input())
output = []
for _ in range(T):
    N = int(input())
    L = []
    for __ in range(N):
        s = input()
        L.append(s)
    permut = permutations(L, 2)
    pelin_exist = False
    
    for tupl in permut:
        s = tupl[0] + tupl[1]
        if is_pelin(s):
            output.append(s)
            pelin_exist = True
            break
    if not pelin_exist:
        output.append(0)

for o in output:
    print(o)