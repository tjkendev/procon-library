# S[i][j] = '#' → (i, j) は 通り抜け不可
# S[i][j] = '.' → (i, j) は 通り抜け可能

from collections import deque
dd = ((-1, 0), (0, -1), (1, 0), (0, 1))
# 
def bfs(S, H, W, r0, c0):
    dist = [[-1]*W for i in range(H)]
    que = deque([(r0, c0)])
    dist[r0][c0] = 0
    while que:
        r, c = que.popleft()
        cur = dist[r][c]
        for dr, dc in dd:
            nr = r + dr; nc = c + dc
            if not 0 <= nr < H or not 0 <= nc < W or S[nr][nc] == '#':
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = cur+1
                que.append((nr, nc))
    return dist

H = 4; W = 5
S = [
    "#....",
    "#.##.",
    "....#",
    "#....",
]
dist = bfs(S, H, W, 1, 4)
for line in dist:
    print(" ".join(map("{:2d}".format, line)))
# =>
# -1  4  3  2  1
# -1  5 -1 -1  0
#  7  6  7  8 -1
# -1  7  8  9 10