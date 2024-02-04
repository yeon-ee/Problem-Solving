n, m = map(int, input().split())

def in_box(x, y):
    return 0 <= x < n and 0 <= y < n

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = 0
cur_x = 0
cur_y = 0
is_valid = True

for i in range(m):
    command, num = input().split()
    num = int(num)
    if command == "MOVE":
        cur_x += num * dx[direction]
        cur_y += num * dy[direction]
    else:
        if num == 0:
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
    if not in_box(cur_x, cur_y):
        is_valid = False
if is_valid:
    print(cur_x, cur_y)
else:
    print(-1)