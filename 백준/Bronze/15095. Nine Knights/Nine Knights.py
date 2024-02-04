dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

knights =[]

is_valid = True

for i in range(5):
    row = input()
    for k in range(5):
        if row[k] == 'k':
            knights.append([i, k])

if len(knights) != 9:
    is_valid = False
else:
    for i in range(9):
        x, y = knights[i]
        for k in range(8):
            for j in range(i,9):
                if x + dx[k] == knights[j][0] and y + dy[k] == knights[j][1]:
                    is_valid = False
                    break

if is_valid:
    print("valid")
else:
    print("invalid")