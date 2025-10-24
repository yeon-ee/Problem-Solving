directions = [[0,0], [0,-1],[0,1],[1,0],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]

def solution(board):
    n = len(board)
    safety_board = [[True for i in range(n)] for j in range(n)]
    
    def is_bomb_here(x, y):
        if x < 0 or x >= n or y < 0 or y >= n:
            return False
        elif board[x][y] == 0:
            return False
        else:
            return True
    
    count = 0
    for i in range(n):
        for j in range(n):
            if_safe = True
            for d in directions:
                x, y = i+d[0], j+d[1]
                if is_bomb_here(x, y):
                    if_safe = False
                    break
            if if_safe:
                count += 1
    
    return count