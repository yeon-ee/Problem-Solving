from collections import defaultdict, deque

def get_steps(x1, y1, x2, y2):
    steps = []
    if x1 == x2:
        for i in range(y1, y2):
            steps.append([x1, i, x2, i+1])
    elif y1 == y2:
        for i in range(x1, x2):
            steps.append([i, y1, i+1, y2])
    return steps

def get_edges(rec):
    edges = []
    x1, y1, x2, y2 = rec
    edges += get_steps(x1, y1, x2, y1)
    edges += get_steps(x1, y1, x1, y2)
    edges += get_steps(x1, y2, x2, y2)
    edges += get_steps(x2, y1, x2, y2)
    return edges

def if_inside(edge, rec):
    x1, y1, x2, y2 = edge
    rx1, ry1, rx2, ry2 = rec
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2
    if rx1 < x < rx2 and ry1 < y < ry2:
        return True
    return False


def string(x, y):
    return str(x) + ',' + str(y)

def solution(rectangle, characterX, characterY, itemX, itemY):
    edges = []
    for rec in rectangle:
        edges += get_edges(rec)
    roads = defaultdict(list)
    for edge in edges:
        add_road = True
        for rec in rectangle:
            if if_inside(edge, rec):
                add_road = False
        if add_road:
            x1, y1, x2, y2 = edge
            roads[string(x1, y1)].append(string(x2, y2))
            roads[string(x2, y2)].append(string(x1, y1))
    target = string(itemX, itemY)
    q = deque([[string(characterX, characterY), 0]])
    visited = {point: False for point in roads.keys()}
    while q:
        cur_loc, count = q.popleft()
        if cur_loc == target:
            return count
        for next_loc in roads[cur_loc]:
            if not visited[next_loc]:
                visited[next_loc] = True
                q.append([next_loc, count + 1])
    return 0