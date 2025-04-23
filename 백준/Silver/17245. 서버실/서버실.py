N = int(input())

total = 0
servers = []
for _ in range(N):
    line = list(map(int, input().split(' ')))
    for i in line:
        total += i
        servers.append(i)

low = 0
high = max(servers)

def on(minute):
    com_on = 0
    for com in servers:
        com_on += min(minute, com)
    return com_on

while low < high:
    mid = (low + high) // 2
    if on(mid) >= total / 2:
        high = mid 
    else:
        low = mid + 1
print(low)