n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

box = [-1] * (n * m)

def in_box(x, y):
    return 0 <= x < n and 0 <= y < m

def index(x, y):
    return y * n + x

cur_x = 0
cur_y = 0
direction = 0
finished = 0
empty_count = n * m

while empty_count > 0:
    if box[index(cur_x, cur_y)] == -1:
        box[index(cur_x, cur_y)] = 0
        empty_count -= 1
    nex_x = cur_x + dx[direction]
    nex_y = cur_y + dy[direction]
    if in_box(nex_x, nex_y) and box[index(nex_x, nex_y)] == -1:
        cur_x = nex_x
        cur_y = nex_y
    else:
        direction = (direction + 1) % 4

print(cur_x, cur_y)