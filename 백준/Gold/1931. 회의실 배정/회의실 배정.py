import sys
input = sys.stdin.readline

N = int(input())

L = []

for _ in range(N):
    s, e = map(int, input().split(' '))
    L.append((e,s))

L.sort()
count = 1
e, s = L[0]
for i in range(1, N):
    if L[i][1] >= e:
        count += 1
        e = L[i][0]
print(count)