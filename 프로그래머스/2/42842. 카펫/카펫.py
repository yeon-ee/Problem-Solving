def solution(brown, yellow):
    for ver in range(3, brown):
        hor = int((brown - (ver - 2) * 2) / 2)
        if yellow == (ver - 2) * (hor - 2):
            return [hor, ver]