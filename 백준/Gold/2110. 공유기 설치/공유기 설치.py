import sys
N, C = map(int, input().split())

houses = []
for _ in range(N):
    h = int(sys.stdin.readline().rstrip())
    houses.append(h)

houses.sort()


def can_connect(max_distance):
    flag = houses[0]
    h_count = 1
    for i in range(1, N):
        if houses[i] >= flag + max_distance:
            flag = houses[i]            
            h_count += 1
    return h_count

low = 0
high = 1000000000
while low < high:
    mid = (low + high) // 2 + 1
    if can_connect(mid) >= C:
        low = mid
    else:
        high = mid - 1
    
print(high)