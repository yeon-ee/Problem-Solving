import sys
sys.setrecursionlimit(10**6)
N = int(input())
a, b, c = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))
C = list(map(int, input().split(" ")))

pos = [0] * (N+1)

for i in A:
    pos[i] = 1
for i in B:
    pos[i] = 2
for i in C:
    pos[i] = 3

if N in A:
    target = 1
elif N in B:
    target = 2
else:
    target = 3

print(target)

answer = 0

def hanoi(N, target):
    global answer
    if N == 1:
        if pos[N] != target:
            answer += 1
        return 0       
    elif pos[N] == target:
        hanoi(N-1, target)
    else:
        mid = pos[N]
        start = 6 - target - mid
        hanoi(N-1, start)
        answer = (answer + pow(2, N-1))%1000000
        
hanoi(N, target)

print(answer)

'''
7
2 2 3
4 3
5 2
7 6 1
'''