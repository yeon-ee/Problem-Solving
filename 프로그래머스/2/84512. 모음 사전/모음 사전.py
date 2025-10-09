from itertools import product
def solution(word):
    L = []
    for i in range(1, 6):
        L += list(product(['A', 'E', 'I', 'O', 'U'], repeat=i))
    L.sort()
    print(L)
    print(len(L))
    return L.index(tuple(word)) + 1