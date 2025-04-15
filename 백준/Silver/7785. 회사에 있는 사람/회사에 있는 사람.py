com = set()

N = int(input())

for _ in range(N):
    name, state = input().split()
    if state == 'enter':
        com.add(name)
    elif state == 'leave':
        com.discard(name)

com = sorted(com)

while len(com) != 0:
    print(com.pop())